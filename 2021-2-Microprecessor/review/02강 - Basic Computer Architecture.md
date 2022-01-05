# 2강 - Basic Computer Architecture

## Organization of Computers

마이크로프로세서가 컴퓨터 구조 시스템의 핵심 소자이다.

CPU를 일반적으로 나누면 PC(personal computer)에 들어가는 범용 목적의(General Purpose) CPU(microprocessor)와 그 외의 tv, 냉장고 등과 같은 특수목적을 위한 마이크로프로세서들이 있다. 

CPU는 데이터를 실행하는, 작업을 처리하는 장치.

메모리는 CPU가 처리한 데이터를 담고 있는 장치.

Input/Output 장치는 모니터, 터치패드, usb 등과 같은 장치들.

컴퓨터시스템에서는 cpu가 마스터가 나머지는 슬레이브 입장이다.

CPU가 중심이고 마스터이다. Bus(기기와 기기를 연결시키는 개념의 선. 컨트롤러를 포함한.)에는 Address Bus, Data Bus, Control Bus 가 있는데, 이들은 각각의 기기에 연결되어있고, 값을 내보내는 원인과 방식이 서로 다르다. 

여러가지 데이터 핀들을 이용해 디바이스들을 연결.

어디로 데이터를 보낼지 선택해야함. 어떤 것을 선택학지를 지정해야 함. 즉 주소를 지정해야 함. 이 때 address bus 사용. address bus는 cpu가 지정할 수 있는 숫자를 정한다. 8bit 마이크로프로세서면 여덟자리 이진수 표현. 0x0 ~ 0xFF. 32bit면 0x0 ~ 0xFFFFFFFF. 논리적으로 각각 ram, rom 등에 연결되도록 address bus에 주소를 실어준다. address bus로 어떤 장치를 지정했으면 데이터를 주고받는다. 데이터를 주고받기 위해 data bus가 사용된다. control bus는 반응 신호를 통해 write or read 할 수 있게 한다. 제어신호. 

결론: cpu와 주변 장치들을 묶어서 하나의 마이크로 프로세서 시스템을 만들 수 있다. 

예전엔 cpu 자체만 가지고 마이크로 프로세서라고 했었음. 나머지(ram rom 등)는 별도의 장치로 만들어서 연결되는 것으로 간주. 

또는 cpu, ram, rom 등을 모아 칩 하나에 모든 시스템을 연결시킨 것을 두고 Microcontroller라는 이름을 붙이기도 했다. 요즘은 이처럼 칩 안에 시스템을 다 연결시켜 하나로 만드는 방식이 더 자주 쓰인다.

## What is the ARM Cortex-M3 Processor

우리가 사용하는 칩의 기본적 구조와 어떻게 그 구조 위에서 소프트웨어를 돌릴 수 있는지를 이해해야 마이크로프로세서를 이해하고 응용할 소프트웨어를 작성할 수 있다.

cortex는 코드명이다.

Exynos, 스냅드래곤은 AP.. 스마트폰에 들어가는 프로세서 이름. 이런 프로세서에 ARM계열의 cortex가 코어로 쓰인다(?)

ARM Cortex-M3라는 이름의 마이크로 프로세서라고 이해하자.

ARM이라는 회사(정확히는 계열)의 CPU 코어인 Cortex-M3는 32-bit microprocessor! (32비트 동시 연산, 주소 체계가 32비트) 이고 장점으로는효율성, ... 등이 있다!

M3의 M은 micro. 저사양용 프로세서다...

## Background of ARM

1990년도에 ARM 설립.

cpu가 복잡한 명령어로 설계되면 CISC, 간단한 명령어의 조합으로 설계되면 RISC(reduced instruction set computer, 명령어 집합)

ARM은 RICK 기반의 CPU이다.

## The Evolution of ARM Processor Architecture

현재 마이크로 프로세서 시장은 모바일.엠베디드 시장과 pc.서버 시장으로 나뉨. 모바일.엠베디드 시장은 주로 ARM이, pc.서버 시장은 주로 Intel이 독점하고 있다.

## ARM is the big player

ARM은 전세계 모바일의 90퍼센트 이상. 스마트폰은 100프로 ARM 코어 기반이다.  삼성 칩은 엑시노스와 스냅드래곤 둘 다 쓴다. 갤럭시S20은 유럽형엔 엑시노스, 우리나라와 중국 등에는 스냅드래곤이 들어간다.  스마트 티비 등도 ARM 기반. 

## Cortex-M3 Processor Applications

1. 저사양 칩은 상대적으로 간단하게 설계된만큼 제조하는데 비용이 적게 든다.
2. 자동차에도 쓰인다. 브레이크 제어장치, 창문 열고닫기, 의자 움직이기 등
3. Data communication. 데이터 통신장치, 블루투스 동글, usb 스틱
4. Industrial control
5. Consumer 

## ARM RISC Design Philosophy

instruction  set (명령어 집합. 이 cpu가 실행할 수 있는.) 들을 알아야 해당 프로세서에 맞는 프로그램을 작성할 수 있다.

instruction set를 배우고 이것이 microprocessor에 응용되는 것을 배우고 실제로 명령어를 이용해 프로그램을 작성하는 법을 배울 것.

ARM 계열의 명령어에 대한 기본 철학이 있다.

1. fixed size: 32-bit (동일한 크기로 되어있다!)
2. Load-store architecture로 되어 있다.

memory에 데이터가 올라가는데 cpu가 연산을 할 때 메모리로부터 데이터를 가져오는 작업이 필요하다(Load 작업). 또 연산을 한 다음 그 결과 데이터를 다시 메모리로 이동시켜 저장시키는 작업이 필요하다(Store 작업).

## ARM Core Data Flow Model

cpu 구조

![Untitled](2%E1%84%80%E1%85%A1%E1%86%BC%20-%20Basic%20Computer%20Architecture%207ed69dd32db5435c8aeface9479343e8/Untitled.png)

이렇게 만들어진 cpu는 우리가 프로그램을 작성하는 

## ARM instructions

크게 세 가지 부류

1. 연산 명령어
2. 이동 명령어
3. 흐름제어 명령어 (조건, 반복)

이번 시간에는 마이크로프로세서가 뭐고, 컴퓨터 시스템에서 마이크로프로세서가 차지하는 위치,  그 기본 원리가 되는 명령어, 기본적으로 명령어 기반의 코어가 돌아가는 방식을 알아보았다.