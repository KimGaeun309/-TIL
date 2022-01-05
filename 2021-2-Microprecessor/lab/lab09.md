## Lab 9-1

* code

main.c
``` C
#include "stm32f10x_lib.h"
#include "System_func.h"

void putch(u8 c);
void puts(u8 *s);

int main() {
  Init_STM32F103();
  
  USART_InitTypeDef USART_InitStructure;
  GPIO_InitTypeDef GPIO_InitStructure;
  
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA | RCC_APB2Periph_USART1, ENABLE);
  
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP; 
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_9;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_Init(GPIOA, &GPIO_InitStructure);
  
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING; 
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_10;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_Init(GPIOA, &GPIO_InitStructure);
  
  USART_InitStructure.USART_BaudRate = 9600;
  USART_InitStructure.USART_WordLength = USART_WordLength_8b;
  USART_InitStructure.USART_StopBits = USART_StopBits_1; 
  USART_InitStructure.USART_Parity = USART_Parity_No; 
  USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None; 
  USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;
  USART_InitStructure.USART_Clock = USART_Clock_Disable;
  USART_InitStructure.USART_CPOL = USART_CPOL_Low; 
  USART_InitStructure.USART_CPHA  =USART_CPHA_2Edge; 
  USART_InitStructure.USART_LastBit = USART_LastBit_Disable; 
  USART_Init(USART1, &USART_InitStructure); 
  
  USART_Cmd(USART1, ENABLE); 
  
  putch('H');
  putch('e');
  putch('l');
  putch('l');
  putch('o');
  puts("\n\rWorld!!");
  
  while(1);
}

void putch(u8 c)
{
  USART_SendData(USART1, c);
  while (USART_GetFlagStatus(USART1, USART_FLAG_TXE) == RESET); 
}

void puts(u8 *s) 
{
  while (*s != '\0')
  {
    putch(*s);
    s++;
  }
}

```
stm32f10x_conf.h 
``` C
#define _USART
#define _USART1

```
* 코드 설명

main.c에서 main() 함수를 실행하기 전에 프로그램에 필요한 헤더를 선언하고 USART1으로 한 문자를 전송하는 함수 putch()와 USART1로 문자열을 전송하는 함수 puts()를 선언합니다. 
main() 함수에서는 시스템을 초기화해준 후 USART를 설정할 때 사용할 구조체 USART_InitStructure와 GPIO를 설정할 때 사용할 구조체 GPIO_InitStructure 를 가져온 뒤, RCC_APB2PeriphClockCmd() 함수를 사용해 GPIOA와 USART1의 클럭을 설정해줍니다.
GPIO_InitStructure를 사용해 Tx(=GPIOA의 9pin)는 Alternate Function Push-Pull 으로 설정해 output으로 사용하고, Rx(=GPIOA의 10pin)는 input 으로 사용하도록 설정하고 GPIO_Init() 함수로 GPIOA를 이 data structure로 초기화해줍니다.
USART_InitStructure를 사용해 통신 규격을 맞춰주는데, 보우레이트는 9600bps로, 데이터 길이는 8비트로, 스톱비트는 1로, 패리티와 하드웨어 흐름제어는 없음으로, USART_Clock는 disable 해주고, 폴라리티는 low, edge는 3edge로 설정해주고 마지막 비트는 disable해주도록 설정하고 USART_Init() 함수로 USART_1을 이 data structure로 초기화해줍니다.
그리고 USART_Cmd() 함수를 사용해 USART1을 Enable 시켜준 다음, putch() 함수를 사용해 Hello를 출력하고, puts() 하무슬ㄹ 사용해 World! 문자열을 출력한 후 while(1) 반복문으로 main()이 끝나지 않도록 해줍니다.
putch() 함수에서는 문자 c를 매개변수로 받아 USART_SendData() 함수를 이용해 문자 c를  DR 레지스터에 써줍니다. 그리고 데이터가 다 전송이 되었는지 확인될 때까지 시간을 지연시키기 위해 TXE레지스터가 0인 동안 대기하도록 while (USART_GeFlagStatus(USART1, USART_FLAG_TXE) == RESET) 코드를 작성해줍니다.
putch() 함수에서는 문자열 *s를 매개변수로 받아 포인터 값을 증가시켜 널 문자에 도달하기 전까지 문자열의 문자들을 차례대로 탐색하며 putch() 함수를 사용해 DR레지스터에 써주어 문자열을 DR 레지스터에 써주도록 코드를 작성하였습니다.
stm32f10x_conf.h 에서  #define _USART와 #define _USART1 의 주석 처리를 풀어줍니다.


