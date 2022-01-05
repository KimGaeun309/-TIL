## Lab 8-1

* code

``` C
#include "stm32f10x_lib.h"
#include "System_func.h"

void Delay(vu32 nCount);

int main(void)
{
  GPIO_InitTypeDef GPIO_InitStructure;  
  TIM_TimeBaseInitTypeDef TIM_TimeBaseStructure; 
  TIM_OCInitTypeDef TIM_OCInitStructure; 
  
  Init_STM32F103();
  
  u16 CCR1_Val = 10; 
 
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_6; 
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_Init(GPIOA, &GPIO_InitStructure); 
  
  RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM3, ENABLE);
  TIM_TimeBaseStructure.TIM_Period = 999;
  TIM_TimeBaseStructure.TIM_Prescaler = 0;
  TIM_TimeBaseStructure.TIM_ClockDivision = TIM_CKD_DIV1;
  TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;
  TIM_TimeBaseInit(TIM3, &TIM_TimeBaseStructure); 
  
  
  TIM_OCInitStructure.TIM_OCMode = TIM_OCMode_PWM1; 
  TIM_OCInitStructure.TIM_Channel = TIM_Channel_1; 
  TIM_OCInitStructure.TIM_Pulse = CCR1_Val; 
  TIM_OCInitStructure.TIM_OCPolarity = TIM_OCPolarity_High; 
  TIM_OCInit(TIM3, &TIM_OCInitStructure);
 
  TIM_OC1PreloadConfig(TIM3, TIM_OCPreload_Enable); 
  TIM_ARRPreloadConfig(TIM3, ENABLE);
  
  TIM_Cmd(TIM3, ENABLE);
  
  while (1) {
    
    CCR1_Val += 5;
    if(CCR1_Val >= 999) {
      CCR1_Val = 0;
    }
    TIM_Cmd(TIM3, DISABLE); 
    TIM_SetCompare1(TIM3, CCR1_Val); 
    TIM_Cmd(TIM3, ENABLE);
    
    Delay(0xafff);
  } // end while
  
} // end main

void Delay(vu32 nCount)
{
  for(; nCount != 0; nCount--);;
}

```
* 코드 설명
 
이 코드는 PWM으로 LED의 밝기를 조절하는 실습 코드입니다. 
이 코드에서는 main() 함수 전에 프로그램에 필요한 헤더파일을 선언하고, 시간을 지연시키는데에 사용할 Delay 함수를 선언해줍니다. 
main() 함수에서는 GPIO 포트를 설정할 때 사용할 구조체 GPIO_InitStructure와 타이머 주기 설정에 사용할 TIM_TimeBaseStructure 와 PWM 신호의 펄스 폭 설정에 사용할 TIM_OCInitStructure 구조체를 가져온 후, 시스템을 초기화하고 TIMx_CCR1 레지스터에 대입할 값을 저장하는 변수 CCR1_Val을 설정해주고 10으로 초기화해줍니다. 이 변수는 CCR 값을 위한 변수입니다.
그 다음으로 GPIOA의 클럭을 인가해준 후 GPIO_InitStructure를 이용해 포트A의 6번 핀을 AFIO 모드로 설정해주고 GPIOA를 초기화줍니다. 또  타이머3의 클럭을 인가해준 후 TIM_TimeBaseStructure를 이용해 타이머 주기를 999 로 설정해주고 타이머3을 초기화해줍니다. 또 TIM_OCInitStructure를 이용해 PWM을 설정해주는데, PWM1모드에 Channel 1을 사용하고 펄스 폭으로 미리 선언한 CCR1_Val 값을 가지며 Polarity high 가 되도록 설정해준 뒤 초기화해줍니다.
그 다음으로 TIM_OC1PreloadConfig() 함수와 TIM_ARRPreloadConfig() 함수를 사용해 TIMx_CCR1 과 TIMx_ARR 레지스터를 enable해준 뒤 TIM_Cmd() 함수를 사용해 타이머3을 동작시킵니다. 
그리고 while문을 사용해 일정 딜레이마다 CCR1_Val 변수 값을 증가시키면서 CCR 레지스터에 대입해 일정 딜레이마다 펄스 폭이 증가되도록 코드를 작성하였습니다. while 문 안에서 CCR1_Val 변수의 값을 5 증가시켜주고, 만약 타이머 주기인 999 보다 CCR1_Val 의 값이 더 크다면 CCR1_Val의 값을 0으로 바꾸어줍니다. 그 다음으로 매 주기마다 밝기를 증가시켜야 하므로 타이머3을 disable해준 뒤 증가된 CCR값을 넣어 다시 enable 해주고, Delay 함수로 시간을 지연시켜줍니다.

