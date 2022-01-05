## Lab 10

* code

lcd.h
``` C
#define LCD_CTRL_PORT_CLK   RCC_APB2Periph_GPIOC  
#define LCD_CTRL_PORT       GPIOC
#define LCD_CTRL_RS         GPIO_Pin_0
#define LCD_CTRL_RW         GPIO_Pin_1
#define LCD_CTRL_E          GPIO_Pin_2

#define LCD_DATA      GPIOA
#define LCD_DATA_CLK  RCC_APB2Periph_GPIOA

#define LCD_LINES               2   
#define LCD_LINE_LENGTH         16  

#define LCD_LINE0_DDRAMADDR     0x00 
#define LCD_LINE1_DDRAMADDR     0x40 
#define LCD_LINE2_DDRAMADDR     0x14 
#define LCD_LINE3_DDRAMADDR     0x54

#define LCD_DELAY   asm("nop\n nop\n nop\n nop\n nop\n nop\n nop\n nop\n nop\n nop\n nop\n nop\n"); 

#define LCD_CLR             0 
#define LCD_HOME            1 
#define LCD_ENTRY_MODE      2 
#define LCD_ENTRY_INC       1 
#define LCD_ENTRY_SHIFT     0 

#define LCD_ON_CTRL         3 
#define LCD_ON_DISPLAY      2 
#define LCD_ON_CURSOR       1 
#define LCD_ON_BLINK        0 

#define LCD_MOVE            4 
#define LCD_MOVE_DISP       3 
#define LCD_MOVE_RIGHT      2 

#define LCD_FUNCTION        5 
#define LCD_FUNCTION_8BIT   4 
#define LCD_FUNCTION_2LINES 3 
#define LCD_FUNCTION_10DOTS 2 

#define LCD_CGRAM           6 
#define LCD_DDRAM           7 

#define LCD_BUSY            7 

#define LCD_FDEF_1         (1<<LCD_FUNCTION_8BIT)
#define LCD_FDEF_2             (1<<LCD_FUNCTION_2LINES)
#define LCD_FUNCTION_DEFAULT   ((1<<LCD_FUNCTION) | LCD_FDEF_1 | LCD_FDEF_2) 
#define LCD_MODE_DEFAULT       ((1<<LCD_ENTRY_MODE) | (1<<LCD_ENTRY_INC))

GPIO_InitTypeDef GPIO_LCD; 

```
main.c
``` C
#include "stm32f10x_lib.h"
#include "System_func.h"
#include "lcd.h"


void lcdInitHW(void) 
{
  // GPIOC 설정 - output모드로.
  RCC_APB2PeriphClockCmd(LCD_CTRL_PORT_CLK, ENABLE);
  GPIO_LCD.GPIO_Pin = LCD_CTRL_RS | LCD_CTRL_RW | LCD_CTRL_E;
  GPIO_LCD.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_LCD.GPIO_Mode = GPIO_Mode_Out_PP;
  GPIO_Init(LCD_CTRL_PORT, &GPIO_LCD);
  GPIO_ResetBits(LCD_CTRL_PORT, LCD_CTRL_RS | LCD_CTRL_RW | LCD_CTRL_E);

  RCC_APB2PeriphClockCmd(LCD_DATA_CLK, ENABLE);
  GPIO_LCD.GPIO_Pin = 0x00FF; 
  GPIO_LCD.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_LCD.GPIO_Mode = GPIO_Mode_Out_PP;
  GPIO_Init(LCD_DATA, &GPIO_LCD);
  GPIO_SetBits(LCD_DATA, 0x00FF); 
}

void lcdBusyWait(void) 
{
  // wait until LCD busy bit goes to zero
  // do a read from control register
  GPIO_ResetBits(LCD_CTRL_PORT, LCD_CTRL_RS); 
                                            
  GPIO_LCD.GPIO_Pin = 0x00FF;
  GPIO_LCD.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_LCD.GPIO_Mode = GPIO_Mode_IN_FLOATING;
  GPIO_Init(LCD_DATA, &GPIO_LCD);
  GPIO_SetBits(LCD_DATA, 0x00FF); 
  
  GPIO_SetBits(LCD_CTRL_PORT, LCD_CTRL_RW | LCD_CTRL_E);
  
  LCD_DELAY;
  
  while((GPIO_ReadInputDataBit(LCD_DATA, 1<<LCD_BUSY))) { 
    GPIO_ResetBits(LCD_CTRL_PORT, LCD_CTRL_E);  
    LCD_DELAY;
    LCD_DELAY; 
    GPIO_SetBits(LCD_CTRL_PORT, LCD_CTRL_E);  
    LCD_DELAY; 
    LCD_DELAY; 
  }
  GPIO_ResetBits(LCD_CTRL_PORT, LCD_CTRL_E); 
}

void lcdControlWrite(u8 data) 
{
  lcdBusyWait();    
  GPIO_ResetBits(LCD_CTRL_PORT, LCD_CTRL_RS | LCD_CTRL_RW); 
  
  GPIO_SetBits(LCD_CTRL_PORT, LCD_CTRL_E); 
  
GPIO_LCD.GPIO_Pin = 0x00FF;
  GPIO_LCD.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_LCD.GPIO_Mode = GPIO_Mode_Out_PP;
  GPIO_Init(LCD_DATA, &GPIO_LCD);
  
  GPIO_ResetBits(LCD_DATA, 0x00FF); 
  GPIO_SetBits(LCD_DATA, data);               
  LCD_DELAY; 
  LCD_DELAY; 
  
  GPIO_ResetBits(LCD_CTRL_PORT, LCD_CTRL_E); 
  LCD_DELAY;
  LCD_DELAY;
}

u8 lcdControlRead(void) 
{
  
  u8 data;
  
  lcdBusyWait();      
  
  GPIO_LCD.GPIO_Pin = 0x00FF;
  GPIO_LCD.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_LCD.GPIO_Mode = GPIO_Mode_IN_FLOATING;
  GPIO_Init(LCD_DATA, &GPIO_LCD);
  
  GPIO_SetBits(LCD_DATA, 0x00FF); 
  GPIO_ResetBits(LCD_CTRL_PORT, LCD_CTRL_RS); 
  GPIO_SetBits(LCD_CTRL_PORT, LCD_CTRL_RW);    
  GPIO_SetBits(LCD_CTRL_PORT, LCD_CTRL_E);   
  LCD_DELAY;   
  LCD_DELAY;  
  data  =(GPIO_ReadInputData(LCD_DATA)); 
  GPIO_ResetBits(LCD_CTRL_PORT, LCD_CTRL_E); 
  
  return data; 
}

void lcdDataWrite(u8 data) 
{
  // RS=1, R/W=0, E=1, DATA = data
  // write a data byte to the display
  
  lcdBusyWait();  // wait until LCD not busy
  
  GPIO_SetBits(LCD_CTRL_PORT, LCD_CTRL_RS); 
  GPIO_ResetBits(LCD_CTRL_PORT, LCD_CTRL_RW); 
  GPIO_SetBits(LCD_CTRL_PORT, LCD_CTRL_E); 
  
  GPIO_LCD.GPIO_Pin = 0x00FF;
  GPIO_LCD.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_LCD.GPIO_Mode = GPIO_Mode_Out_PP;
  GPIO_Init(LCD_DATA, &GPIO_LCD);
  
  GPIO_ResetBits(LCD_DATA, 0x00FF); 
  GPIO_SetBits(LCD_DATA, data&0xFF); 
  LCD_DELAY;   
  LCD_DELAY;   
  GPIO_ResetBits(LCD_CTRL_PORT, LCD_CTRL_E);
}

u8 lcdDataRead(void) 
{
  u8 data;
  lcdBusyWait(); 
  

GPIO_LCD.GPIO_Pin = 0x00FF;
  GPIO_LCD.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_LCD.GPIO_Mode = GPIO_Mode_IN_FLOATING;
  GPIO_Init(LCD_DATA, &GPIO_LCD);
  
  GPIO_SetBits(LCD_DATA, 0x00FF); 
  GPIO_SetBits(LCD_CTRL_PORT, LCD_CTRL_RS | LCD_CTRL_RW); 
  GPIO_SetBits(LCD_CTRL_PORT, LCD_CTRL_E);  
  
  LCD_DELAY;      
  LCD_DELAY;
  
  data = GPIO_ReadInputData(LCD_DATA);
  GPIO_ResetBits(LCD_CTRL_PORT, LCD_CTRL_E);  
  
  return data;
}

void lcdInit() 
{
  lcdInitHW();
 
  lcdControlWrite(LCD_FUNCTION_DEFAULT);
  lcdControlWrite(1<<LCD_CLR);
  lcdControlWrite(1<<LCD_ENTRY_MODE | 1<<LCD_ENTRY_INC);
  lcdControlWrite(1<<LCD_ON_CTRL | 1<<LCD_ON_DISPLAY | 1<<LCD_ON_CURSOR | 1<<LCD_ON_BLINK);
  lcdControlWrite(1<<LCD_HOME);
  lcdControlWrite(1<<LCD_DDRAM | 0x00); 
}

void lcdHome(void) 
{
  lcdControlWrite(1<<LCD_HOME);
}

void lcdClear(void)
{
  lcdControlWrite(1<<LCD_CLR);
}

void lcdGotoXY(u8 x, u8 y) 
{
  u8 DDRAMAddr = x;

  switch(y) {
  case 0: DDRAMAddr = LCD_LINE0_DDRAMADDR+x; break;
  case 1: DDRAMAddr = LCD_LINE1_DDRAMADDR+x; break;
  case 2: DDRAMAddr = LCD_LINE2_DDRAMADDR+x; break;
  case 3: DDRAMAddr = LCD_LINE3_DDRAMADDR+x; break;
  default: DDRAMAddr = LCD_LINE0_DDRAMADDR+x;
  }
  lcdControlWrite((1<<LCD_DDRAM)|DDRAMAddr); 
}

void lcdPrintData(char* data, u8 nBytes)
{
  u8 i;
  
  
  if (!data)
    return;
  
  for(i=0; i<nBytes; i++) { 
    lcdDataWrite(data[i]);
  }
} 


int main(void) {
  Init_STM32F103();
  
  lcdInit();
  
  lcdDataWrite('H');
  lcdDataWrite('e');
  lcdDataWrite('l');
  lcdDataWrite('l');
  lcdDataWrite('o');
  
  lcdGotoXY(7, 1);
  
  lcdPrintData("STM32!!", 7);
  
  while(1);
}



```


