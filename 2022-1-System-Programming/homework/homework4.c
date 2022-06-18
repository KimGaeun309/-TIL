// 오류 : client 프로세스를 실행시켜 connect 시키면 server 프로세스에서 recv() 에서 error가 발생하여 음수 값을 반환하는 문제가 있습니다.

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <pthread.h>
#include <string.h>

#define MAX 1024
#define PORT 30376
#define BACKLOG 5

int ch_sd[50];
char kv[100][2][50];

char* find_value(char* key) {
	for (int i=0; i<100; i++) {
		if (strcmp(kv[i][0], key) == 0) {
			return kv[i][1];
		}
	}
	return NULL;
}

void update_value(char* key, char* value) {
	for (int i=0; i<100; i++) {
		if (strcmp(kv[i][0], key) == 0) {
			strcpy(kv[i][1], value);
		}
	}
}

int insert_key(char* key, char* value) {
	for (int i=0; i<100; i++) {
		if (kv[i][0] == NULL) {
			strcpy(kv[i][0], key);
			strcpy(kv[i][1], value);
			return 0;
		}
	}
	return 1;
}

void *threadFunc(void * param) {
	int bytes, idx;
	char recv_data[MAX], send_data[MAX];
	char* token = NULL;
	char* context = NULL;
	char* key = NULL;
	char* value = NULL;
	char * idx_str = NULL;
	idx_str = (char *) param;
	idx = atoi(idx_str);
	
	while(1) {

		bytes = recv(ch_sd[(int)idx], recv_data, MAX, 0);
		
		if (bytes == 0) break;
		else if (bytes < 0) {
			fprintf(stderr, "can't receive data.\n");
			exit(1);
		}

		token = strtok_r(recv_data, " ", &context);
		

		if (strcmp(token, "quit") == 0) { 
			strcpy(send_data, "quit_ack");
			bytes = sizeof(send_data);
			if (send(ch_sd[(int)idx], send_data, bytes, 0) != bytes) {
				fprintf(stderr, "can't send data.\n"); exit(1);
			}
			pthread_exit((void*)pthread_self());
		}
		else if (strcmp(token, "read") == 0) {
			key = strtok_r(recv_data, " ", &context);
			value = find_value(key);
			if (value == NULL) {
				sprintf(send_data, "%02d read Failed\n", (int)idx + 1);	
			}
			else {
				strcpy(value, find_value(key));
				sprintf(send_data, "%02d read : %s %s\n", (int)idx + 1, key, value);
			}
			fprintf(stdout, "client %02d : read %s %s\n", (int)idx + 1, key, value);
		}
		else if (strcmp(token, "update") == 0) {
			key = strtok_r(recv_data, " ", &context);
			value = strtok_r(recv_data, " ", &context);
			if (find_value(key) == NULL) {
				sprintf(send_data, "%02d update Failed\n", (int)idx + 1);
			}
			else {
				update_value(key, value);
				sprintf(send_data, "%02d update OK: %s %s\n", (int)idx + 1, key, value);
			}
			fprintf(stdout, "client %02d : update %s %s\n", (int)idx + 1, key, value);
		}
		else if (strcmp(token, "insert") == 0) {
			key = strtok_r(recv_data, " ", &context);
			value = strtok_r(recv_data, " ", &context);
			if (find_value(key) != NULL) {
				sprintf(send_data, "%02d insert Failed : key Exist\n", (int)idx + 1);
			}
			else if (insert_key(key, value) != 0) {
				sprintf(send_data, "%02d insert Failed\n", (int)idx + 1);
			}
			else {
				sprintf(send_data, "%02d insert %s %s\n", (int)idx + 1, key, value);
			}
			fprintf(stdout, "client %02d : insert %s %s\n", (int)idx + 1, key, value);
		}
		bytes = sizeof(send_data);
		if (send(ch_sd[(int)idx], send_data, bytes, 0) != bytes) {
			fprintf(stderr, "can't send data.\n"); exit(1);
		}
	}

	//pthread_exit((void*)pthread_self());
}

int main(int argc, char *argv[])
{
	pthread_t t[50];
	struct sockaddr_in servaddr, cliaddr;
	int sd, nsd, cliaddsize, t_idx;
	char t_idx_str[10];

	if ((sd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
		fprintf(stderr, "can't open socket.\n");
		exit(1);
	}
	
	memset(ch_sd, -1, sizeof(ch_sd));

	bzero((char*)&servaddr, sizeof(servaddr));
	servaddr.sin_family = AF_INET;
	servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
	servaddr.sin_port = htons(PORT);
	
	if (bind(sd, (struct sockaddr*)&servaddr, sizeof(servaddr)) < 0) {
		fprintf(stderr, "can't bind to socket.\n");

		exit(1);
	}
	
	listen(sd, BACKLOG);
	
	t_idx = 0; // thread idx

	while(1) {

		cliaddsize = sizeof(cliaddr);
		if ((nsd = accept(sd, (struct sockaddr *)&cliaddr, &cliaddsize) < 0)) {
			fprintf(stderr, "can't accept connection/\n");
			exit(1);
		}
		
		ch_sd[t_idx] = nsd;

		sprintf(t_idx_str, "%d", t_idx);
		pthread_create( &t[t_idx], NULL, threadFunc, t_idx_str);
		
		t_idx += 1;

	}

	
	
	return 0;
}
