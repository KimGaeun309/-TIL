// 실행 오류
// 실행시켰을 때 세 개의 프로세스가 모두 종료되지만
// P에서와 달리 C1, C2에서는입력 파일의 끝에 도달하지 못한 채로 프로세스가 종료되며,
// c1-out.txt 와 c2-out.txt 파일에는 문장은 저장되지 못하고 Line 수와 Word 수가 모두 0인 상태만 출력됩니다.

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/wait.h>

#define BUFFER_SIZE 1024

int main(int argc, char* argv[])
{
	int fd1[2];
	int fd2[2];
	char ubuf[BUFFER_SIZE];
	char buf1[BUFFER_SIZE], buf2[BUFFER_SIZE];
	int pid1, pid2, status;
	FILE* p_stream;

	p_stream = fopen(argv[1], "r");

	pipe(fd1);
	pipe(fd2);

	pid1 = fork();
	pid2 = fork();

	if (pid1 == 0) { // child 1
		int line_cnt1 = 0;
		int word_cnt1 = 0;
		int n1, c1_des;
		FILE* c1_out;
		FILE* fd1_read = fdopen(fd1[0], "r");

		c1_des = creat("c1-out.txt", 0777);
		c1_out = fdopen(c1_des, "w");

		close(fd1[1]);
		close(fd2[0]);
		close(fd2[1]);
		
		while ((n1 = read(fd1[0], buf1, BUFFER_SIZE)) != 0) {
			line_cnt1 += 1;
			word_cnt1 += 1;
	
			for (int i = 0; i < n1; i++) {
				if (buf1[i] == '\n')
					break;
				else if (buf1[i] >= 97 && buf1[i] <= 122)
					buf1[i] -= 32;
				else if (buf1[i] == ' ')
					word_cnt1 += 1;
				
			}
	
			write(c1_des, buf1, n1);
				
		}
		
			

		fprintf(c1_out, "Line : %d, Word : %d\n", line_cnt1, word_cnt1);

		if (feof(p_stream) != 0) {
			printf("입력 파일의 끝에 도달하였습니다. (C1)\n");
		}
		else {
			printf("입력 파일의 끝에 도달하지 못했습니다. (C1)\n");
		}

		close(fd1[0]);
		fclose(c1_out);
		close(c1_des);
		fclose(p_stream);
		fclose(fd1_read);
		printf("Goodbye from C1\n");
		exit(0);

	}
	if (pid2 == 0) { // child 2
		int line_cnt2 = 0;
		int word_cnt2 = 0;
		int n2;
		int c2_des;
		FILE* c2_out;
		FILE* fd2_read = fdopen(fd2[0], "r");
		
		c2_des = creat("c2-out.txt", 0777);
		c2_out = fdopen(c2_des, "w");
		

		close(fd2[1]);
		close(fd1[0]);
		close(fd1[1]);

		
		while ((n2 = read(fd2[0], buf2, BUFFER_SIZE)) != 0) {

			line_cnt2 += 1;
			word_cnt2 += 1;
		
			for (int j = 0; j < n2; j++) {
				if (buf2[j] == '\0')
					break;
				else if (buf2[j] >= 65 && buf2[j] <= 90)
					buf2[j] += 32;
				if (buf2[j] == ' ')
					word_cnt2 += 1;
			}
			write(c2_des, buf2, n2);
			
		}

		fprintf(c2_out, "Line : %d, Word : %d\n", line_cnt2, word_cnt2);


		if (feof(p_stream) != 0) {
			printf("입력 파일의 끝에 도달하였습니다. (C2)\n");
		}
		else {
			printf("입력 파일의 끝에 도달하지 못했습니다. (C2)\n");
		}

		fclose(c2_out);
		close(c2_des);
		close(fd2[0]);
		fclose(p_stream);
		fclose(fd2_read);
		printf("Goodbye from C2\n");
		exit(0);
	}
	else {
		int cnt;

		close(fd1[0]);
		close(fd2[0]);

		FILE* fd1_write = fdopen(fd1[1], "w");
		FILE* fd2_write = fdopen(fd2[1], "w");

		cnt = 0;
		while (fgets(ubuf, BUFFER_SIZE, p_stream) != NULL) {
			cnt += 1;

			if (cnt % 2 == 1) {
				fputs(ubuf, fd1_write);
			}
			else if (cnt % 2 == 0) {
				fputs(ubuf, fd2_write);
			}

		}
		
		close(fd1[1]);
		close(fd2[1]);
		
		if (feof(p_stream) != 0) {
			printf("입력 파일의 끝에 도달하였습니다. (P)\n");
		}
		else {
			printf("입력 파일의 끝에 도달하지 못했습니다. (P)\n");
		}

		fclose(p_stream);
		fclose(fd1_write);
		fclose(fd2_write);
		printf("Goodbye from P\n");

		waitpid(pid1, &status, 0);
		waitpid(pid2, &status, 0);
		exit(0);
	}

	return 0;
}

