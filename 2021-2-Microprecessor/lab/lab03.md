## Lab 3-1 ADD, ADDS, SUB, SUBS, SMULL, UMULL
* code

``` assembly
NAME    main
        PUBLIC  __iar_program_start
        SECTION .intvec : CODE (2)
__iar_program_start
        B       main
SECTION .text : CODE (2)
main
        MOV R0, #0x00001234  ; R0 = 0x00001234
        MOV R1, #0x00004567  ; R1 = 0x00004567
        MOV R2, #0xFFFFFFFF   ; R2 = 0xFFFFFFFF
        MOV R3, #0x00000002  ; R3 = 0x00000002
        
      ; S suffix -> APSR 변할 수 있음  
        ADD R4, R0, R1  ; R4 = R0 + R1 
        ADDS R4, R0, R1 
        
        ADD R5, R2, R3  ; R5 = R2 + R3
        ADDS R5, R2, R3  
        ; Carry 발생 확인 가능!
       
        SUB R4, R0, R1  ; R4 = R0 - R1
        SUBS R4, R0, R1  
        ; Negative 발생 확인 가능!
        
        SUB R5, R2, R3  ; R5 = R2 - R3
        SUBS R5, R2, R3  
        ; Negative 와 Carry 발생 확인 가능! (음수 - 양수)
        
      ; SMULL 과 UMULL
        SMULL R7, R6, R0, R2  ; R6R7 = R0 * R2
        UMULL R7, R6, R0, R2  
        
        SMULL R9, R8, R1, R3  ; R8R9 = R1 * R3
        UMULL R9, R8, R1, R3
        
        END

```

* 실행 결과

ADD R4, R0, R1    
ADDS R4, R0, R1    
-> 위 두 코드의 실행 결과는 같습니다. R0와 R1을 더해도 Carry나 Negative가 발생하지 않기 때문입니다.
 
ADD R5, R2, R3    
ADDS R5, R2, R3 ; Carry 발생    
-> 위 두 코드의 경우 실행 결과에 차이가 있습니다. R2와 R3를 더할 시 오버플로우가 발생하며 Carry가 생겨나는데, ADD 명령어는 Carry를 저장하지 않고, ADDS 명령어는 APSR flag에 Carry를 저장하기 때문입니다.
 
SUB R4, R0, R1    
SUBS R4, R0, R1 ; Negative 발생    
-> 위 두 코드의 경우에도 실행 결과에 차이가 있습니다. R0에서 R1을 빼면 결과값이 마이너스가 되는데, SUB 명령어는 Negative가 발생했음을 따로 저장하지 않고, SUBS 명령어는 APSR flag에 저장하기 때문입니다.
 
SUB R5, R2, R3    
SUBS R5, R2, R3 ; Negative, Carry 발생    
-> 위 코드의 경우에는 SUBS … 를 실행했을 때 Negative와 Carry가 모두 발생합니다. 결과값이 음수이며, 음수(R2, 0xFFFFFFFFF) 에서 양수(R3, 0x00000002) 를 빼면서 오버플로우가 발생했기 때문입니다.
 
SMULL R7, R6, R0, R2    
-> SMULL 은 곱한 값을 부호를 가지는 변수(signed value)로 저장합니다.
 

UMULL R7, R6, R0, R2

->	이 코드의 실행결과를 보면 SMULL로 같은 값을 곱해 저장한 코드의 실행결과보다 더 작은 값이 저장된 것을 확인할 수 있습니다. 그 이유는 UMULL 은 SMULL 과 다르게  곱한 값을 부호가 없는 변수(unsigned value)로 저장하는데, unsigned value의 경우 부호를 저장하는 비트가 필요하지 않으므로 signed value에 비해 더 큰 정수값을 저장할 수 있기 때문입니다.
 
SMULL R9, R8, R1, R3    
UMULL R9, R8, R1, R3    
-> 위 두 코드의 실행결과는 같은 것처럼 보여집니다. R1과 R3에 저장된 값들의 곱은 부호 비트까지 사용하지 않아도 충분히 저장할 수 있어서 SMULL 명령어를 사용하나 UMULL 명령어를 사용하나 저장되는 값이 같기 때문입니다.
 
## Lab 3-2 SUM
* code

