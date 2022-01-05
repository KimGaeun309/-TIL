# 4강 - CortexM3 Instruction Set

- 4강 목차

이번주부터 3주간 마이크로프로세서의 명령어 set (프로그래머 입장 - 하드웨어 칩을 이용해 하드웨어 기반 시스템 프로그램을 작성해야 하는) 에 대해 알아보고 그 명령어들을 사용해서 기본적으로 프로그램이 마이크로프로세서 위에서 어떻게 구동되는지를 익혀보는 강의가 되겠습니다.

## Agenda

### Assembly Basics

instruction set 란 기계어이기 때문에 그것을 더 쉽게 표현한 Assembly 표현법을 배울 건데 그 기초가 되는 Assembly Basics 를 배울 것이다. 

### Endian format

그리고 메모리에 데이터가 들어가는 개념이 뭐냐, 기본적으로 컴퓨터 시스템이란 cpu 와 메모리 등과 같은 가장 기본적인 소자를 기반으로 하는데 데이터를 저장하는 곳은 메모리이고 데이터를 메모리에 저장하는 방법은 프로세서마다 차이가 있을 수 있다.  데이터의 포멧 크기와 실제 메모리에 데이터를 담는 게 다르기 때문. 기본적으로  Endian format ... 메모리에 어뗗게 데이터를 담는지에 대해 배울 것.

### Cortex-M3 Registers & Memory

instruction 에 기반해서 어떤 정보들을 프로세서에 ...프로그래밍하는가.

### Cortex-M3 Instruction Set Architecture

cortex-m3에 어떤 명령어 세트가 있느냐.

## Assembly Basics

### Assembler Language: Basic Syntax

assembly language 의 기본은 1문장 1명령어.

- Common format for assembler code

일반적인 format은 다음 그림과 같다.

- Label

일반적인 format - 라벨을 붙인다. 

라벨은 사실 명령어는 아니고 라벨이 적혀진 곳의 주소를, 라벨 표기법을 만듦. 라벨이 있으면 컴파일러가 어떤 텍스트파일을 컴파일해서 ... 

어셈블러로 코드를 작성하면 논리적인건데 이걸 실행 파일로 바꾸면 코드가 나오고 이 코드들이 메모리에 들어갈 때 주소값이 이미 정해져있다. 그럼 이 주소, 특정 위치를 구분하기 위해 특정 위치에 라벨을 붙인다. 라벨이 실제 주소 값으로 바뀌어 어셈블러가(?) 주소 값으로 인식. 라벨은 하나의 독립적인 인식 장치(?). 

실제 명령어의 표현은 Opcode 와 Oprands 로 이루어진다.

- Opcode

명령어의 encoded symbol. 프로세서가 실제 실행할 명령어들을 우리가 이해하기 쉬운 단어나 표기법으로 표현한 것. ex) ADD, MOV, LDR, STR 등등...

- Operands

피연산자..

ex) ADD       R1, R2, R3

    opcode    operands

- Comments

주석. 프로그램의 이해도를 높이기 위해. 

// 혹은 ; (어셈블리어는 1문장 1명령이기 때문에 굳이 ; 을 문장 뒤에 붙일 필요가 없었음.)

결론: opcode 와 operands 의 조합으로 instruction set 이 작성된다.

## Assembly Basics

### Assembler Language examples

MOV          R0,                 #0x12               ; Set R0 = 0x12

opcode   operand     immediate value       comment

             destination          source

### Define constant using EQU (similar to #define in c)

어셈블리 코드에서도 어떤 상수 값을 기호로 define 해서 그 기호를 쓰는 것이 편할 수 있다 → EQU 라는 걸로 define. 

### Assembler Language: Use of Suffixes

suffix 개념은 cortex-m3를 포함해 arm 프로세서를 위한 어셈플리 코드에서 사용되는데, arm 프로세서를 위한 어셈블러 코드에서는 suffix 라는 것을 통해서 instuction을 많이 확장시킬 수 있다. suffix는 번역하자면 접미사이다. 어떤 명령어 뒤에 suffix를 붙여 명령어를 확장시켜 많은 일을 수행하도록 할 수 있다.

