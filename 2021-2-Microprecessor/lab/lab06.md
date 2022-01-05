## Lab 6-1

* code

main.c
``` C

#include "stm32f10x_lib.h"
#include "System_func.h"

u8 flag = 1; 

void Delay(vu32 nCount)
{
  for(; nCount != 0; nCount--);
}

int main(void)
{
  EXTI_InitTypeDef EXTI_InitStructure; 
  NVIC_InitTypeDef NVIC_InitStructure; 
  GPIO_InitTypeDef GPIO_InitStructure; 
  
  unsigned int LED_data = 0x0080;
  
Init_STM32F103();
  
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);
  
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA | RCC_APB2Periph_GPIOC | RCC_APB2Periph_AFIO, ENABLE);
  
GPIO_InitStructure.GPIO_Pin = GPIO_Pin_All;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
  GPIO_Init(GPIOC, &GPIO_InitStructure);
  
GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0; 
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;
  GPIO_Init(GPIOA, &GPIO_InitStructure);
  
NVIC_InitStructure.NVIC_IRQChannel = EXTI0_IRQChannel;
  NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;
  NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;
  NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
  NVIC_Init(&NVIC_InitStructure);
  
GPIO_EXTILineConfig(GPIO_PortSourceGPIOA, GPIO_PinSource0); 
  
EXTI_InitStructure.EXTI_Line = EXTI_Line0; 
  EXTI_InitStructure.EXTI_Mode = EXTI_Mode_Interrupt;
  EXTI_InitStructure.EXTI_Trigger = EXTI_Trigger_Rising;
  EXTI_InitStructure.EXTI_LineCmd = ENABLE; 
  EXTI_Init(&EXTI_InitStructure); 
  
while (1)  {

    if(flag == 1) { 
      GPIO_ResetBits(GPIOC, LED_data);
      if(LED_data == 0x80)
        LED_data = 0x01;
      else
        LED_data <<= 1;
      GPIO_SetBits(GPIOC, LED_data);
      Delay(0xAFFFF);
    } // end if
  } // end while
  
} // end main

```
stm32f10x_it.c
``` C
extern u8 flag;

void EXTI0_IRQHandler(void)
{
  if(EXTI_GetITStatus(EXTI_Line0) != RESET) {
    flag = (flag!=0)?0:1;
    EXTI_ClearITPendingBit(EXTI_Line0); 
  }
}

```

* 코드 설명

이 코드에서는 main 함수 선언 전에 필요한 헤더 파일들을 선언해주고 외부 인터럽트0가 발생할 때마다 토글되어 LED 점등을 제어하기 위해 쓰일 전역변수 flag를 선언해줍니다. 그리고 Delay함수를 정의해줍니다.
main함수에서는 외부 인터럽트 소스를 설정하기 위한 data structure, 인터럽트 데이블에 대한 값을 설정하기 위한 data structure, GPIO 설정을 위한 data structure를 가져오고, LED_data를 선언해 0x0080 (이진수로 10000000) 으로 초기화해준 후 시스템을 초기화해줍니다. 그 다음으로 GPIO 포트 및 AFIO에 클럭을 인가해줍니다.
그 다음 앞에서 미리 가져왔던 GPIO 설정을 위한 data structure 인 GPIO_InitStructure를 사용해 GPIOC를 output으로 설정해주고, GPIOA를 input으로 설정해줍니다.
그 다음으로는 인터럽트 데이블에 대한 값을 설정하기 위한 data structure인 NVIC_InitStructure 를 사용하여 외부 인터럽트0의 인터럽트를 가장 높은 우선순위로 허용한 후, GPIO_EXTILineConfig 함수를 사용해 포트A의 0번핀을 외부 인터럽트 0과 연결해줍니다.
그리고 외부 인터럽트 소스를 설정하기 위한 data structure인 EXTI_InitStructure 를 사용해서 외부 인터럽트0 가 상승엣지에서 발생되도록 설정해줍니다. 
그리고 while문에서는 flag가 1이면 LED를 이동시켜 빛이 흐르도록 하는데, EXTI0_IRQHandler에서 인터럽트가 들어오면 flag 값이 변경되도록 해줍니다. (flag는 전역변수로 선언되었습니다.)
stm32f10x_it.c 에 정의된 EXTI0_IRQHandler 함수에는 외부 인터럽트가 발생하면 flag 값을 바꾸어준 후 PendingBit를 클리어해 다음에 또 인터럽트가 발생될 수 있도록 해주는 코드를 작성하였습니다.

