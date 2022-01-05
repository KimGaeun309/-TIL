## Lab 10

* code

lcd.h
``` C

#define LCD_CTRL_PORT_CLK   RCC_APB2Periph_GPIOB
#define LCD_CTRL_PORT       GPIOB
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

void lcdInitHW(void);
void lcdBusyWait(void);
void lcdControlWrite(u8 data);
u8 lcdControlRead(void);
void lcdDataWrite(u8 data);
u8 lcdDataRead(void);
void lcdInit();
void lcdHome(void);
void lcdClear(void);
void lcdGotoXY(u8 x, u8 y);
void lcdPrintData(char* data, u8 nBytes);

```

lcd.c
``` C
#include "stm32f10x_lib.h"
#include "System_func.h"
#include "lcd.h"

GPIO_InitTypeDef GPIO_LCD; 



void lcdInitHW(void) 
{
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
  lcdBusyWait(); 
  
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

```
keypad.h
``` C

#define IN_PORT     GPIOC 
#define IN_DDR      RCC_APB2Periph_GPIOC
#define IN_MASK     0x000f 


#define IN_1        GPIO_Pin_0  
#define IN_2        GPIO_Pin_1
#define IN_3        GPIO_Pin_2
#define IN_4        GPIO_Pin_3

#define IN_LINE     (IN_1 | IN_2 | IN_3 | IN_4) 

#define LINE_PORT   GPIOC 
#define LINE_DDR    RCC_APB2Periph_GPIOC 

#define LINE_1      GPIO_Pin_4
#define LINE_2      GPIO_Pin_5
#define LINE_3      GPIO_Pin_6
#define LINE_4      GPIO_Pin_7

#define LINE_MASK   (LINE_1 | LINE_2 | LINE_3 | LINE_4)


```
main.c
``` C
#include "stm32f10x_lib.h"
#include "System_func.h"
#include "lcd.h"
#include "keypad.h"

void init_keypad(void);
u8 passwd_check(u8 pass[]);
void passcheck(u8 data);
void reset_check(void);
void back_pass(void);
u8 get_passwd(void);
void Timer3_Delay_init();
void delay_ms(u16 nCount);

void rotate_motor(u8 direction);


u8 cnt = 0; 
u8 pass[4] = {0};

u8 PASSWD[] = "1234"; 

void init_keypad(void){ 
  GPIO_InitTypeDef GPIO_InitStructure;
  RCC_APB2PeriphClockCmd(IN_DDR | LINE_DDR, ENABLE);
  
  GPIO_InitStructure.GPIO_Pin = LINE_1 | LINE_2 | LINE_3 | LINE_4; 
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;
  GPIO_Init(LINE_PORT, &GPIO_InitStructure);
  
  GPIO_InitStructure.GPIO_Pin = IN_1 | IN_2 | IN_3 | IN_4; 
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
  GPIO_Init(IN_PORT, &GPIO_InitStructure);
  
  lcdInit();
  lcdGotoXY(0, 0);
  lcdPrintData("PASSWORD?", sizeof("PASSWORD?")-1);
  lcdGotoXY(0, 1); 
  lcdDataWrite('>');
}

void Timer3_Delay_init() {
  TIM_TimeBaseInitTypeDef TIM3_TimeBaseInitStruct;
  
  RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM3, ENABLE);
  
  TIM3_TimeBaseInitStruct.TIM_Prescaler = 7200 -1;
  TIM3_TimeBaseInitStruct.TIM_CounterMode = TIM_CounterMode_Up;
  TIM3_TimeBaseInitStruct.TIM_Period = 10 - 1;
  TIM3_TimeBaseInitStruct.TIM_ClockDivision = TIM_CKD_DIV1;
  TIM_TimeBaseInit(TIM3, &TIM3_TimeBaseInitStruct);
}

void delay_ms(u16 time) { 
  u16 i;
  TIM_Cmd(TIM3, ENABLE); 
  for(i=0; i<time; i++) { 
    while(TIM_GetFlagStatus(TIM3, TIM_IT_Update)==RESET);
    TIM_ClearFlag(TIM3, TIM_FLAG_Update); 
  }
  TIM_Cmd(TIM3, DISABLE);
}

int main(void) {
  Init_STM32F103();
  
  init_keypad(); 
  
  Timer3_Delay_init(); 
  
  while(1) {
    
    GPIO_ResetBits(IN_PORT, IN_LINE); 
    GPIO_SetBits(IN_PORT, IN_2 | IN_3 | IN_4); 
    if(GPIO_ReadInputDataBit(LINE_PORT, LINE_1)==0) { 
      passcheck('1');
    }
    else if(GPIO_ReadInputDataBit(LINE_PORT, LINE_2)==0) { 
      passcheck('4');
    }
    else if(GPIO_ReadInputDataBit(LINE_PORT, LINE_3)==0) {
      passcheck('7');
    }
    else if(GPIO_ReadInputDataBit(LINE_PORT, LINE_4) == 0) {
      back_pass();
    }
    delay_ms(1);  
    
    GPIO_ResetBits(IN_PORT, IN_LINE);
    GPIO_SetBits(IN_PORT, IN_1 | IN_3 | IN_4); 
    if (GPIO_ReadInputDataBit(LINE_PORT, LINE_1)==0) {
      passcheck('2');
    }
    else if(GPIO_ReadInputDataBit(LINE_PORT, LINE_2)==0) {
      passcheck('5');
    }
    else if(GPIO_ReadInputDataBit(LINE_PORT, LINE_3)==0) {
      passcheck('8');
    }
    else if(GPIO_ReadInputDataBit(LINE_PORT, LINE_4)==0) {
      passcheck('0');
    }
    delay_ms(1); 
    
    GPIO_ResetBits(IN_PORT, IN_LINE);
    GPIO_SetBits(IN_PORT, IN_1 | IN_2 | IN_4); 
    if(GPIO_ReadInputDataBit(LINE_PORT, LINE_1)==0) {
      passcheck('3');
    }
    else if(GPIO_ReadInputDataBit(LINE_PORT, LINE_2)==0) {
      passcheck('6');
    }
    else if(GPIO_ReadInputDataBit(LINE_PORT, LINE_3)==0) {
      passcheck('9');
    }
    else if(GPIO_ReadInputDataBit(LINE_PORT, LINE_4)==0) {
      reset_check();
    }
    delay_ms(1);
    
    GPIO_ResetBits(IN_PORT, IN_LINE);
    GPIO_SetBits(IN_PORT ,IN_1 | IN_2 | IN_3); 
    if(GPIO_ReadInputDataBit(LINE_PORT, LINE_1)==0) {
      reset_check();
    }
    else if(GPIO_ReadInputDataBit(LINE_PORT, LINE_2)==0) {
      reset_check();
    }
    else if(GPIO_ReadInputDataBit(LINE_PORT, LINE_3)==0) {
      reset_check();
    }
    else if(GPIO_ReadInputDataBit(LINE_PORT ,LINE_4)==0) {
      reset_check();
    }
    delay_ms(1); 
  }
}

void passcheck(u8 data) {
  if(cnt!=3) {
    lcdDataWrite('*');
    pass[cnt++] = data;
    delay_ms(200);
  } else if(cnt==3) {
    lcdDataWrite('*');
    pass[cnt] = data;
    
    if(passwd_check(pass)!=0) {
      lcdGotoXY(0, 0);
      lcdPrintData("WrongPassWord!", sizeof("WrongPassWord")-1);
      
      rotate_motor(0); 
      
      cnt = 0; 
      delay_ms(1000);
      lcdClear();
      
      delay_ms(1000);
      lcdClear();
      
      delay_ms(1000);
      
      lcdGotoXY(0, 0); 
      lcdPrintData("PASSWORD?", sizeof("PASSWORD?")-1);
      lcdGotoXY(0, 1);
      lcdDataWrite('>');
    } else { 
      lcdClear();
      
      lcdGotoXY(0, 0);
      lcdPrintData("Hello MCU_WORLD", sizeof("Hello MCU_WORLD")-1);
      
      rotate_motor(1); 
        
      cnt = 0;
      
      delay_ms(2);
    }
  }
}

u8 passwd_check(u8 pass[]) { 
  u8 _error = 0;
  u8 i;
  for(i=0; i<4; i++) {
    if(pass[i]!=PASSWD[i])
      _error++;
  }
  return _error;
}

void back_pass(void) { 
  if(cnt!=0) {
    lcdGotoXY(cnt, 1);
    lcdDataWrite(' ');
    lcdGotoXY(cnt, 1);
    cnt--;
  }
}

void reset_check(void) { 
  lcdClear();
  delay_ms(1000);
  
  lcdGotoXY(0, 0);
  lcdPrintData("Reset!!", sizeof("Reset!!")-1);
  
  delay_ms(1);
  
  lcdGotoXY(0, 0);
  lcdPrintData("PASSWORD?", sizeof("PASSWORD?")-1);
  lcdGotoXY(0, 1);
  lcdDataWrite('>');
  
  cnt = 0;
}


void rotate_motor(u8 direction) {
  GPIO_InitTypeDef GPIO_InitStructure;
  
  unsigned char mot_tbl[] = {0x01, 0x02, 0x04, 0x08, 0x01, 0x02, 0x04, 0x08};
  u8 index = 0;
  unsigned int count = 0;

  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC, ENABLE);
  
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_8 | GPIO_Pin_9 | GPIO_Pin_10 | GPIO_Pin_11;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
  GPIO_Init(GPIOC, &GPIO_InitStructure);
  GPIO_SetBits(GPIOC, 0x00);
  
  for(count = 0; count < 5000; count++) {
    GPIO_ResetBits(GPIOC, (mot_tbl[index]<<8)); 
    
    if (direction == 1) {
      index++;
      if (index >=8)
        index = 0;
    } else {
     if (index==0)
       index = 8;
     index--;
    }
    
    GPIO_SetBits(GPIOC, (mot_tbl[index]<<8));
    delay_ms(1);
  }
  
}

```