* 실행 결과

실행 결과 6번째 LED의 불빛이 점점 밝아졌다가 꺼지고 다시 불빛이 밝아지기를 
반복하는 것을 확인할 수 있다. 

## Lab 8-2

* code

``` C
#include "stm32f10x_lib.h"
#include "System_func.h"

TIM_TimeBaseInitTypeDef TIM_TimeBaseStructure;
TIM_OCInitTypeDef TIM_OCInitStructure;
GPIO_InitTypeDef GPIO_InitStructure;

unsigned int key2DoReMi(unsigned int key);
void Change_FREQ(unsigned int freq);
void STOP_FREQ();

int main(void)
{
  Init_STM32F103();

  u16 key_value = 0; 
  u16 freq_value = 0; 
  
  RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM3, ENABLE);
  
RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA|RCC_APB2Periph_GPIOC, ENABLE); 
  
  GPIO_InitStructure.GPIO_Pin = 0x00ff; 
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;
  GPIO_Init(GPIOC, &GPIO_InitStructure); 
  
TIM_TimeBaseInit(TIM3, &TIM_TimeBaseStructure);
  
  TIM_TimeBaseStructure.TIM_Period = 0;
  TIM_TimeBaseStructure.TIM_Prescaler = 360-1;
  TIM_TimeBaseStructure.TIM_ClockDivision = TIM_CKD_DIV1;
  TIM_TimeBaseInit(TIM3, &TIM_TimeBaseStructure);
  
  TIM_OCInitStructure.TIM_OCMode = TIM_OCMode_PWM1;
  TIM_OCInitStructure.TIM_Channel = TIM_Channel_1;
  TIM_OCInitStructure.TIM_Pulse = 0;
  TIM_OCInitStructure.TIM_OCPolarity = TIM_OCPolarity_High;
  TIM_OCInit(TIM3, &TIM_OCInitStructure);
  
TIM_OC1PreloadConfig(TIM3, TIM_OCPreload_Enable);
  TIM_ARRPreloadConfig(TIM3, ENABLE);
  
  while (1) {
    STOP_FREQ();
    while(!GPIO_ReadInputDataBit(GPIOC, 0x00ff)); 
    key_value = GPIO_ReadInputData(GPIOC)&0x00ff; 
    freq_value = key2DoReMi(key_value); 
    Change_FREQ(freq_value); 
    while(GPIO_ReadInputDataBit(GPIOC, 0x00ff));
    
  } // end while
  
} // end main

void STOP_FREQ() { 
  TIM_Cmd(TIM3, DISABLE); 
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_6; 
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_Init(GPIOA, &GPIO_InitStructure);
}

void Change_FREQ(unsigned int freq) { 
  u16 tmp = (unsigned int)(100000/freq); 
  
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_6;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP; 
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_Init(GPIOA, &GPIO_InitStructure);
  
  TIM_Cmd(TIM3, DISABLE);
  TIM_OC1PreloadConfig(TIM3, TIM_OCPreload_Disable); 
  TIM_ARRPreloadConfig(TIM3, DISABLE);
  
  TIM_SetAutoreload(TIM3, tmp); 
  TIM_SetCompare1(TIM3, (unsigned int)(tmp/2)); 
  
  TIM_OC1PreloadConfig(TIM3, TIM_OCPreload_Enable); 
  TIM_ARRPreloadConfig(TIM3, ENABLE);
  TIM_Cmd(TIM3, ENABLE);
}

unsigned int key2DoReMi(unsigned int key) { 
  unsigned int ret = 0; 
  
  switch(key) {
  case 0x01: 
    ret = 523;
    break;
  case 0x02:
    ret = 587;
    break;
  case 0x04:
    ret = 659;
    break;
  case 0x08: 
    ret = 698;
    break;
  case 0x10: 
    ret = 783;
    break;
  case 0x20: 
    ret = 880;
    break;
  case 0x40: 
    ret = 987;
    break;
  case 0x80: 
    ret = 1046;
    break;
  }
  return ret;
}

```
* 코드 설명

