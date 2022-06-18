// 컴퓨터전자시스템공학부 202000376 김가은
// 정상동작

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <ctype.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <time.h>


struct record {
	char acc_no[6];
	char name[10];
	int balance;
};

int reclock(int fd, int recno, int len, int type) {
	struct flock fl;

	switch (type) {
	case F_RDLCK:
	case F_WRLCK:
	case F_UNLCK:
		fl.l_type = type;
		fl.l_whence = SEEK_SET;
		fl.l_start = recno * len;
		fl.l_len = len;
		fcntl(fd, F_SETLKW, &fl);
		return 1;
	default:
		return -1;
	}
}

void random_usleep(void) {
	long t;
	srand(time(NULL));
	t = rand() % 1000001;
	usleep(t);
}

void do_operation(int ofd, int pid) {
	struct record current;
	char operation[200];
	ssize_t n;
	int fdop;
	FILE* foperation;
	char curr_acc_no[5];
	char curr_optype_str[2];
	char curr_optype;
	char curr_amount[6];
	int curr_record_no;
	int continue_flag = 0;

	fdop = open("./operation.dat", O_RDONLY);
	foperation = fdopen(fdop, "r");

	while (1) {
		if (fgets(operation, sizeof(operation), foperation) == NULL) break;
		strncpy(curr_acc_no, operation, 4);
		curr_acc_no[4] = '\0';
		strncpy(curr_optype_str, operation + 5, 1);
		curr_optype_str[1] = '\0';
		curr_optype = curr_optype_str[0];
		if (curr_optype != 'i') {
			strncpy(curr_amount, operation + 7, 5);
			curr_amount[5] = '\0';
		}

		// curr_acc_no 에 해당하는 curr_record_no 를 ofd에서 찾기
		for (int i = 0; i < 5; i++) {
			lseek(ofd, i * sizeof(struct record), SEEK_SET);
			n = read(ofd, &current, sizeof(struct record));
			if (strcmp(current.acc_no, curr_acc_no) == 0) {
				curr_record_no = i;
				break;
			}
			else {
				if (i == 4) {
					fprintf(stdout, "계좌정보 없음\n");
					continue_flag = 1;
				}
			}
		}

		if (continue_flag == 1) {
			random_usleep();
			continue_flag = 0;
			continue;
		}

		// operation하고 화면에 결과 출력하기
		switch (curr_optype) {
		case 'w':
			reclock(ofd, curr_record_no, sizeof(struct record), F_WRLCK);

			lseek(ofd, curr_record_no * sizeof(struct record), SEEK_SET);
			n = read(ofd, &current, sizeof(struct record));

			current.balance -= atoi(curr_amount);

			lseek(ofd, curr_record_no * sizeof(struct record), SEEK_SET);
			write(ofd, &current, sizeof(struct record));

			fprintf(stdout, "pid:	%d	acc_no: %s	withdraw: %s	balance: %d\n", pid, curr_acc_no, curr_amount, current.balance);

			reclock(ofd, curr_record_no, sizeof(struct record), F_UNLCK);
			break;
		case 'd':
			reclock(ofd, curr_record_no, sizeof(struct record), F_WRLCK);

			lseek(ofd, curr_record_no * sizeof(struct record), SEEK_SET);
			n = read(ofd, &current, sizeof(struct record));

			current.balance += atoi(curr_amount);

			lseek(ofd, curr_record_no * sizeof(struct record), SEEK_SET);
			write(ofd, &current, sizeof(struct record));

			fprintf(stdout, "pid:	%d	 acc_no: %s	deposit: %s	balance: %d\n", pid, curr_acc_no, curr_amount, current.balance);

			reclock(ofd, curr_record_no, sizeof(struct record), F_UNLCK);
			break;
		case 'i':
			reclock(ofd, curr_record_no, sizeof(struct record), F_RDLCK);

			lseek(ofd, curr_record_no * sizeof(struct record), SEEK_SET);
			n = read(ofd, &current, sizeof(struct record));

			// 출력
			fprintf(stdout, "pid:	%d	acc_no: %s	inquiry	balance: %d\n", pid, curr_acc_no, current.balance);

			reclock(ofd, curr_record_no, sizeof(struct record), F_UNLCK);
			break;
		default:
			fflush(stdout);
		};
		random_usleep();
	}

	fflush(stdout);
	close(ofd);
	close(fdop);

	exit(0);
}

int main(int argc, char* argv[])
{
	int cpid[10];
	int pid;
	struct record current;
	ssize_t n;
	int fdacc, fdop;
	char line[200];
	FILE* fop;

	for (int i = 0; i < 10; i++) {
		cpid[i] = fork();
		if (cpid[i] == 0) {
			fdacc = open("./account.dat", O_RDWR);
			do_operation(fdacc, getpid());
		}
	}


	for (int i = 0; i < 10; i++) {
		waitpid(cpid[i], NULL, 0);
	}

	// account.dat 에 기록된 모든 계좌 내용을 화면에 출력
	fdacc = open("./account.dat", O_RDONLY);

	for (int i = 0; i < 5; i++) {
		lseek(fdacc, i * sizeof(struct record), SEEK_SET);
		n = read(fdacc, &current, sizeof(struct record));
		printf("acc_no: %s	balance: %d\n", current.acc_no, current.balance);
	}

	close(fdacc);
	return 0;
}