ADD  R1, R2, R3    ; R1 = R2 + R3

ADDS   ADDEQ   ADDNE  ADDLT  ADDGT 등등... 을 통해 의미를 다양화.

## The Endianess religious war: 288 years and counting!

어셈블리에 대한 기본 표현법에 대해 알아보았고, 이제 메모리에 데이터가 저장되어있다고 하는 개념에 대해 설명하겠다. 이것은 원론적인 내용이기에 어디선가 들어보게 될 것이나 적용하기 어렵다.

Endian 이라는 개념이 있다. 메모리의 주소는 byte level 에서 메모리가 만들어진다. 메모리 주소를 만들 때 공간의 크기는 byte 기준이다. 따라서 주소값은 비트에 따라 0x0, 0x1, ... 이렇게 되면 헷갈릴 일이 없다. 하지만 cpu와 memory가 데이터를 주고받을 때 cortex-m3 기준 32비트 즉 4바이트를 한 번에 전송할 수 있다. 4 byte를 cpu 에서 받는데 cpu 입장에서 32 비트를 표현하면 4바이트가 나오는데 MSB, LSB 라는 용어가 나오는데 LSB 는 least significant bit, MSB 는 most significant bit. 0번째 자리수를 LSB라고 한다. 3번째 자리수를 MSB 라고 한다.

이때 표현법에는 little-endian 방식과 big-endian 방식이 있다. 

little-endian 에서는 LSB 에 담긴 값을 메모리의 낮은 address 에 저장한다.

big-endian 에서는 MSB 에 담긴 값을 메모리의 낮은 address 에 저장한다.

왜? cpu 마다 다르기 때문. arm 은 little-endian 방식을 사용한다.

## Addressing: Big Endian vs Little Endian

cpu 가 바라보는 메모리의 order 와 실제 메모리에 저장되어 있는 order 가 달라진다. little-endian 은 lsb가 낮은 메모리 주소로, big-endian은 msb가 낮은 메모리 주소로. 

MIPS 라는 것은 cpu architecture 인데 big-endian방식을 사용하고 있고, 우리가 흔히 아는 intel 계열, 그리고 arm 계열 cpu는 little-endian 방식의 구조를 가진다.

## ARM Cortex-M3 Memory Formats (Endian)

word 란 cpu 와 memory 간에 한 번에 전송할 수 있는 기본단위.

어떤 cpu가 몇 비트 머신이냐? cortex-m3는 32 비트 머신이므로 32비트가 하나의 word 이다. 64 비트 cpu에서는 64비트가 하나의 word 이다.

그래서 프로그래밍에서 word 단위로 데이터를 주고받으면 endian 을 고려할 필요가 없다. word 단위로 주고받으면 메모리에 어떻게 적혔든  하나의 word 단위로 한 번에 적힌 순서 상관 없이 왔다갔다 하기 때문. 

하지만 워드 단위가 아닌 바이트 단위로 데이터를 주고받게 될 경우 little endian, big endian을 잘 알아서 어디에 있는 데이터인지를 잘 고려할 필요가 있다. (이론적인 얘기. endian의 개념이 있다는 것 정도만 알아두자. 실습에서 이걸 알아보지는 않을 것.)

## Instruction Set Architecture

어셈블리 코드를 표현하는 기본 개념. cpu와 메모리 간에 데이터가 전송되는 기본 개념을 알아보았고, 이제는 instruction set 라고 하는 것의 기본 개념과 cortex-m3에서 instruction set 이 어떻게 구성되어있는지, 또 이를 통해 어떻게 데이터를 주고받는지에 알아볼 건에 이건 지난 시간에 배운 내용을 복습하는 느낌... 리뷰한다 생각하고 들어라. cortex-m3는 기본적으로 ARM v7 Architecture 타입이다.

instruction type 에 여러가지 종류가 있다.

16비트 크기의 data processing instruction 이 있고 32비트 크기의 data processing instruction이 있고, 

16비트 크기의 load-store instruction 이 있고 32비트 크기의 load-store instruction 이 있다.

지난 시간에 ARM processing 의 철학 - RISC, Load-Store 아키텍쳐.