* 실행 결과

이 코드를 실행하면 LED의 빛이 흐르다가 스위치 0번을 누르면 인터럽트가 발생하여 flag 값이 0으로 바뀌고 LED가 멈춥니다. 다시 스위치를 누르면 flag 값이 다시 1로 바뀌어 LED의 빛이 다시 흐르기 시작합니다.

## Lab 6-2

* code

main.c
``` C
#include "stm32f10x_lib.h"
#include "System_func.h"

unsigned char time_10ms = 0, time_100ms = 0, time_1s = 0, time_10s = 0;
char Time_STOP = 1;

void GPIO_Configuration(void);
void Delay(vu32 nCount);

int main(void)
{
  EXTI_InitTypeDef EXTI_InitStructure;
  NVIC_InitTypeDef NVIC_InitStructure;
  
  unsigned char FND_DATA_TBL[] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7C, 0x7F, 0x67, 0x77, 0x7C, 0x39, 0x5E, 0x79, 0x71, 0x08, 0x80};
  
  Init_STM32F103();
  
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC | RCC_APB2Periph_GPIOB | RCC_APB2Periph_GPIOA | RCC_APB2Periph_AFIO, ENABLE);
  
  NVIC_InitStructure.NVIC_IRQChannel = EXTI0_IRQChannel;
  NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;
  NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;
  NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
  NVIC_Init(&NVIC_InitStructure);
  
  NVIC_InitStructure.NVIC_IRQChannel = EXTI1_IRQChannel;
  NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 1;
  NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
  NVIC_Init(&NVIC_InitStructure);
  
GPIO_Configuration();
  
  GPIO_EXTILineConfig(GPIO_PortSourceGPIOA, GPIO_PinSource0);
  EXTI_InitStructure.EXTI_Line = EXTI_Line0;
  EXTI_InitStructure.EXTI_Mode = EXTI_Mode_Interrupt;
  EXTI_InitStructure.EXTI_Trigger = EXTI_Trigger_Rising;
  EXTI_Init(&EXTI_InitStructure);
 
  GPIO_EXTILineConfig(GPIO_PortSourceGPIOA, GPIO_PinSource1);
  EXTI_InitStructure.EXTI_Line = EXTI_Line1;
  EXTI_InitStructure.EXTI_Mode = EXTI_Mode_Interrupt;
  EXTI_InitStructure.EXTI_Trigger = EXTI_Trigger_Rising;
  EXTI_Init(&EXTI_InitStructure);
  
  while (1)  { 
    GPIO_SetBits(GPIOB, GPIO_Pin_0 |  GPIO_Pin_1 |  GPIO_Pin_2 |  GPIO_Pin_3); 
    GPIO_ResetBits(GPIOB, GPIO_Pin_3); 
    
    GPIO_ResetBits(GPIOC, 0x00FF); 
    GPIO_SetBits(GPIOC, FND_DATA_TBL[time_10ms]); 
    Delay(0x1FFF); 
    
    GPIO_SetBits(GPIOB, GPIO_Pin_0 |  GPIO_Pin_1 |  GPIO_Pin_2 |  GPIO_Pin_3);
    GPIO_ResetBits(GPIOB, GPIO_Pin_2); 
    
    GPIO_ResetBits(GPIOC, 0x00FF); 
    GPIO_SetBits(GPIOC, FND_DATA_TBL[time_100ms]); 
    Delay(0x1FFF);
    
    GPIO_SetBits(GPIOB, GPIO_Pin_0 | GPIO_Pin_1 | GPIO_Pin_2 | GPIO_Pin_3);
    GPIO_ResetBits(GPIOB, GPIO_Pin_1); 
    
    GPIO_ResetBits(GPIOC, 0x00FF); 
    GPIO_SetBits(GPIOC, FND_DATA_TBL[time_1s]|0x80); 
    Delay(0x1FFF);
    
    GPIO_SetBits(GPIOB, GPIO_Pin_0 | GPIO_Pin_1 | GPIO_Pin_2 | GPIO_Pin_3);
    GPIO_ResetBits(GPIOB, GPIO_Pin_0); 
    
    GPIO_ResetBits(GPIOC, 0x00FF); 
    GPIO_SetBits(GPIOC, FND_DATA_TBL[time_10s]); 
    Delay(0x1FFF);
    
    if(Time_STOP == 0) continue; 
    
time_10ms++;
    
    if (time_10ms == 10) {
      time_10ms = 0;
      time_100ms++;
    }
    
    if (time_100ms == 10) {
      time_100ms = 0;
      time_1s++;
    }
    
    if (time_1s == 10) {
      time_1s = 0;
      time_10s++;
    }
    
    if (time_10s == 10) {
      time_10s = 0;
    }
  } // end while
  
} // end main

void GPIO_Configuration(void)
{
  GPIO_InitTypeDef GPIO_InitStructure; 
  
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0 | GPIO_Pin_1;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;
  GPIO_Init(GPIOA, &GPIO_InitStructure);
  
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0 | GPIO_Pin_1 | GPIO_Pin_2 | GPIO_Pin_3;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
  GPIO_Init(GPIOB, &GPIO_InitStructure);
 
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0 | GPIO_Pin_1 | GPIO_Pin_2 | GPIO_Pin_3 | GPIO_Pin_4 | GPIO_Pin_5 | GPIO_Pin_6 | GPIO_Pin_7;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
  GPIO_Init(GPIOC, &GPIO_InitStructure);
  
}


void Delay(vu32 nCount)
{
  for(; nCount != 0; nCount--);
}

```
stm32f10x_it.c
``` C
extern unsigned char time_10ms, time_100ms, time_1s, time_10s;
extern char Time_STOP;


void EXTI0_IRQHandler(void)
{
  if (EXTI_GetITStatus(EXTI_Line0) != RESET)
  {
    if (Time_STOP == 0) {
      Time_STOP = 1;
    }
    else {
      Time_STOP = 0;
    }
    EXTI_ClearITPendingBit(EXTI_Line0);
  }
}

void EXTI1_IRQHandler(void)
{
  if(EXTI_GetITStatus(EXTI_Line1) != RESET)
  {
    if (Time_STOP == 0) {
      time_10ms = 0;
      time_100ms = 0;
      time_1s = 0;
      time_10s = 0;
    }
    EXTI_ClearITPendingBit(EXTI_Line1); 
  }
}


```
* 코드 설명

