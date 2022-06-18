// 완성
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include "mymessage.h"

int main(int argc, char *argv[])
{
	int qid_c, qid_s, other;
	long type;
	struct umsg msg_send, msg_recv;

	if (argc != 2) {
		fprintf(stderr, "usage %s [client number]\n", argv[0]);
		perror("msgq");
		exit(1);
	}

	if ((qid_s = msgget((key_t)0x20003761, IPC_CREAT|0660)) == -1) { 
          perror("msgget");
          exit(1);
    }

	if (atoi(argv[1]) == 1) {
		if ((qid_c = msgget((key_t)0x20003762, IPC_CREAT|0660)) == -1) { 
			perror("msgget");
			exit(1);
		}
		printf("message queue 0x20003762 생성\n");
		type = (long)100;
		other = 2;
	}
	else if (atoi(argv[1]) == 2){
		if ((qid_c = msgget((key_t)0x20003763, IPC_CREAT|0660)) == -1) { 
			perror("msgget");
			exit(1);
		}
		printf("message queue 0x20003763 생성\n");
		type = (long)200;
		other = 1;
	}
	else {
		perror("wrong argument");
		exit(1);
	}
	
	while(1) {
		memset(msg_send.mtext, 0, MSIZE);
		printf("Text to send: ");
		fgets(msg_send.mtext, sizeof(msg_send.mtext), stdin);
		msg_send.mtext[strlen(msg_send.mtext)-1] = '\0';
		msg_send.mtype = type;
		msgsnd(qid_s, &msg_send, strlen(msg_send.mtext), 0);
		printf("send to client%d : %s\n", other, msg_send.mtext);
		memset(msg_recv.mtext, 0, MSIZE);
		msgrcv(qid_c, &msg_recv, (size_t)MSIZE, 0, 0);
		msg_recv.mtext[strlen(msg_recv.mtext)] = '\0';
		printf("recv from client%d : %s\n", other, msg_recv.mtext);
			
		if (strncmp(msg_recv.mtext, "quit", 4) == 0) { 
			msg_send.mtype = type;
			strncpy(msg_send.mtext, "quit", 4);
			msg_send.mtext[4] = '\0';
			msgsnd(qid_s, &msg_send, strlen(msg_send.mtext), 0);
			printf("received 'quit' and sended 'quit'\n");
			break;
		}
	}
	
	printf("message queue를 제거\n");
	msgctl(qid_c, IPC_RMID, NULL);
	printf("프로그램 종료\n");
	return 0;
}