RISC 대표하는것 = fixed-size(고정된 크기의 명령어, 16비트 혹은 32비트. 하지만 주로 32비트 크기이니 32비트로 기억할 것.)

Load-Store 란 cpu는 데이터를 연산하고 memory 에 그 결과를 보내주는데 그 연산의 대상이 되는 것도 메모리에 있다. ARM 코어는 메모리에 있는 데이터를 

Load를 이용해 cpu 내부 레지스터로 옮긴다. 두번째로 연산하고 세번째로 다시 메모리로 데이터를 가지고 간다. 이게 바로 로드 스토어 아키텍쳐이다. 즉, 데이터를 처리하는 명령어와 데이터를 메모리에서 cpu로 , 혹은 cpu에서 메모리로 이동시키는 명령어를 명확하게 구분해놓은 아키텍쳐가 바로 Load-Store Architecture.

## An ISA defines the hardware/software interface

Load-Store. 메모리와 cpu 간의 이동이다. 다음으로 데이터 프로세싱, 즉 연산인데 연산은 cpu 내부의 레지스터를 가지고 한다. 

그 다음으로 중요한 것 중 하나는 Branch, 프로그램의 흐름을 제어하는 것.

이렇게 세 가지(Load-Store, Processing, Branch) 관점에서 명령어가 구성되어있다. 어떻게? = Addressing Mode(Load-Store와 관련. 주소값을 어떻게 지정하는지), Word size(Processing 과 관련. 워드 크기는? 한번에 연산을 하는 데이터의 크기는? ... 각 cpu마다 word 크기는 다름),  Data formats(명령어를 쓸 때 포멧을 어떻게 가져가는지), Operating modes는 어떻게 되는지, Condition codes(Branch 할 때, 조건 브랜치. 분기가 되는지.)

## ARM Cortex-M3 ISA

이런 관점에서 Cortex-M3는 어떻게 구성이 되어있나?

내부 연산을 하는 Register Set이 16개와 xPSR로 구성이 되어 있는데 13 14 15는 특수 목적. (13은 Stack Pointer, 14는 Link Register, 15는 Program Counter) 그 외 R0 ~ R12는 General Purpose.

그 다음 cpu 에서 바라보는 메모리는 Address Space가 32비트 머신이고, 주소가 0x00000000 부터 0xFFFFFFF 까지 펼쳐져 있다. 명령어들은 Branching (flow) 명령어, Data processing 명령어, Load-Store 명령어, Exceptions 명령어, Miscellaneous (예외적인 것들) 명령어들로 구분할 수 있다.

## Registers for ISA

레지스터에 대해 간략하게 다시 설명하자면 low, high 로 구분되어있긴 하지만 우리는 이걸 구분할 필요는 없다. 일반적으로 low register 8개가 중점적으로 사용되고 스택에 저장할 때 주로 이 8개 정도를 저장한다. 그 다음으로 R13 Stack Pointer, R14 Link Register, R15 PC 가 있고 xPSR 는 suffix과 연관이 있어서 opcode 뒤에 붙는 s 등의 suffix를 판별할 때 프로그램 레지스터에 있는 정보를 보고 판별을 한다.

## Address Space

address space는 계속 얘기하는데, cortex-m3는 32비트 머신이니까 0x0000000 ~ 0xFFFFFFF 까지 있는데 메모리 구성이 밑에 주소에 code가 들어가고, 0x4000000 부터는 periperal 영역인데 assembly 를 사용할 땐 사용할 일이 거의 없을 것이다. 외부 디바이스를 제어할 때 쓰이는 영역인데 C 코드에서 라이브러리를 통해 접근해야 하기 때문.  0x6000000 부터는 실제메모리인데 메모리 영역은 별로 쓰일 일은 없다. Code 영역에서 메모리까지 커버할 수 있기 때문에. 큰 프로그램을 돌릴 때나 메모리 영역이 사용된다. 그 위에는 외부 private peripheral 과 연결된 영역이 있는데 이곳까지 접근할 일은 거의 없다. 

## ARM Instruction Set Architecture

이 그림은 종합적으로 다 보여준다.

