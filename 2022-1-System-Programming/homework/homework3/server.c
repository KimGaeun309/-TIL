// 202000376 김가은
// 완성
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include "mymessage.h"

int main(int argc, char *argv[])
{
	int qid_c1, qid_c2, qid_s;
	int quit_cnt = 0;
	struct umsg msg_s;
	if ((qid_s = msgget((key_t)0x20003761, IPC_CREAT|0660)) == -1) { 
          perror("msgget");
          exit(1);
    }
	printf("message queue 0x20003761 생성\n");
	msg_s.mtype = (long)0;

	if ((qid_c1 = msgget((key_t)0x20003762, IPC_CREAT|0660)) == -1) { 
		perror("msgget");
		exit(1);
	}
	if ((qid_c2 = msgget((key_t)0x20003763, IPC_CREAT|0660)) == -1) {
		perror("msgget");
		exit(1);
	}
	
	while(1) {
		memset(msg_s.mtext, 0, MSIZE);
		msgrcv(qid_s, &msg_s, (size_t)MSIZE, (long)100, 0);
		msg_s.mtext[strlen(msg_s.mtext)] = '\0';
		printf("recv from client1 : %s\n", msg_s.mtext);
		msgsnd(qid_c2, &msg_s, strlen(msg_s.mtext), 0);
		printf("send to client2 : %s\n", msg_s.mtext);
		if (strncmp(msg_s.mtext, "quit", 4) == 0) {
			quit_cnt += 1;
			if (quit_cnt >= 2) break;
		}
		memset(msg_s.mtext, 0, MSIZE);
		msgrcv(qid_s, &msg_s, (size_t)MSIZE, (long)200, 0);
		msg_s.mtext[strlen(msg_s.mtext)] = '\0';
		printf("recv from client2 : %s\n", msg_s.mtext);
		msgsnd(qid_c1, &msg_s, strlen(msg_s.mtext), 0);

		printf("send to client1 : %s\n", msg_s.mtext);
		if (strncmp(msg_s.mtext, "quit", 4) == 0) {
			quit_cnt += 1;
			if (quit_cnt >= 2) break;
		}
	}
	
	printf("message queue를 제거\n");
	msgctl(qid_s, IPC_RMID, NULL);
	printf("프로그램 종료\n");
	return 0;
}
