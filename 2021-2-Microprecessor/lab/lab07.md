## Lab 7-1

* code

main.c
``` C
#include "stm32f10x_lib.h"
#include "System_func.h"

int main(void)
{
  GPIO_InitTypeDef GPIO_InitStructure;
  TIM_TimeBaseInitTypeDef TIM2_TimeBaseInitStruct; 
  
  unsigned int LED_data = 0x0080;
  
  Init_STM32F103();
  
RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE); 
  
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0|GPIO_Pin_1|GPIO_Pin_2|GPIO_Pin_3|GPIO_Pin_4|GPIO_Pin_5|GPIO_Pin_6|GPIO_Pin_7;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
  GPIO_Init(GPIOA, &GPIO_InitStructure); 
  
  RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM2, ENABLE);
  
  TIM2_TimeBaseInitStruct.TIM_Prescaler = 7200-1; 
  TIM2_TimeBaseInitStruct.TIM_CounterMode = TIM_CounterMode_Up; 
  TIM2_TimeBaseInitStruct.TIM_Period = 5000-1;
  TIM2_TimeBaseInitStruct.TIM_ClockDivision = TIM_CKD_DIV1;
  TIM_TimeBaseInit(TIM2,&TIM2_TimeBaseInitStruct); 
  
TIM_Cmd(TIM2, ENABLE); 
  
  while (1) {
    GPIO_ResetBits(GPIOA, LED_data);
    if(LED_data == 0x80)
      LED_data = 0x01;
    else
      LED_data <<= 1;
    
    GPIO_SetBits(GPIOA, LED_data);
    
    while(TIM_GetFlagStatus(TIM2,TIM_IT_Update)==RESET) {} 
    TIM_ClearFlag(TIM2, TIM_FLAG_Update); 
  } // end while
  
} // end main

```
* 코드 설명

이 코드에서는 main함수를 쓰기 전에 먼저 프로그램에 필요한 헤더파일을 선언합니다. 그리고 main함수에서 GPIO 포트를 설정해주기 위한 구조체와 타이머 값을 설정할 수 있는 구조체 GPIO_InitStructure와 TIM2_TimeBaseInitStruct와 LED에 내보낼 값을 저장할 변수 LED_data 를 선언해준 뒤 시스템을 초기화합니다.
RCC_APB2PeriphClockCmd()를 사용해 LED로 출력을 발생할 GPIO 포트A의 클럭 및 출력핀을 설정한 다음, GPIO_InitStructure를 사용해 GPIOA의 0번~7번 포트를 50MHz의 output으로 설정해줍니다. 그리고 GPIO_Init() 함수를 사용해 GPIOA를 초기화해줍니다.
RCC_APB1PeriphClockCmd()를 통해 타이머2의 클럭, 주기 등을 인가한 다음 TIM2_TimeBaseInitStruct를 사용해 타이머를 업카운트 방향, 72MHz로 설정해줍니다. 그리고 프리스케일러는 7200-1, 주기값(=ARR)은 5000-1로 설정해주는데, 이렇게 설정하면 타이머는 7200 * 5000 / 72 *10^6 = 0.5초가 지나면 expire하게 됩니다. TIM_TimeBaseInit() 함수를 통해 타이머를 초기화해주고 TIM_Cmd() 함수를 사용해 타이머를 동작시킵니다.
그 다음으로 while문을 사용해 LED_data 의 값이 0x80 (이진수로 10000000) 이면 0x01로 바꾸어주고, 그렇제 않으면 LED_data의 비트를 하나씩 왼쪽으로 이동시켜준 후 GPIOA에 LED_data에 저장된 값을 출력시켜 LED에 빛이 하나씩 들어오도록 하였습니다. 그리고 while문과 TIM_GetFlagStatus() 함수를 사용해 타이머가 expire될 때까지 0.5초간 대기시킨 후에 TIM_ClearFlag 함수를 사용해 타이머를 다시 동작시킬 수 있도록 해줍니다. 
위 코드에서 타이머의 주기값(=ARR) 설정을 5000-1이 아니라 20000-1로 바꾸어주면 7200 * 20000 / 72 * 10^6 = 2초 지나고 expire하는 타이머로 설정되어 2초마다 LED가 점멸하는 코드고 바뀌게 됩니다.

* 실행 결과