``` assembly
NAME    main
PUBLIC  __iar_program_start
SECTION .intvec : CODE (2)
__iar_program_start
        B       main
SECTION .text : CODE (2)
main
     ; 1부터 10까지의 정수를 모두 더해 r10에 그 결과를 저장

        MOV R0, #0  ; 1부터 10까지 계속 커져 합에 더해질 변수
        MOV R1, #0  ; 합 저장하는 변수
        
      ; 반복문
here  ; 돌아올 곳(label)
        ADD R0, R0, #1  ; R0 = R0 + 1
        ADD R1, R1, R0  ; R1 = R1 + R0
        CMP R0, #10 ; R0에 저장된 값과 10을 비교. 같으면 Zero가 1, 같지 않으면 Negative가 1.
        BNE here   ; 위의 비교 결과가 같지 않으면 here1로 돌아감
     ; while (R0 != 10) 과 비슷하게 동작
        
        MOV R10, R1  ; R10 = R1
        END

```

* 실행 결과

이 코드를 실행하면         
-> R0 에 저장된 값 1이 R1에 더해져 R1에도 1이 저장됩니다.

이때 CMP R0, #10 이 거짓이므로 Negative가 1로 변합니다. (Zero에 저장된 값은 변하지 않습니다.)        
-> 그러므로 BNE here 코드를 실행했을 때 here로 되돌아가 다시 ADD R0, #1 코드를 실행합니다.        
-> R0에 R0와 1을 더한 값을 저장하면 R0에 2가 저장됩니다.        
-> R1에는 R1에 R0를 더한 값이 저장되므로 1 + 2 = 3이 저장됩니다.        
-> 또다시 CMP … 와 BNE … 코드가 실행되면 이번에도 R0에 10이 저장되지 않았으므로 here로 돌아가게 됩니다.         
-> 위의 동작들이 반복되다가 R0에 0x0000000A (= 10) 의 값이 저장되면 CMP … 코드를 실행했을 때 APSR flag의 Z flag가 1로 변합니다.         
-> 따라서 코드는 루프에서 빠져나와 MOV R10, R1 을 실행해 R10에 1부터 10까지의 수를 모두 더한 결과값인 0x00000037이 저장됩니다.    
 
## Lab 3-3 Count number of 0 or 1
* code

``` assembly
NAME    main

PUBLIC  __iar_program_start
        SECTION .intvec : CODE (2)

__iar_program_start

        B       main
        SECTION .text : CODE (2)


main
       ; 32비트의 값을 MOV 명령어로 옮기려고 하면 error가 발생할 수 있기 때문에 LDR 사용.
        LDR R0, =0xF0F0F0F0  
; R0 = 0xF0F0F0F0 (= 1111 0000 1111 0000 1111 0000 1111 0000)
        LDR R1, =0x12345678  
; R1 = 0x12345678 (= 0001 0010 0011 0100 0101 0110 0111 1000)
  
        MOV R2, #1   ; R2 = 1, R3 = 32  
        MOV R3, #32  ; 32번 반복해주기 위한 조건 확인에 사용할 변수.

here1

        AND R4, R0, R2  ; R4 = R0 and R2
        CMP R4, #1    
        BNE jmp1   ; R4 != 1 면 jmp1 로 건너뜀.
        ADD R9, R9, #1  ;  R9 = R9 + 1 (R0의 1의 개수 저장됨)
        
jmp1
        LSR R0, R0, #1  ; R0의 비트를 하나씩 오른쪽으로 Shift
        SUBS R3, R3, #1 ; R3 = R3 - 1. R3가 0이 되는 순간 Z flag가 1이 된다.
        BNE here1       ; 32번 루프가 돌아 R3가 0이 되기 전까지는 here1로 돌아간다.

        MOV R3, #32  ; R3의 값이 0이 되었으므로 다시 32를 저장해 반복 조건 확인에 사용.
        
here2        
        AND R5, R1, R2  ; R4 = R1 and R2
        CMP R5, #0
        BNE jmp2  ; R5 != 0 이면 jmp2로 건너뜀.
        ADD R10, R10, #1  ; R10 = R10 + 1 (R1의 0의 개수 저장됨)
jmp2
        LSR R1, R1, #1  ; R1의 비트를 하나씩 오른쪽으로 Shift
        SUBS R3, R3, #1 ; R3 = R3 + 1. R3가 0이 되는 순간 Z flag가 1이 된다.
        BNE here2       ; 루프가 32번 돌아 R3가 0이 되기 전까지는 here2로 되돌아간다.  
            

        END


```
* 실행 결과