* 코드 설명

main.c에서 먼저 헤더 파일들을 include해주고 사용할 함수들과 변수들을 선언줍니다. 
main()함수에서는 init_keypad()라는 함수를 호출해 키패드를 초기화하고 Timer3_Delay_init()이라는 함수를 호출해 타이머를 초기화해줍니다. init_keypad()에서는 GPIO를 초기화하기 위해 GPIO_InitStructure 라는 구조체를 가져오고 클럭을 인가한 다음 LINE_1 LINE2 LINE3 LINE4 (keypad.h에서 GPIO_Pin_4 ~ GPIO_Pin_7로 define함) 에 해당하는 핀들을 input모드로, IN_1 IN_2 IN_3 IN_4 (keypad.h에서 지정함) 에 해당하는 핀들을 output 모드로 설정해주고 초기화한 다음 lcdInit() 함수를 호출해 lcd 를 초기화해준 후 (0,0)으로 커서를 옮긴 뒤 PASSWORD? 라는 문구를 출력하고 커서를 그 다음줄로 옮겨 > 를 출력합니다.그 다음으로 Timer3_Delay_init() 함수를 호출해 타이머를 초기화해줍니다. Timer3_Delay_Init() 함수에서는 TIM3_TimeBaseInitStruct를 가져오고 클럭을 인가한 후 Prescaler를 7200-1로, Period는 10-1로 설정해 1ms 동안 시간을 지연시키는 타이머를 생성합니다. 
그 다음으로 while()문을 통해 키패드에서 입력받은 값이 무엇인지 확인합니다. while문 안에서 IN_PORT에 대해 0111, 1011, 1101, 1110 을 각각 내보내 IN_1, IN_2, IN_3, IN_4에 대해 입력이 있었는지 확인합니다. 이 때 if~else if~else 문을 사용해 각각의 상황에서 LINE_1, LINE_2, LINE_3, LINE_4 이 0인지 확인해 눌린 버튼이 어떤 것인지 확인하고 눌린 버튼에 따라  passcheck() 함수 또는 back_pass() 함수 또는 reset_check() 함수를 사용합니다. 
passcheck() 함수에서는 4자리의 패스워드가 맞는지 확인합니다. cnt가 3이 아니면 아직 네 자리의 번호를 모두 입력받지 못했으므로 lcdDataWrite에 * 을 출력하고 pass[cnt]에 입력받은 버튼에 해당하는 숫자를 저장한 후 cnt 값을 증가시킨 다음 delay_ms() 함수로 200ms의 딜레이를 줍니다. delay_ms() 함수에서는 time 매개변수를 입력받아 타이머를 enable시킨 후 for에서 타이머를 구동시켜 time ms 시간만큼의 딜레이가 발생합니다. 만약 cnt가 3이면 번호를 모두 입력받았으므로 pass[cnt]에 입력된 숫자를 저장한 후 passwd_check() 함수를 통해 입력받은 번호가 password가 맞는지 확인합니다. passwd_check() 함수에서는 _error 라는 변수를 선언하고 0으로 초기화해 password가 저장된 PASSWD 배열과 매개변수로 받은 pass 배열의 원소들을 하나씩 비교하며 값이 다를 때마다 _error 값을 증가시킨 후 리턴해줍니다. 만약 passwd_check() 함수가 리턴한 값이 0이 아니라면 비밀번호가 틀렸으므로 lcdClear() 함수를 통해 쓰여진 값들을 없앤 후 lcdGotoXY() 함수로 0,0 으로 커서를 옮긴 다음 lcdPrintData() 함수로 WrongPassWord! 라는 문구를 출력한 다음 rotate_motor() 함수에 0을 매개변수로 주어 모터를 역방향으로 회전시킵니다. rotate_motor() 함수에서는 GPIOC의 8번핀~11번핀을 output모드로 설정한 다음 for문을 통해 5000번 GPIOC에 mot_tbl[index]<<8의 값을 넣어 GPIOC의 high로 1상여자방식의 STEP_A에 해당하는 값을 보낸 다음, 매개변수로 받은 direction이 0이면 index가 7부터 0까지 줄어들기를 반복하도록, 1이면 index가 0부터 7까지 증가하기를 반복하도록 한 다음 GPIOC에 mot_tbl[index]<<8의 값을 넣어 그 다음 스텝으로 넘어가도록 한 다음 delay_ms()로 1ms의 시간동안 지연시키기를 반복합니다. 그러면 5000ms 동안 direction이 0이면 왼방향으로, direction이 1이면 오른방향으로 회전합니다. 그 다음으로 cnt를 0으로 리셋시키고 1000ms 의 딜레이를 준 다음 LCD의 글씨들을 지우고 LCD에 다시 PASSWD? 와 > 글씨를 띄웁니다. 
만약 passwd_check() 함수가 리턴한 값이 0이라면 비밀번호가 맞는 경우이므로 LCD를 클리어한 다음 Hello MCU_WORLD 라는 문구를 출력하고 rotate_motor()에 1을 매개변수로 주어 모터를 순방향으로 회전시킨 다음 cnt를 0으로 설정하고 딜레이를 줍니다. 
back_pass() 함수는 cnt가 0이 아니면 커서를 (cnt,1)에 해당하는 곳으로 옮겨공백을 출력시켜 이전에 쓰여졌던 문자를 지운 다음 다시 커서를 (cnt, 1)로 옮기고 cnt값을 감소시켜 백스페이스 기능을 수행합니다.
reset_check() 함수는 패스워드 체크를 리셋시키는 함수로, LCD를 클리어한 다음 딜레이를 주었다가 Reset!! 문구를 잠시 띄우고 PASSWORD? 와 > 를 출력시키고 cnt를 0으로 초기화합니다.

* 실행 결과

잘못된 비밀번호를 입력하면 Text LCD에 “WrongPassWord!” 라는 문구가 출력되
고 모터가 왼방향으로 회전됩니다.
알맞은 비밀번호를 입력하면 Text LCD에 “Hello MCU_WORLD” 라는 문구가 출력
되고 모터가 오른방향으로 회전됩니다.