0.5초마다 LED가 점멸하여 1초가 지나면 LED가 두 칸 옮겨간 모습을 확인할 수 
있습니다.


## Lab 7-2

* code

main.c
``` C
#include "stm32f10x_lib.h"
#include "System_func.h"

unsigned char time_10m = 0, time_1m = 0, time_10s = 0, time_1s = 0;

void Delay(vu32 nCount);

int main(void)
{
  GPIO_InitTypeDef GPIO_InitStructure;
  TIM_TimeBaseInitTypeDef TIM2_TimeBaseInitStruct; 
  NVIC_InitTypeDef NVIC_InitStructure; 

  unsigned char FND_DATA_TBL[] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7C, 0x07, 0x7F, 0x67, 0x77, 0x7C, 0x39, 0x5E, 0x79, 0x71, 0x08, 0x80};
  
  u16 FND_Pin = GPIO_Pin_0 |GPIO_Pin_1 |GPIO_Pin_2| GPIO_Pin_3 |GPIO_Pin_4 |GPIO_Pin_5 |GPIO_Pin_6 |GPIO_Pin_7;
  
  u16 FND_COM_pin = GPIO_Pin_0 |GPIO_Pin_1 |GPIO_Pin_2 |GPIO_Pin_3;
  
  Init_STM32F103();
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC|RCC_APB2Periph_GPIOA, ENABLE); 
  
  
  GPIO_InitStructure.GPIO_Pin = FND_Pin;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
  GPIO_Init(GPIOA, &GPIO_InitStructure); 
  
  
  GPIO_InitStructure.GPIO_Pin = FND_COM_pin;
  GPIO_Init(GPIOC, &GPIO_InitStructure);
  
 
  NVIC_InitStructure.NVIC_IRQChannel = TIM2_IRQChannel;
  NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0; 
  NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0; 
  NVIC_Init(&NVIC_InitStructure); 
  
  RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM2, ENABLE);
  
  TIM2_TimeBaseInitStruct.TIM_Prescaler = 7200-1; 
  TIM2_TimeBaseInitStruct.TIM_CounterMode = TIM_CounterMode_Up; 
  TIM2_TimeBaseInitStruct.TIM_Period = 20000-1; 
  TIM2_TimeBaseInitStruct.TIM_ClockDivision = TIM_CKD_DIV1; 
  TIM_TimeBaseInit(TIM2,&TIM2_TimeBaseInitStruct); 
  
  TIM_ITConfig(TIM2, TIM_IT_Update, ENABLE); 
  TIM_Cmd(TIM2, ENABLE); 
  
  while (1) {
    GPIO_SetBits(GPIOC, FND_COM_pin); 
    GPIO_ResetBits(GPIOC, GPIO_Pin_3); 
    
    GPIO_ResetBits(GPIOA, FND_Pin); 
    GPIO_SetBits(GPIOA, FND_DATA_TBL[time_1s]);  
    Delay(0x1FFF);
    
    GPIO_SetBits(GPIOC, FND_COM_pin);
    GPIO_ResetBits(GPIOC, GPIO_Pin_2);
    
    GPIO_ResetBits(GPIOA, FND_Pin);
    GPIO_SetBits(GPIOA, FND_DATA_TBL[time_10s]); 
    Delay(0x1FFF);
    
    GPIO_SetBits(GPIOC, FND_COM_pin);
    GPIO_ResetBits(GPIOC, GPIO_Pin_1);
    
    GPIO_ResetBits(GPIOA, FND_Pin);
    GPIO_SetBits(GPIOA, FND_DATA_TBL[time_1m]|0x80); 
    Delay(0x1FFF);
    
    GPIO_SetBits(GPIOC, FND_COM_pin);
    GPIO_ResetBits(GPIOC, GPIO_Pin_0);
    
    GPIO_ResetBits(GPIOA, FND_Pin);
    GPIO_SetBits(GPIOA, FND_DATA_TBL[time_10m]);
    Delay(0x1FFF);    
    
  } // end while
  
} // end main

void Delay(vu32 nCount)
{
  for(; nCount != 0; nCount--);;
}

```
stm32f10x_it.c 
``` C
extern unsigned char time_10m, time_1m, time_10s, time_1s; 

void TIM2_IRQHandler(void)
{
  if (TIM_GetFlagStatus(TIM2, TIM_IT_Update) == SET) {
    TIM_ClearITPendingBit(TIM2, TIM_FLAG_Update); 
    time_1s += 2; 
    if(time_1s == 10) {
      time_10s++;
      time_1s = 0;
    }
    if (time_10s == 6) {
      time_1m++;
      time_10s = 0;
    }
    if (time_1m == 10) {
      time_10m++;
      time_1m = 0;
    }
    if (time_10m == 6) {
      time_10m = 0;
    }
  }
}

```