이 코드에서는 먼저 프로그램에 필요한 헤더선언을 해주고 시간값을 저장하기 위한 time_10ms, time_100ms, time_1s, time_10s 와 스톱워치 동작플래그로 쓰일 Time_STOP을 전역변수로 선언해줍니다. 그리고 GPIO 설정을 할 GPIO_Configuration 함수와 시간을 지연시켜줄 Delay 함수를 선언해줍니다.
main함수에서는 외부 인터럽트 소스를 설정하기 위한 data structure, 인터럽트 데이블에 대한 값을 설정하기 위한 data structure를 가져오고 FND_DATA_TBL 에 FND에 출력할 데이터 값들을 차례대로 저장해줍니다. 그 다음 시스템을 초기화해주는 코드를 작성하고, RCC_APB2PeriphClockCmd 함수를 사용해 포트 A, B, C 및 AFIO 클럭을 설정해줍니다.
그 다음으로는 외부 인터럽트 소스를 설정하기 위한 data structure인 NVIC_InitStructure 를 사용하여 인터럽트를 enable시키고 우선순위를 설정해준 후, GPIO_Configuration 함수를 호출하여 GPIO를 설정해줍니다.
GPIO_Configuration 함수에서는 포트 A의 0번 핀과 1번 핀을 입력으로 설정해주고 포트 B와 C는 출력으로 설정해주는데, GPIOB는 0번~3번 핀에 대해 출력으로 설정해주고 GPIOC는 0번~8번 핀에 대해 출력으로 설정해줍니다. GPIOB는 숫자를 표시할 위치가 네 군데중 어디인지를 확인하는 역할을 하지만 GPIOC는 그리고 싶은 숫자에 맞게 led를 켜주는 역할을 해주어 8개의 핀이 필요하기 때문입니다.
그 다음으로 외부 인터럽트 0, 1 이 포트A로 상승엣지에서 발생되도록 설정해주기 위해 인터럽트 데이블에 대한 값을 설정하기 위한 data structure인 EXTI_InitStructure 를 사용합니다. 이때 Line0을 위한 설정과 Line1를 위한 설정을 따로따로 해줍니다.
while 문은 수동적으로 계속 GPIO에 네 자리 수를 내보내주기 위해 사용됩니다. GPIO_SetBits 함수, GPIO_ResetBits 함수를 활용해 GPIOB 에 내보내줄 위치를 선택하고 GPIO_ResetBits 함수와 GPIO_SetBits 함수를 다시 사용해 미리 선언해준 time_10ms 등의 변수를 인덱스로 가지는 FND_DATA_TBL 의 값을 GPIOC에 내보내주고 Delay 함수를 호출해 시간을 지연시켜주는 과정을 C0, C1, C2, C3 모두에 적용되도록 반복해줍니다.
그 다음으로는 line0에 interrupt가 발생하면 바뀌도록 EXTI0_IRQHandler 에서 설정한 Time_STOP 이 0이면 계속 진행해 시간을 증가시키도록 하는 코드를 작성하였습니다.
이때 time_10ms를 증가시켜주고 time_10ms 가 10이면 time_10ms를 0으로 초기화해주고 더 높은 자릿수의 값을 의미하는 time_100ms의 값을 증가시켜줍니다. 그리고 time_100ms가 10이면 time_100ms를 초기화해주고 더 높은 자릿수의 값인 time_1s를 증가시켜줍니다. 그리고 time_1s가 10이면 time_1s를 초기화해주고 더 높은 자릿수의 값인 time_10s를 증가시켜주어 시간을 증가시켜줍니다.
stm32f10x_it.c 에서 외부 인터럽트에 대한 처리를 설정해주는데, EXTI0_IRQHandler 에서는 line0에 대한 처리를, EXTI1_IRQHandler에서는 line1에 대한 처리를 해줍니다. 이 함수들에서 사용할, 이미 main.c에 선언한 전역변수들을 이곳에서도 사용하는데, EXTI0_IRQHandler 에서는 line0가 Pending되었는지 확인한 후 line0에 외부 인터럽트가 발생할 때마다 Time_STOP의 값을 바꾸어주고 다음 interrupt를 위해 EXTI_ClearITPendingBit 함수를 이용해 클리어해주는 코드를 작성하였고, EXTI1_IRQHandler에서는 ㅣline1이 Pending되어있는지 확인한 후line1에 외부 인터럽트가 발생했을 때 Time_STOP 이 0이면 (= 스톱워치가 멈춰 있으면) time_10ms, time_100ms, time_1s, time_10s 를 모두 0으로 초기화해주어 스톱워치의 값을 0으로 되돌리도록 하고 다음 interrupt를 위해 클리어해주는 코드를 작성하였습니다.

* 실행 결과

이 코드를 실행하면 스톱워치의 시간이 증가하다가 0번 스위치를 누르면 멈
춥니다. 그리고 다시 0번 스위치를 누르면 이어서 시간이 증가됩니다. 시간이 
증가될 때 1번 스위치를 누르면 아무 일도 일어나지 않고, 시간이 멈춰있을 
때 1번 스위치를 누르면 시간이 초기화되어 00.0이 표시됩니다.

