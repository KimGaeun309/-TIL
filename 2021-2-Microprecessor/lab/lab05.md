## Lab 5-1
* code

``` C
#include "stm32f10x_lib.h"
#include "System_func.h"

void Delay(vu32 nCount);
void Delay(vu32 nCount){
  for(; nCount != 0; nCount--); 
}

int main(void)
{
  Init_STM32F103();
  
  GPIO_InitTypeDef GPIO_InitStructure;

  unsigned int LED_data = 0x0080;    
  
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);
  
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0| GPIO_Pin_1 | GPIO_Pin_2| GPIO_Pin_3| GPIO_Pin_4 | GPIO_Pin_5 | GPIO_Pin_6 | GPIO_Pin_7; // 출력 핀 설정
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz; // speed 설정
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; // 출력 모드 설정
  GPIO_Init(GPIOA, &GPIO_InitStructure);
  
  while (1)  {
    
    GPIO_ResetBits(GPIOA, LED_data);
    if(LED_data == 0x0080)
      LED_data = 0x0001;
     else
       LED_data<<=1;

GPIO_SetBits(GPIOA, LED_data);
    Delay(0xAFFFF);
  }
  
}


```
* 코드 설명

이 코드에서는 main() 함수 실행 전에 먼저 시스템에 필요한 헤더 파일과 Delay() 함수를 선언해줍니다. main() 함수에서는 시스템을 초기화하고 GPIO를 제어하기 위한 코드를 작성하고 GPIOA에 동작클럭을 인가했습니다.
그 후 GPIO_InitTypeDef 구조체의 GPIO_Pin 으로 사용할 핀(0~7)을 선택해준 후 GPIO_Speed 로 speed를 50MHz로 설정해주었습니다. 또 GPIO_Mode 로 출력 모드를 output mode general purpose push-pull 로 선택해주었습니다. 
그 다음으로 while() 문을 통해 실제로 LED가 끊임없이 켜지도록 하였는데, GPIO_ResetBits함수를 이용해서 포트A로 LED_data 변수가 의미하는 핀을 클리어한 후 LED_data 가 이진수로 10000000, 즉 0x0080이 되면 LED_data를 이진수로 00000001, 즉 0x0001 로 설정해주고, 그렇지 않다면 비트 연산자 << 를 이용해 LED_data의 비트를 왼쪽으로 하나씩 밀어준 후 GPIO_SetBits함수를 이용해서 포트A로 LED_data변수가 의미하는 핀을 출력하고 Delay 함수를 호출해 시간을 지연시킵니다. 

* 실행 결과

실행 결과 GPIOA 의 CRL 이 0x44444444(초기값) 에서 0x33333333 으로 바뀌는 것을 확인할 수 있었습니다.
또 GPIOA_ODR의 값이 LED_data의 값이 변함에 따라 바뀌는 모습을 확인할 수 있었습니다.
실습 키트의 모습을 확인해보면 가장 오른쪽부터 한 번에 하나씩 끊임없이 led가 켜졌다 꺼지는 모습을 볼 수 있었습니다.

## Lab 5-2

* code

``` C

#include "stm32f10x_lib.h"
#include "System_func.h"


int main(void)
{
  Init_STM32F103();
  
  GPIO_InitTypeDef GPIO_InitStructure;

  unsigned int input_data = 0; // 포트C로 입력되는 데이터를 저장하기 위한 변수     
  
RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC|RCC_APB2Periph_GPIOA, ENABLE);
  
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0| GPIO_Pin_1 | GPIO_Pin_2| GPIO_Pin_3| GPIO_Pin_4 | GPIO_Pin_5 | GPIO_Pin_6 | GPIO_Pin_7;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
  GPIO_Init(GPIOA, &GPIO_InitStructure);
  
  
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0| GPIO_Pin_1 | GPIO_Pin_2| GPIO_Pin_3| GPIO_Pin_4 | GPIO_Pin_5 | GPIO_Pin_6 | GPIO_Pin_7;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;
  GPIO_Init(GPIOC, &GPIO_InitStructure);
  
while(1) {
    input_data = GPIO_ReadInputData(GPIOC);
    GPIO_Write(GPIOA, input_data);
  }
}

```

* 코드 설명