* 코드 설명

main.c 파일에서는 먼저 프로그램에 필요한 헤더파일과, 시간값을 저장할 전역 변수와 Delay 함수를 를 선언해줍니다. 그리고 main 함수에서 GPIO, 타이머 값, NVIC 설정을 위한 구조체 GPIO_InitStructure, TIM2_TimeBaseInitStruct, NVIC_InitStructure 를 선언한 후 FND에 출력할 값을 저장한 배열 FND_DATA_TBL을 선언해줍니다.
그리고 FND_Pin에 0번부터 7번까지의 GPIO 핀을 저장해주고, FND_COM_pin에는 0번부터 3번까지의 GPIO 핀을 저장해주어 나중에 7-Segment로 값을 내보낼 때 사용할 수 있도록 한 후 Init_STM32F103() 함수를 사용해 시스템을 초기화해줍니다.
RCC_APB2PeriphClockCmd 함수와 GPIO_InitStructure 구조체, GPIO_Init 함수를 사용해 GPIOA의 0번~7번 핀과 GPIOC의 0번~3번 핀을 50MHz output으로 설정해줍니다. 그 다음으로 NVIC_InitStructure 를 사용해 인터럽트 발생 시 TIM2_IRQChannel로 분기하도록 설정해줍니다. 그리고 RCC_APB1PeriphClockCmd 함수와 TIM2_TimeBaseInitStruct 구조체, TIM_BaseInit 함수를 사용해 타이머의 프리스케일을 7200-1로, 주기값을 20000-1로 설정해주어 7200 * 20000 / 72 * 10^6 = 2초 후에 expire되도록 타이머를 설정해줍니다. 그리고 TIM_ITConfig 함수와 TIM_Cmd 함수를 하용해 인터럽트와 타이머를 enable하게 만들어줍니다.
그 다음으로는 while문을 사용해 타이머가 expire되기 전까지 7-Segment에 타이머의 현재 시각을 그대로 출력시켜줄 코드를 작성하였습니다. while문 안에서 GPIOC로는 어느 위치에 숫자를 나타낼지를 선택하고 GPIOA로는 0 ~ 9 까지의 숫자 중 어느 숫자를 7-Segment의 그 위치로 내보낼지를 선택하고 Delay 함수를 이용해 시간을 지연시키기를 반복하여 시간을 출력하도록 하였습니다.
이때 미리 선언한 time_1s 등의 전역변수를 사용해 내보낼 값을 알아내는데, 이 값은 stm32f10x_it.c 파일의 TIM2_IRQHandler 함수를 통해 타이머가 expire해 인터럽트가 발생할 때마다 time_1s의 값을 2씩 증가시켜주고 시간이 다 차면 0으로 초기화해준 후 그보다 더 높은 자리의 시간 값을 증가시켜주어 2초마다 시간이 2초씩 늘어날 수 있게 하였습니다.
위 코드에서 main.c 파일의 타이머의 주기값(=ARR) 설정을 20000-1이 아닌 40000-1로 설정해주면 7200 * 40000 / 72 * 10^6 = 4초 지나고 expire되도록 설정됩니다. 그리고 stm32f10x_it.c 에서도 time_1s를 4씩 증가시켜주도록 수정합니다. 그리고 time_1s 가 8 에서 12로 바뀌는 등 자릿수가 바뀐 후에 time_1s의 값이 0이 아닌 경우를 고려하여 시간이 최대치를 넘으면 최대치만큼을 빼준 후 더 높은 자리의 시간 값을 증가시키도록 코드를 수정하여, 4초마다 시간이 4초씩 늘어나도록 코드를 작성하였습니다.

* 실행 결과

     
스톱워치의 시간과 비교해보면, 7-세그먼트에서 2초 단위로 건너뛰며 시간을 출력
하는 모습을 확인할 수 있습니다.