* 코드 설명

lcd.h 파일을 새로 만들어 사용할 매크로들을 선언해줍니다.
lcd.h에서 먼저 컨트롤 포트와 관련된 매크로를 지정합니다. 컨트롤 포트로 GPIOC를 지정해주고 RS로는 0번핀, RW로는 1번핀, E로는 2번핀을 지정해줍니다. 그리고 데이터 포트와 관련된 매크로를 지정합니다. 데이터 포트로 GPIOA를 지정해줍니다. 그 다음으로 라인 수와 길이를 지정하는데 우리는 두 개의 라인을 사용하고 한 라인당 길이는 16으로 지정해줍니다. 각 라인에 대한 DDRAM 주소도 지정해주는데 첫 번재 라인의 base address는 0x00, 두 번째 라인의 base address는 0x40입니다. 그 다음으로는 delay가 나도록 해줄 매크로 LCD_DELAY를 지정해줍니다.
그 밑으로는 명령어들에 대한 매크로들을 지정합니다. LCD_CLR는 0번째 비트, LCD_HOME은 1번째 비트, LCD_ENTRY_MODE는 2번째 비트, 그리고 1번째 비트와 0번째 비트를 가지고 엔트리 모드를 설정해줍니다. 디스플레이 컨트롤은 3번재 비트로 컨트롤하고, 3번째 비트 밑에 있는 비트로 디스플레이 온오프 컨트롤을 합니다. 그리고 MOVE, FUNCTION에 대한 비트를 지정해주고, CGRAM, DDRAM에 대한 비트도 지정해준 다음, 값을 읽어올 때 필요한 매크로인 LCD_BUSY의 를 7번째 비트로 짖ㅇ해준 다음 8비트를 사용한다는 것을 매크로로 지정해주고 나중에 넣어서 하드웨어 설정을 해줄 디폴트 값도 지정해준 후 GPIO를 하나 선언해줍니다.
main.c에서는 lcd.h를 포함한 코드에 필요한 헤더파일들을 선언해준 뒤 LCD에 대한 라이브러리 함수들을 직접 구현합니다. 
lcdInitHW() 메소드는 LCD 하드웨어를 초기화하는 메소드로, 컨트롤 포트인 GPIOC와 GPIOA를 모두 output 모드로 설정해주고 초기 풀업을 해줍니다. 이 때 GPIOC의 RS, RW, E 를 모두 0으로 넣어줍니다.
lcdBusyWait() 메소드느 Busy 플래그를 체크하는 메소드로, RS를 0으로 설정해 명령어 레지스터를 읽을 수 있도록 한 뒤 GPIOA를 input모드로 설정하고 초기 풀업을 합니다. 그리고 RW와 E를 모두 1로 설정해 읽기 모드를 실행시킨 다음 LCD_DELAY 매크로로 시간을 지연시키고 Busy 플래그의 값이 0이 될 때까지 기다리는 while문을 작성했습니다. 그 안에서 LCD_DELAY를 사이에 두고 E를 0으로 리셋했다가 다시 1로 set해주기를 반복합니다. while문을  빠져나온 다음에는 LCD에 다른 값을 넣을 수 있도록 E를 0으로 리셋해줍니다.
lcdControlWrite() 메소드는 명령어를 받아 명령어를 써주는 메소드로, lcdBusyWait() 메소드로 LCD를 사용할 수 있을 때까지 대기했다가 RS, RW 모두 0으로 설정해 IR 쓰기 모드로 만든 뒤 E를 1로 설정해줍니다. 그리고 GPIOA를 다시 output 모드로 설정해준 후 GPIO_ResetBits()로 초기화한 후 GPIO_SetBits()로 전달받은 값을 내보내줍니다. 그리고 LCD_DELAY로 시간을 지연시킨 다음 E를 0으로 설정해 다음에 다시 LCD를 사용할 수 있도록 합니다.
lcdControlRead() 메소드는 값을 읽는 메소드인데, data 변수를 선언해준 후 lcdBusyWait() 함수를 사용해 LCD를 사용할 수 있을 때까지 기다렸다가 GPIOA를 input 모드로 설정해주고 RS=0, RW=1, E=1로 설정해주어 IR 읽기 모드를 실행하고 LCD_DELAY로 시간을 시연시켰다가 GPIO_ReadInputData()를 통해 GPIOA의 데이터를 읽어 data에 저장해준 다음 E를 다시 0으로 설정하고 data를 return해줍니다.
lcdDataWrite() 메소드는 lcdControlWrite와 다르게 RS=1로 설정해 data register에 값을 쓰는 메소드로, lcdBusyWait() 로 LCD를 사용할 수 있을 때까지 기다렸다가 RS=1, RW=0, E=1로 설정해 DR 쓰기 모드로 설정해 줍니다. 그 다음 GPIOA를 output으로 설정해준 다음 데이터를 GPIOA에 써주고 DELAY시켜주었다가 E를 리셋합니다.
lcdDataRead() 메소드는 data register의 값을 읽는 메소드로, data 변수를 선언하고 lcdBusyWait() 로 LCD 를 쓸 수 있을 때까지 기다렸다가 GPIOA를 input 모드로 설정하고 초기 풀업을 해준 다음 RS=1, RW=1, E=1로 설정해 DR 읽기 모드로 설정해준 다음 LCD_DELAY 매크로로 기다렸다가 data에 GPIOA로부터 읽은 데이터를 저장하고 E를 0으로 설정한 후에 data를 return해줍니다.
lcdInit() 메소드는 LCD 자체를 기본 초기화해주는 메소드로, 먼저 lcdInitHW()를 사용해 하드웨어를 초기화해준 다음 function 설정해주고 LCD를 클리어시키고 엔트리 모드, 디스플레이에 대해 설정해준 다음 커서를 홈으로 이동시켜주고, DDRAM 주소를 base address 0x00으로 설정해줍니다.
lcdHome() 메소드는 홈 명령어를 써주는 메소드입니다.
lcdClear() 메소드는 컨트롤 명령어를 써주는 메소드입니다.
lcdGotoXY() 메소드는 특정 위치로 보내는 메소드로, DDRAMAddr 변수를 선언해주고  y의 값에 따라 각 라인의 base address 값에 x값을 더한 값을 DDRAMAddr에 저장해주고 lcdControlWrite()를 사용해 1을 7번 왼쪽으로 shift해준 10000000에 DDRAMAddr주소를 넣어주어 DDRAM 주소값을 설정합니다.
lcdPrintData() 메소드는 스트링 문장을 받아서 쓰는 메소드로, 우리가 제대로 된 data 값을 받았는지 if문으로 확인해준 다음 for문으로 캐릭터 주소를 증가시키며 lcdDataWrite()를 통해 하나씩 값을 써줍니다.

그 다음으로 main()함수에서는 Init_STM32F103()으로 초기화해준 뒤 lcdInit()을 통해 LCD도 초기화해줍니다. 그리고 lcdDataWrite()를 통해 원하는 문자를 내보내준 후 lcdGotoXY()를 통해 원하는 장소로 커서를 이동시키고 lcdPrintData()를 이용해 원하는 문장을 내보내줍니다. 그리고 while(1)로 시간을 지연시켜줍니다.