왼쪽이 cpu 영역, 오른쪽이 memory 영역. 

opcode와 operands

mov r0, #4 → 4 값을 r0에 넣어라. (mov: cpu안 레지스터간 데이터 이동)

ldr r1m [r0, #8] →  (ldr: memory에서 cpu로 데이터 이동, [] 안에 주소 값 적어둠)

bne loop → (branch. b는 무조건,  loop는 라벨. 코드의 어느 부분에 loop 라벨이 붙어있는게 있는데 이 loop으로 branch하라는 뜻. ne는 낫 이콜. 같지 않다. 이 상태를 program status register의 상위 비트를 보면 NZCVQ 라는 비트가 있는데 이 값들을 보고 이콜인지 낫 이콜인지 판별할 수 있다. 낫이콜이면 loop 쪽으로 가고 아니면 그 다음줄을 실행.

subs r2, #1 → s는 suffix 중 하나. program status register의 어떤 비트를 이 연산의 결과에 맞도록 업데이트를 하라고 시키는 suffix. (그 외의 다른 모든 suffix는 조건을 따져보는 suffix이다.)

# Instruction Descriptions Details

지금부터는 마이크로프로세서 cortex-m3의 instruction set의 종류와 명령어들의 구성과 명령어들의 사용 방법에 대해 알아볼 것. 자료를 보면 아까 얘기했듯이 명령어들의 타입이 크게 세 가지로 나뉜다. 데이터를 이동시키는 명령어, 데이터를 processing 하는 명령어, branch 하는 명령어. 또 이런 것들에 부가적으로 suffix를 사용해 부가적인 의미를 부여할 수 있다. 

### 1) Assembler Language: Moving Data

하나는 cpu 내부에 있는 레지스터에서 레지스터로 이동하는 명령어 - MOV

그 다음으로 메모리와 레지스터 간에 이동하는 명령어 - LDR

### 2) Assembler Language: Processing Data

그 다음으로 데이터를 처리하는 명령어는 데이터를 연산한다. 레지스터들 사이의 연산이다. 연산하는 유닛을 아리스메틱 로직 유닛, ALU 라고 한다. 이는 사칙연산, 논리적연산을 하는 유닛이란 뜻. 이런 연산들을 한다. - Addition, Subtraction, Multiply, Division.

### 3) Assembler Language: Call and Unconditional Branch

그 다음에 Branch. Branch 는 기본적으론 하나가 있고 뒤에 suffix가 붙어서 조건을 만들어낸다. 무조건 Branch가 있고 조건 Branch가 있는데 기본적으로 Branch 라고 하는 것은 프로그램의 흐름을 제어한다. (flow control) 

overview하는 측면에서 이 세 가지 타입에 대해 간단하게 살펴보았고, 오늘은 Moving Data 명령어들에 대해서 명령어 표기법과 사용 방법 예제에 대해 자세히 살펴보고 실습 시간에 실습을 해보도록 하겠습니다. 

## *1) Assembler Language: Moving Data*

아까 봤듯이 ,이 데이터를 이동하는 명령어는 프로세서에서 가장 기본적인 기능을 하는 명령어이다. 레지스터-레지스터 명령어인 MOV, 메모리-레지스터 명령어인 LDR, STR 이 있다. * 이 세 가지가 가장 기본!!

그 밑에 있는 명령어들은 특별한 명령어들인데, 이것은 우리가 실습에서 쓸 일은 없다. MRS 는 범용 레지스터가 아니라 특수 레지스터인 program status register 에 값을 읽고 쓸 수 있는 명령어이다. 

일단 MOV 명령어는 뒤에 operands 가 두 개 올 수 있다. 소스 레지스터에 담겨있는 값을 데스티네이션 레지스터로 복사해 옮겨준다. MOV R8 R3 의 경우 R3에 담긴 값을 복사해 R8 에 넘기는 것이다.

그 다음으로 LDR 와 STR 는 표기 방법은 비슷하지만 개념은 반대다. LDR는 메모리의 값을 레지스터로, STR는 레지스터의 값을 메모리로 옮기는 명령어이다.

표기법을 보면 LDR.W R0, {R0-R3} 앞에 있는 R0 가 데스티네이션, 뒤의 {R0-R3} 가 소스인데 메모리 주소 값이 오도록 되어 있다. C에서 포인터가 헷갈리는 개념인데 이 개념을 우리가 명확하게 받아들여야 한다.  이 괄호가 대괄호가 되면 이 값이 가리키는 값이 가리키는 메모리 영역이다.

STR R1, [] 에서는 앞의 R1이 소스가 되고 뒤의 괄호가 데스티네이션이 된다. (LDR과 반대!!)

그 다음에 이제 LDR든 MOV 든 뒤에 #(즉시)이 붙으면 숫자 자체를 가리키는 것이다. 

### Instruction Descriptions Details

MOV는 표현하기 쉽기 때문에 그냥 쓰면 되지만 LDR, STR는 굉장히 많은 변형이 있고 뒷부분에 메모리 주소값이 표기법이 되어 있는데 이 표기법이 복잡하다. 

cpu 내부에서 데이터를 이동시킬 때는 무조건 32비트 기준으로 데이터가 이동된다는 것을 알 수 있었는데, cpu 와 메모리간 데이터 이동에서도 32비트 단위로 데이터를 이동시키는데 그보다 적은 단위로 데이터를 주고받도록 하는 명령어가 확장되어 있다. 예를 들어 LDR 뒤에 H를 붙이면 16비트 데이터를 load 하거나 store 할 수 있다. 하지만 그냥 word 단위로 데이터를 이동시킨다고 한다면 그냥 LDR, STR 명령어를 사용하면 된다.

### Addressing Modes

이제 addressing mode 라고 세 가지 모드가 있다.

표현법이, LDR-STR 의 경우 LDR를  하고 뒤에 메모리 주소값이 온다고 했는데, 이 주소 표현법이 memory address를 지정하는 표현법이다. 이  addressing mode 가 offset, pre-indexed, post-indexed 세 가지이다. 왜냐면, 메모리 데이터를 가져올 때 array 의 경우 여러 개의 데이터를 가져온다.  이 때 주소값을 매법 증가시키는데 어떤 식으로 증가시키도록 만들어주는지에 대한 개념을 포함한다.

이는 C 프로그램의 pointer를 연상시킨다.

### 1) Offset Addressing Mode

대괄호 안에 레지스터 변수와 콤마와 offset이라는 특정 값을 적을 수 있다.

[<Rn>, <offset>] 계산을 하자면 Rn + offset 을 해서 어떤 값을 만드는데 이 값이 메모리 주소가 된다. offset 안써도 됨. Rn 에 들어있는 레지스터 값에 offset값을 더해서 값을 만들어내는데 이 값이 메모리 주소이다. 

이게 기본적인 offset 표현방법이고 LDR, STR 명령어로 해결한 예시가 밑에 나온다.

LDR R0 [R1, #4] → 만약 R1에 0x10000000 값이 들어 있었다면 R1, #4 는 0x10000004 가 된다. 0x10000004 메모리 주소에 만약 2라는 값이 들어 있다고 한다면 이 값을 복사해 R0 레지스터로 옮겨서 쓰라는 명령어가 된다.

### 2) Pre-indexed Addressing Mode

[<Rn>, <offset>]! → 괄호 뒤에 느낌표가 붙는다.

그리고 pre-indexed 이기에 addressing 을 하기 전에 index를 미리 바꾸어준다.

LDR R0, [R1, #offset]! 

R0에 [R1 + offset] 한 메모리 주소에 들어있는 값을 옮겨라(먼저 증기시킨 후 옮김!) 그리고 R1 값을 offset과 바꿔라.

for(i = 0; i < 10; i++)

B = A[i]............? // ++i 를 한 것과 마찬가지?

### 3) Post-indexed Addressing Mode

post indexed 는 이 값을 적용시킨 닫음 값을 증가시킨다.

[<Rn>], <offset>

LDR R0, [R1], #offset

R1의 메모리가 가리키는 주소의 값을 R0에 넣은 뒤 R1 = R1 + offset

** 약간씩 차이가 있으나 표현법이 조금씩 다르다!

---

예제1)

R0 = 0x00000000

R1 = 0x00009000

mem[0x00009000] = 0x01010101

mem[0x00009004] = 0x02020202

LDR R0, [R1, #4] 수행한 후 R0 값은 얼마고, R1 값은 얼마일까?

→ R0 = 0x02020202, R1 = 0x00009000

LDR R0, [R1, #4]!    ; preindex

→ R0 = [0x00009004], R1 = R1 + 4

→ R0 = 0x02020202, R1 = 0x00009004

LDR R0, [R1], #4  ; postindex

→ R0 = 0x01010101, R1 = 0x02020202

### Multiple load/store

아까 pre 나 post index를 하는 이유가, 이 기준점이 되는 base 주소값을 offset만큼 증가시켜주는 것을... 메모리에 여러 개의 word를 한 번에 한 번씩 LDR 나 STR 를 가지고 데이터를 옮길 수 있다.

그걸 이제 한 번에 여러 개의 데이터를 한 번에 옮길 수 있는 명령어가 있다.

그러한 명령어를 Multiple load/store (LDR) 라고 한다.

LDM 은 Load Multiple 이고 STM은 Store Multiply 이다.

LDR / STR 일 때 하나씩 옮긴다. LDM 이 되면 한 번에 여러 데이터를 몇 개의 레지스터에 넣을 수 있다.

메모리에 있을 때 이 데이터를 cpu의 레지스터 R0~R3 네 개의 주소가 주어진다면 주소를 연결지어놓은 후  그 다음 주소를 + 방향으로 증가시킬지 혹은 -방향으로 증가시킬지를 우리가 지정해줄 수 있다.

+방향 증가: increment (I), 감소: decrement (D).

A를 붙이면 After, postindex. 먼저 주소를 가져오고 난 다음 메모리의 주소 값을 증가시킴.

B를 붙이면 Before, preindex. 주소값을 먼저 증가시킨 후 값을 불러옴.

IA (increment after), IB (increment before), DA (decrement after), DB (decrement before)

이 앞에 LDM, STM 등이 올 수 있다.

---

예제2)

mem[0x80018] = 0x03

mem[0x80014] = 0x02

mem[0x80010] = 0x01

R0 = 0x80010

LDMIA R0!, {R1 - R3}

→ R1 에 R0가 가리키는 값을 옮긴 후 R0 = R0 + 4 를 실행한다.

→ R1 = 0x01, R0 = 0x80014

→ R2 = 0x02, R0 = 0x80018

→ R3 = 0x03, R0 = 0x8001C

이번 강의 시간에는 명령어 종류에 대해 - 데이터 이동, 데이터 프로세싱, 브랜칭 알아봄.

데이터 이동 종류에는 레지스터간 이동과 레지스터와 메모리간 이동이 있다. (후자가 더 복잡. 주소 값 활용... 이 때 흔히 base 와 offset 값 활용.)

## *2) Assembler Language: Processing Data*

그래서 오늘 강의는 instruction set 중에서 data를 processing하는데 arithmetic logic instruction에 대해 먼저 알아볼 것이고, 그 다음에 branch 명령어에 대해 공부해볼 것입니다. data를 연산하는 명령어에는 두 종류(arithmetic, logic)가 있습니다. 

### Arithmetic Operation Instructions

그 중 arithmetic 은 addition, subtraction, multiply, division..

ADD, SUB, MUL, DIV 등의 아리스메틱 명령어가 있습니다. 연산은 대체로 세 개의 operand가 있다.

예) ADD R0, R0, R1  ; R0 = R0 + R1

operand에는 register만 올 수 있다.

ARM instruction의 특징 두 가지(1. RISC → instruction이 제한적, 크기가 정해짐)2. load-store architecture → 데이터를 이동하는 명령어와 데이터를 연산하는 명령어를 확실하게 구분지어 놓음 → LDR STR 는 메모리 주소를 지칭하는 operand, ADD SUB 의 operand는 immediate값 혹은 register.)

모든 연산을 보면 Register 혹은 immediate 값이 operand이다.

ADD**S** → Suffix 접미사. S 가 붙으면 PSR (Program status register)에 결과에 대한상태를 update한다.  → 네 가지 경우 (overflow, carry, zero, negative)

MUL Rd, Rm ;두 개의 피연산자가 오면 Rd = Rd * Rm.

UDIV (Unsigned Division), SDIV (Signed Division)

### Examples of Arithmetic Instructions

source와 destination 이 같을 수 있다. immed가 올 수 있다.

ADC 는 Add with Carry. 캐리 값을 더해주어 연산을 하는 명령어이다.

SBC 는 Sub with Carry (=Borrow).

RSB 는 Reverse Subtract. RSB.W Rd, Rn, Rm  ; Rd = Rm - Rn

MUL 을 보면, 우리가 32비트 cpu를 사용하는데(모든 레지스터는 32비트 크기.) 32 bit + 32 bit → 최대 33 bit. 남은 한 비트 → 오버플로우가 발생! → PSR (Program Status Register) 에 오버플로우가 발생했다고 저장.

32 bit * 32bit → 최대 64 bit → overflow로 커버되지 않는다. 상위 32비트, 하위 32비트를 따로 저장. → MULL 명령어! (SMULL (signed), UMULL (unsigned)) 

SMULL RdLo, RdHi, Rn, Rm  ; {RdHi, RdLo} = Rn * Rm

여기까지가 Arithmetic 연산이었다. 그 다음에

### Logic Operation Instructions

논리적 연산. AND, OR, EOR, NOT → 비트 단위의 연산(bitwise) → 같은 자리의 비트끼리 논리연산.

AND, ORR, BIC(bit clear), EOR(exclusive or)

예를 들어, 

R0 0xFFFFFFFF

R1 0x0000FFFF

AND R1, R0 → R1 = 0x0000FFFF

ORR R1, R0 → R1 = 0xFFFFFFFF

BIC R0, R1 → ~R1 0xFFFF0000 해 R0와 AND →0xFFFF0000. 원래 R0에 있는 비트 중에서 R1에서 1을 가지고 있는 것만큼 0으로 clear 해주고, R1이 1이 아닌 곳의 비트는 그대로 통과시켜준다.

### Shift and Rotate Instructions

비트 단위로 오른쪽 혹은 왼쪽으로 몇 칸 이동시키는 연산을 하도록 명령어를 만들었다.  이때 칸을 옮기면서 생긴 빈 공간을 어떻게 채우느냐를 결정해주는 명령어를 나누었다.

ASR : Arithmetic Shift Right (산술적으로 오른쪽으로)

LSR : Logically Shift Right (논리적으로 오른쪽으로)

LSL : Logically Shift Left (논리적으로 왼쪽으로 . 산술적으로 왼쪽은 없음.)

+) Shift의 경우 빠지는 숫자들은 버려진다. 그런데 이를 버리지 않고 그대로 비는 공간에 가져나 넣는 연산은 Rotation 이라고 하며, 이 명령어에는 ROR (Rotation Right), ROL (Rotation Left) 가 있다.

이때, 캐리가 발생할 수 있는데, 캐리를 고려해서 Shift를 할 수가 있다.

정리를 하자면, 어떤 Register 가있을 경우 왼쪽으로 Shift를 할 수 있는  연산은 LSL 밖에 없다. 이 명령어를 사용하면 왼쪽의 비트가 빠지는데, 이 빠지는 것 중 가장 마지막에 빠지는 값이 Carry로 빠지고 오른쪽의 빈 곳에는 0이 채워진다.

Shift Right는 두 종류가 있는데 ,LSR를 하면 오른쪽으로 캐리가 빠지고 왼쪽의 빈 곳에는 0이 채워진다. ASR를 하면 원래 최상위권에 있던 값이 다시 채워진다.

ROR 을 하면 캐리와 상관없이 빠지는 비트가 그대로 빈 곳에 채워진다. 

로테이션에 캐리를 포함시키는 명령어도 따로 있다. ( RRX)

몇 가지만 정리하자면, 

Arithmetic - ADD SUB MULL DIV

Logical - AND ORR EOR BIC

Shift - LSL LSR ASR ROR 

이제 다음으로 Flow Control, 프로그램의 흐름을 제어하는 명령어들을 알아보도록 하겠습니다.

## *3-1) Assembler Language: Call and Unconditional Branch*

조건 없이 무조건 Branch가 일어나는 특징을 가지는 명령어

이 종류의 명령어는 B 밖에 없다. B, BX.

B 명령어를 쓰면 뒤에 올 수 있는 것은 label . 그리고 BX 뒤에는 Register 가 올 수 있다.

### Branch

Branch 는 Jump가 일어나는 것을 말한다. 일반적으로는 프로그램을 실행하면 그것이 순차적으로 실행되는데, Branch 명령어를 만나면 그 Label 또는 Register 에 해당하는 곳에 있는 명령어를 수행하도록 하여 프로그램의 실행 흐름을 바꾼다.

B, BX

BL, BLX

### Branch examples

B label → label로 바로 Jump. (BL : branch with link. (링크를 사용 → 프로그램을 실행하다가 b명령어 만나 label로 jump할 때 b 명령어 실행할 때 PC가 0x8이라고 할 때, label로 가도록 cpu가 PC 값에 label의 주소값인 0x18로 바꾸어준다. 그리고 쭉 계속 4씩 증가시키며 순차적으로 진행한다. 그 사이의 명령어를 수행하기 위해서는 다른 곳에서 다시 Jump를 하거나, 종료되는 개념이 있으면(BL) 다시 돌아와 수행한다. 이때 종료해서 돌아올 때 쓸 주소를 Link Register 에 저장해둔다. B는 이 돌아올 주소를 저장하지 않고, BL 은 돌아올 주소를 LR에 저장한다.))

BX reg → register 의 값으로 Branch.

B나 BX 는 PC 값만 update시킨다. BL, BLX 를 사용해야 LR 도 update 시켜준다.

BX 뒤에 label을 두는 것은 Cortex-M3에서는 불가능하다!!

+) Branch 명령어 사용하지 않고 Branch를 할 수 있다! PC 값을 다음 실행할 명령어의 메모리 주소  값으로 바꾸어주는 작업을 수동으로 해주면 된다! PC 는 R15이다.