## Lab 9-2

* code

main.c
``` C
#include "stm32f10x_lib.h"
#include "System_func.h"

void putch(u8 c);
void puts(u8 *s);
unsigned char getch();

int main() {
  Init_STM32F103();
  
  USART_InitTypeDef USART_InitStructure;
  GPIO_InitTypeDef GPIO_InitStructure;
  
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA | RCC_APB2Periph_USART1, ENABLE);
  
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP; 
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_9;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_Init(GPIOA, &GPIO_InitStructure);
  
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING; 
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_10;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_Init(GPIOA, &GPIO_InitStructure);
  
  USART_InitStructure.USART_BaudRate = 9600;
  USART_InitStructure.USART_WordLength = USART_WordLength_8b;
  USART_InitStructure.USART_StopBits = USART_StopBits_1;  
  USART_InitStructure.USART_Parity = USART_Parity_No; 
  USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None; 
  USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;
  USART_InitStructure.USART_Clock = USART_Clock_Disable;
  USART_InitStructure.USART_CPOL = USART_CPOL_Low; 
  USART_InitStructure.USART_CPHA  =USART_CPHA_2Edge; 
  USART_InitStructure.USART_LastBit = USART_LastBit_Disable; 
  USART_Init(USART1, &USART_InitStructure); 
  
  USART_Cmd(USART1, ENABLE); 
  
  puts("Hello");
  puts("\n\rEnter Name: ");

  while(1) {
    unsigned char data = getch();
    putch(data);
  }
}

void putch(u8 c)
{
  USART_SendData(USART1, c);
  while (USART_GetFlagStatus(USART1, USART_FLAG_TXE) == RESET); 
}

unsigned char getch() {
  unsigned char key = 0;
  while(USART_GetFlagStatus(USART1, USART_FLAG_RXNE) == RESET){} 
  key = USART_ReceiveData(USART1); 
  return key;
                            
}

void puts(u8 *s) 
{
  while (*s != '\0')
  {
    putch(*s);
    s++;
  }
}



```
stm32f10x_conf.h 
``` C
#define _USART
#define _USART1

```

* 코드 설명

실습 9-1의 코드와의 차이점만을 설명하겠습니다.
이 코드에서는 들어온 데이터를 DR레지스터로부터 읽어오는 함수 getch()도 선언해줍니다.
그리고 main() 함수에서 puts() 함수를 사용해 Hello 와 Enter Name: 를 전송하고, 수신받은 데이터를 그대로 송신하기 위해 while(1)문에서 getch() 함수로 수신받은 데이터를 putch() 함수를 사용해 다시 전송해줍니다.
getch() 함수는 값이 DR레지스터로 들어올 대가지 기다려야 하므로 RXNE 레지스터의 값을 확인하기 위해 while(USART_GetFlagStatus(USART1, USART_FLAG_RXNE) == RESET){} 으로 값이 들어올 때까지 시간을 지연시켰다가, 값이 들어오면 while문을 빠져나와 key 변수에 USART_ReceiveData() 함수를 통해 입력받은 값을 저장하고 key 를 리턴해주어 값을 수신받으면 그 값을 리턴하도록 코드를 작성하였습니다.