이 코드에서는 먼저 시스템에 필요한 헤더 파일을 선언해주고, main() 함수에서 시스템을 초기화하고 포트C로 입력되는 데이터를 저장하기 위한 변수 input_data를 선언하고 GPIOC와 GPIOA에 동작클럭을 인가했습니다.
그 다음으로 실습 5-1에서와 같은 방법으로 GPIOA의 모든핀을 동작클럭을 50MHz로 해서 출력핀으로 설정해주는 코드를 작성하였습니다. 그리고 GPIOC를 입력모드로 설정해주기 위해 GPIO_InitTypeDef 구조체의 GPIO_Pin 으로 사용할 핀(0~7)을 선택해준 후 GPIO_Speed 로 speed를 50MHz로 설정해주었습니다. 또 GPIO_Mode 로 출력 모드를 input mode floating input(reset state)으로 선택해주었습니다.
그 다음으로 GPIOC로 입력받은 값을 GPIOA로 내보내주기를 반복하도록 하기 위해 while()문을 작성하였습니다. while() 안에서 미리 선언해준 변수 input_data에 에 GPIO_ReadInputData(GPIOC) 로 GPIO에서 입력받은 값을 대입해주고 GPIO_Write 함수를 이용해 GPIOA로 input_data에 대입된 값을 츨력해줍니다.


* 실행 결과

이 코드를 실행시키고 GPIOC에 연결된 스위치를 누르면 그에 해당하는 LED
에 불이 들어옵니다. 

## Lab 5-3

* code

``` C
#include "stm32f10x_lib.h"
#include "System_func.h"

void Delay(vu32 nCount)
{
  for(; nCount!=0;nCount--);  
}

int main(void)
{
  Init_STM32F103();
  
  GPIO_InitTypeDef GPIO_InitStructure;

unsigned int FND_DATA_TBL[] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x27, 0x7F, 0x6F, 0x77, 0x7C, 0x39, 0x5E, 0x79, 0x71, 0x08, 0x80};
  
  unsigned char cnt = 0, i;

RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC|RCC_APB2Periph_GPIOA, ENABLE);
  
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0| GPIO_Pin_1 | GPIO_Pin_2| GPIO_Pin_3| GPIO_Pin_4 | GPIO_Pin_5 | GPIO_Pin_6 | GPIO_Pin_7;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
  GPIO_Init(GPIOA, &GPIO_InitStructure);
  
  
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0| GPIO_Pin_1 | GPIO_Pin_2| GPIO_Pin_3| GPIO_Pin_4 | GPIO_Pin_5 | GPIO_Pin_6 | GPIO_Pin_7;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
  GPIO_Init(GPIOC, &GPIO_InitStructure);
  
  GPIO_ResetBits(GPIOA, 0x0F);
               
  while(1) {
   GPIO_ResetBits(GPIOC, 0xFF);
   GPIO_SetBits(GPIOC, FND_DATA_TBL[cnt]);

   cnt++;
   
   if(cnt == 18)
     cnt = 0;
   
   for(i=0;i<30;i++)
     Delay(0xFFFF);
  }
}

```
* 코드 설명

이 코드에서는 먼저 시스템에 필요한 헤더 파일과 Delay() 함수를 선언해줍니다. 그리고 main 에서 실습 5-1, 5-2에서와 같이 초기 설정을 해주고 FND_DATA_TBL 에 FND에 출력할 데이터 값들을 저장해줍니다. 그리고 후에 반복문에서 사용할 변수 cnt와 i를 선언해줍니다. 그리고 실습 5-1과 같은 방법으로 포트 A의 0 ~ 7번 핀을 50MHz의 general purpose output push-pull 로 설정해줍니다. 그리고 FND 네 개를 모두 출력하도록 GPIOA의 port0~3 를 0으로 설정하기 위해 GPIO_ResetBits(GPIOA, 0x0F) 를 작성하였습니다.
그 다음으로 FND 테이블에 있는 값들을 일정 딜레이마다 FND로 출력하기 위해 while 문을 사용해 코드를 작성했습니다. while문 안에서 GPIO_ResetBits 함수와 GPIO_SetBits 함수를 사용해 포트를 리셋시키고 FND_DATA의 cnt번째 인덱스에 든 값을 출력해줍니다. 그리고 cnt++; if(cnt>17) cnt=0; 를 작성하였는데, 이 코드는 while문이 반복될 때마다 FND_DATA의 값을 출력해준 후 cnt를 증가시켜주고, 만약 cnt의 값이 FND 테이블의 크기를 초과하면 cnt를 다시 0으로 초기화해주는 역할을 합니다. 그 다음으로 Delay 함수를 사용해 시간을 지연시켜줍니다.

* 실행 결과

이 코드를 실행시키면 GPIOA_Low 와 GPIOC_Low에 연결된 FND(7-segment)
에 500ms마다 7-segment 에 0000 ,1111, 2222 ,3333, 4444, 5555, 6666, 7777, 
8888, 9999, AAAA, BBBB, CCCC, DDDD, EEEE, FFFF, ____, …. 가 차례대로 출력
되기를 반복합니다.