```
LDR R0, =0xF0F0F0F0
LDR R1, =0x12345678  
```
-> 32비트 값은 MOV 명령어로 저장하면 에러가 발생할 수 있기 때문에 LDR 명령어로 처리해 R0에 0xF0F0F0F0 (이진수로는 111100001111100001111000011110000)을, R1에 0x0x12345678 (이진수로는 00010010001101000101011001111000)을 저장해줍니다.

```
MOV R2, #1 
MOV R3, #32  
```
-> R2에는 1을, R3에는 32를 저장해줍니다. Register View 를 보면, R2에 0x00000001, R3에 0x00000020 (= 십진수로 32) 이 저장된 것을 확인할 수 있습니다.
 
```
here1
        AND R4, R0, R2  
        CMP R4, #1    
        BNE jmp1   
        ADD R9, R9, #1
```
-> R2에 미리 저장해둔 1과 R0를 and 연산을 한 값을 R4에 저장해줍니다. R4에 저장된 값이 1이면 R0의 마지막 비트가 1이라는 뜻입니다. R0에 저장된 값은 이진수로 1111 0000 1111 0000 1111 0000 1111 0000 이기 때문에 이 반복이 처음 이루어질 때 R4에는 0이 저장됩니다. 따라서 CMP R4, #1 이 실행되면 N flag 는 1이 되고, Z flag는 그대로 0입니다. BNE jmp1 은 Z가 1이 아니면 jmp1로 건너뛴다는 명령어입니다. 이때 Z가 0이므로 jmp1로 건너뛰게 됩니다. 건너뛰면서 ADD R9, R9, #1 코드가 실행되지 않아 R9의 값이 증가되지 않은 것을 확인할 수 있습니다.
 
 ```
jmp1
        LSR R0, R0, #1 
        SUBS R3, R3, #1 
        BNE here1
```
-> 이 명령어들을 실행하면 R0에 원래 저장되었던 값 0xF0F0F0F0 이 0x78787878 로 변하고, R3에 저장되었던 값 0x00000020이 감소되어 0x0000001F 로 변하는 것을 확인할 수 있습니다. 또 R3에 저장된 값이 0이 아니므로 Z flag는 0이고, here1 로 돌아갑니다.    
-> 위 과정을 네 번 반복하면 R0 의 마지막 비트가 1이 됩니다. 따라서 R4에는 1이 저장되고, CMP … 실행 후에 Z flag 가 1이 됩니다. 아래 실행 화면을 보면 ADD 명령어가 실행되어 R9 의 값이 증가된 모습을 확인할 수 있습니다.      
-> 이 과정은 R3 가 0이 될 때까지 총 32번 반복됩니다. 아래 실행화면을 보면 32번 실행시켜 R3가 0x00000000이 되어 Z flag가 1이 되었고 반복문을 빠져나온 것을 확인할 수 있습니다. 이때 R9에는 0x00000010 , 십진수로 16이 저장되어있습니다. R0에 처음 저장했던 값의 이진수가 11110000111100001111000011110000 이었으므로 R0의 1의 개수는 16개가 맞습니다.     
-> R9에 R0의 1의 개수를 세어 저장하는 코드가 잘 작성되었음을 알 수 있습니다.    

```
MOV R3, #32  

here2        
        AND R5, R1, R2  
        CMP R5, #0
        BNE jmp2  
        ADD R10, R10, #1  
jmp2
        LSR R1, R1, #1  
        SUBS R3, R3, #1 .
        BNE here2 
```
-> R1의 0의 개수를 R10에 저장하는 경우도 비슷하지만 R3에 0x00000000이 저장되어있으므로 다시 32를 저장해줍니다.    
-> R0의 1의 개수를 세는 경우와 다른 점은 R1과 R2를 and 연산한 값을 R5에 저장하고, R5에 0이 저장되지 않은 경우 jmp2로 건너뛴다는 점입니다. 아래 실행화면을 보면, R5에 0이 저장되어있어 Z flag가 1이 되어 건너뛰지 않고 ADD가 실행되어 R10의 값이 증가된 것을 확인할 수 있습니다.          
-> R0의 1의 개수를 세는 코드와 마찬가지로 32번 반복하면 루프를 빠져나옵니다. 이때 R10에 0x13이 저장되어있는 모습을 볼 수 있습니다. 0x12345678 은 이진수로 00010010001101000101011001111000 이므로, R1의 0의 개수는 십진수로 19개, 16진수로 0x13개가 맞습니다.    
-> 따라서 R10에 R1의 0의 개수를 세어 저장하는 코드도 잘 작성되었음을 알 수 있습니다
 