MOV R15, R0 처럼 PC 값을 update해주어 우리가 원하는 branch를 할 수 있다.

## *3-2) Assembler Language: Combined Compare and Conditional Branch*

조건에 해당되면 Branch가 일어나는 특징을 가지는 명령어

CBZ, CBNZ 와 같이 명시된 조건을 따지는 명령어와, suffix(접미사)를 붙여 조건을 따지도록 하는 명령어가 있습니다.

CBZ 는 Compare and Branch Z 인데, 뒤의 것을 비교해 Branch. 

## Flags in ARM Processors

(A)PSR 에 연산 결과의 상태를 저장... N Z C V 가 있다.

Negative(음수 결과면 1), Zero(연산 결과 0이면 1) Carry (carry 발생하면 1) V (overflow 발생하면 1)

## Application Program Status Register (APSR)

## *4) Assembler Language: Use of Suffixes*

### Use of Suffixes

뒤에 S를 붙여주면 PSR 의 네 개 비트의 값에 업데이트를 시키라고 한다. 주로 ADD SUB MUL 등 data processing 명령어 뒤에 접미사로 붙는다.

그 외에 조건을 따지는 접미사는 굉장히 종류가 많다! (외울필요X)

### Updating the APSR

SUB

SUBS

ADD

ADDS

suffix S 가 붙어있으면 update !!!

### Use of Suffixes

CMP 는 연산의 결과를 status register 만 업데이트한다.

CMP R0, R1 를 하면 R0 - R1을 해서 0이면 Z를 1로 업데이트시킨다. (nzcv 모두 업데이트..)

ITTEE GT 에서 I는 if. GT는 조건. 이 조건이 TT는 두 개의 조건이 참일 경우... T는 한 개의 조건... EE 는 X. 이 조건과 맞지 않은 것을 찾음(??) GT 는 GREAT. Z flag 가 clear되고 N, V가 set되어있거나 N이 클리어되어있고 V가 클리어면...

LE 는 GT 의 반대. 

# Exercise: What is the value of r2 at done?

# Summary