이 코드는 PWM 신호를 제어해 버저에 들어가는 주파수 신호를 제어해 음계를 만드는 실습 코드입니다. 
이 코드에서는 main() 함수 실행 전에 먼저 프로그램에 필요한 헤더파일을 선언한 후, 타이머 주기 설정에 사용할 TIM_TimeBaseStructure 와 PWM 신호의 펄스 폭 설정에 사용할 TIM_OCInitStructure 구조체와 GPIO 포트를 설정할 때 사용할 구조체 GPIO_InitStructure를 가져옵니다. 그리고 사용할 함수들을 선언합니다. 구조체들을 main() 함수 뿐만 아니라 이 함수들에서도 사용할 수 있기 때문에 전역으로 선언해주었습니다.
main() 함수에서는 시스템을 초기화해준 후 입력되는 키 값을 저장할 변수 key_value와 각 키에 대한 주파수값을 저장할 변수 freq_value 를 선언한 후 타이머3과 GPIOA, GPIOC의 클럭을 인가해줍니다.
그 다음으로 GPIO_InitStructure를 사용해 GPIOC의 0번~7번 핀에 대해 input 모드로 설정해주고 GPIOC를 초기화해줍니다. 그리고 TimeBaseStructure를 사용해 타이머3의 prescaler를 360-1로 설정해줍니다. 또 TIM_OCInitStructure를 사용해 타이머3을 PWM1, Channel 1, Polarity high 로 사용하도록 설정하고, 펄스 폭은 0으로 설정해줍니다. 그리고 TIMx_CCR1, TIMx_ARR 레지스터를 enable시켜줍니다.
그 다음으로 while 문을 작성해 스위치로 값을 입력받아 그에 따른 주파수를 버저로 내보내 원하는 음계를 낼 수 있도록 하였습니다. 
while 문 안에서 먼저 STOP_FREQ() 함수를 호출합니다. STOP_FREQ() 함수는 GPIOA에 대해 disable 해주고, GPIOA의 pin 6 을 OUT_PP 로 설정해주고 GPIOA를 초기화해주어 잡음을 제거하는 동작을 합니다.
그 다음으로 while(!GPIO_ReadInputDataBit(GPIOC, 0x00ff)); 코드를 사용해 GPIOC, 즉 스위치로부터 값이 입력될 때까지 기다립니다. 값이 입력되면 그 다음문장이 실행되어 눌려진 값에 0x00ff 를 & 연산한 값이 key_value 에 저장됩니다. 그리고 key2DoReMi() 함수를 사용해 freq_value 값을 구합니다. key2DoReMi() 함수는 매개변수로 받은 값에 맞는 주파수를 내보냅니다. key 가 0x01이면 낮은 도에 맞는 주파수를, 0x04이면 미에 맞는 주파수를, … 0x80이면 높은 도에 맞는 주파수를 리턴해줍니다. 리턴받은 값이 freq_value에 저장되면 Change_FREQ() 함수를 사용해 주파수(frequency)에 맞게 CCR의 값을 변화시켜 버저로 내보냅니다. Change_FREQ() 함수에서는 freq 값을 넘겨받아 CCR 값을 생성하는데, 변수 tmp에 100000/freq 의 값을 저장하고, GPIOA에 대해 다시 AF 모드로 설정해 초기화해준 다음, ARR과 CCR의 Preload값을 모두 초기화해주기 위해 먼저 disable시켜줍니다. 그리고 TIM_SetAutoreload() 함수를 사용해 tmp 값을 ARR로 설정해주고,  TIM_SetCompare1() 함수를 사용해 tmp/2 값을 CRR로 설정해줍니다. 그리고 ARR과 CCR의 Preload 값을 다시 enable시켜주고 동작시킵니다. Change_FREQ() 함수의 동작이 끝나면 다시 main() 으로 돌아와 while(GPIO_ReadInputDataBit(GPIOC, 0x00ff)); 코드를 실행시킵니다. 이 코드는 GPIOC의 값을 입력받는 만큼 시간을 지연시키기 위한 코드입니다.

* 실행 결과

 [드라이브 링크](https://drive.google.com/file/d/17V_kbkmyaANw8P4wECg8Tdad0gVdHwwY/view?usp=drivesdk)
 
