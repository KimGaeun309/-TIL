## Lab2-1 MOV, STR, LDR 사용
### 방법 1. offset addressing
* code
```assembly
NAME    main
        
        PUBLIC  __iar_program_start
        
        SECTION .intvec : CODE (2)
        
__iar_program_start
        B       main

        
        SECTION .text : CODE (2)
      
main
   ; 1. MOV 명령어를 사용해 값 1 ~ 4 를 R0 ~ R3 으로 가져오기 
        MOV R0, #1
        MOV R1, #2
        MOV R2, #3
        MOV R3, #4
        
   ; 2. MOV 명령어를 사용해 R4 가 0x20000000을 가리키도록 하기 
        MOV R4, #0x20000000

; 3. R0 ~ R3 에 저장된 값들을 R4가 가리키는 주소부터 메모리에 저장하기 
        STR R0, [R4, #0] ; offset addressing
        STR R1, [R4, #4]
        STR R2, [R4, #8]
        STR R3, [R4, #12]
        
   ; 4. 메모리 주소에 저장된 값들을 R5 ~ R8 으로 가져오기
        LDR R5, [R4, #0]
        LDR R6, [R4, #4]
        LDR R7, [R4, #8]
        LDR R8, [R4, #12]
        
        END
   
```

* register, memory 분석

1번을 실행하면 Register View에서 R0 에 1, R1에 2, R2에 3, R3에 4 가 차례로 저장되는 것을 확인할 수 있습니다.
2번을 실행하면 R4에 0x20000000 이 저장되는 모습을 확인할 수 있습니다.
3번을 실행하면 Memory View에서 R4가 가리키는 주소값인 0x20000000 에 #0, #4, #8, #12 가 각각 더해진 주소값에 해당하는 메모리에 R0, R1, R2, R3 에 저장된 값들이 차례로 저장되는 모습을 확인할 수 있습니다. (이때 R4에 저장된 주소값에는 변화가 없습니다.)
4번을 실행하면 R4 가 가리키는 주소값인 0x20000000 에 #0, #4, #8, #12 가 각각 더해진 주소가 가리키는 메모리에 저장된 값들이 R5, R6, R7, R8 에 차례로 저장되는 모습을 확인할 수 있습니다. (이때도 R4에 저장된 주소값에는 변화가 없습니다.)

### 방법 2. pre-offset addressing
* code
``` assembly

NAME    main
        
        PUBLIC  __iar_program_start
        
        SECTION .intvec : CODE (2)  
        
__iar_program_start
        B       main
        
        SECTION .text : CODE (2)
      
main
        ; 1. 값 1 ~ 4 를 R0 ~ R3 으로 가져오기 
        MOV R0, #1
        MOV R1, #2
        MOV R2, #3
        MOV R3, #4
        
        ; 2. R4 가 0x20000000을 가리키도록 하기 
        MOV R4, #0x20000000
 
       ; 3. R0 ~ R3 에 저장된 값들을 R4가 가리키는 주소부터 4씩 증가시키며 메모리에 저장하기 
        STR R0, [R4, #0]! ; pre-offset addressing
        STR R1, [R4, #4]! ; R4 에 0x20000004
        STR R2, [R4, #4]! ; R4 에 0x20000008
        STR R3, [R4, #4]! ; R4 에 0x2000000C
        
        ; R4가 가리키는 주소값을 다시 0x20000000으로 바꾸어주기 
        MOV R4, #0x20000000
        
        ; 4. 메모리 주소에 저장된 값들을 R5 ~ R8 으로 가져오기 
        LDR R5, [R4, #0]! 
        LDR R6, [R4, #4]! ; R4 에 0x20000004
        LDR R7, [R4, #4]! ; R4 에 0x20000008
        LDR R8, [R4, #4]! ; R4 에 0x2000000C
        
        END


```
* register, memory 분석

방법 1과 다른 점은 3번과 4번에서 pre-offset addressing 을 사용해 R4가 가리키는 주소를 바꾼 후 값을 저장한다는 점입니다.
예를 들어, 3번 첫 줄을 실행하면 R4에 저장된 0x20000000 에 #0 을 더해 저장하고 R4가 가리키는 메모리 주소에 R0 에 저장된 값을 저장합니다. 둘째줄을 실행하면 R4에 저장된 0x20000000 에 #4 를 더한 0x20000004 가 저장되고 그 주소에 해당하는 곳에 R1 에 저장된 값을 저장합니다. 
이때 3번을 실행하면서 R4가 가리키는 주소 값이 0x2000000C 로 변하였으므로 4번을 실행하기 전에 R4가 가리키는 주소 값을 다시 0x20000000 으로 바꾸어주어야 제대로 실행됩니다.

### 방법 3. post-offset addressing
* code
``` assembly

NAME    main
        
        PUBLIC  __iar_program_start
        
        SECTION .intvec : CODE (2)
    
        
__iar_program_start
        B       main

        
        SECTION .text : CODE (2)
      
main
        ; 값 1 ~ 4 를 R0 ~ R3 으로 가져오기 
        MOV R0, #1
        MOV R1, #2
        MOV R2, #3
        MOV R3, #4
        
        ; R4 가 0x20000000을 가리키도록 하기 
        MOV R4, #0x20000000
 
       ; R0 ~ R3 에 저장된 값들을 R4가 가리키는 주소부터 4씩 증가시키며 메모리에 저장하기 
        STR R0, [R4], #4 ; post-offset addressing
        STR R1, [R4], #4 ; R4 에 0x20000004
        STR R2, [R4], #4 ; R4 에 0x20000008
        STR R3, [R4], #4 ; R4 에 0x2000000C
                         ; R4 에 0x20000010
        
        ; R4가 가리키는 주소값을 다시 0x20000000으로 바꾸어주기 
        MOV R4, #0x20000000
        
        ; 메모리 주소에 저장된 값들을 R5 ~ R8 으로 가져오기 
        LDR R5, [R4], #4 
        LDR R6, [R4], #4 ; R4 에 0x20000004
        LDR R7, [R4], #4 ; R4 에 0x20000008
        LDR R8, [R4], #4 ; R4 에 0x2000000C
                         ; R4 에 0x20000010
        
        

        END


```

* register, memory 분석

방법3에서는 post-offset addressing 을 사용해 값을 저장한 후 R4가 가리키는 주소를 바꿉니다.
예를 들어, 3번 첫째줄을 실행하면 R0 에 R4가 가리키는 0x20000000 에 저장된 값이 저장되고, R4 는 #4를 더한 0x20000004 를 가리키도록 합니다.
3번을 다 실행하고 나면 R4에는 0x20000010 이 저장되어있는데, R4가 다시 0x20000000 을 가리키도록 해야 4번이 제대로 실행됩니다.

## Lab 2-2 MOV, STM, LDM 사용
### 방법 1. STMIA, LDMIA
* code

``` assembly
NAME    main
        
        PUBLIC  __iar_program_start
        
        SECTION .intvec : CODE (2)
        
__iar_program_start
        B       main
        
        SECTION .text : CODE (2)
      
main
        ; 1. 값 1 ~ 4 를 R0 ~ R3 으로 가져오기 
        MOV R0, #1
        MOV R1, #2
        MOV R2, #3
        MOV R3, #4
        
        ; 2. R4 가 0x20000000을 가리키도록 하기 
        MOV R4, #0x20000000
 
       ; 3. R0 ~ R3 에 저장된 값들을 R4가 가리키는 주소부터 4씩 증가시키며 메모리에 저장하기 
        STMIA R4!, {R0, R1, R2, R3}
        
        ; R4가 가리키는 주소값을 다시 0x20000000으로 바꾸어주기 
        MOV R4, #0x20000000
        
        ; 4. 메모리 주소에 저장된 값들을 R5 ~ R8 으로 가져오기 
        LDMIA R4!, {R5, R6, R7, R8}
        
        

        END

```
* register, memory 분석

Lab 2-1 과 다른 점은 STR, LDR 대신 STM, LDM 을 사용해 한 번에 여러 값을 가져오거나 저장하여 코드가 간결해졌다는 점입니다.
예를 들면 3번에서 STMIA 를 사용하면 R0에 저장된 값을 R4가 가리키는 주소 값(0x20000000)에 저장한 후 R4가 가리키는 주소 증가시키고, R1에 저장된 값을 R4가 가리키는 주소 값(0x20000004) 에 저장하기를 반복합니다.
3번을 실행하고 나면 R4가 가리키는 주소 값이 0x20000010 이 되었으므로 다시 0x20000000 으로 바꾸어주어야 합니다. 
그리고 4번에서는 LDMIA 를 사용하는데 R4가 가리키는 메모리 주소(0x20000000)에 저장된 값을 R5에 저장한 후 R4가 가리키는 메모리 주소 값을 증가시키고, R4가 가리키는 메모리 주소(0x20000004)에 저장된 값을 R6에 저장하기를 반복합니다. 4번을 실행하고 나면 R4는 0x20000010 을 가리킵니다.

### 방법 2. STMIA, LDMDB

* code

``` assembly
NAME    main
        
        PUBLIC  __iar_program_start
        
        SECTION .intvec : CODE (2)
    
        
__iar_program_start
        B       main
        
        SECTION .text : CODE (2)
      
main
        ; 1. 값 1 ~ 4 를 R0 ~ R3 으로 가져오기 
        MOV R0, #1
        MOV R1, #2
        MOV R2, #3
        MOV R3, #4
        
        ; 2. R4 가 0x20000000을 가리키도록 하기 
        MOV R4, #0x20000000
 
       ; 3. R0 ~ R3 에 저장된 값들을 R4가 가리키는 주소부터 4씩 증가시키며 메모리에 저장하기 
        STMIA R4!, {R0, R1, R2, R3}
        ; R4 에 0x20000010 저장됨 
        
        ; 4. 메모리 주소에 저장된 값들을 R5 ~ R8 으로 가져오기 
        LDMDB R4!, {R8, R7, R6, R5}
        
        END

```
* register, memory 분석

방법2에서는 3번 실행 후 R4가 가리키는 주소를 바꾸지 않고 LDMDB를 사용해 R8, R7, R6, R5 순서대로 메모리 주소에 저장된 값을 레지스터로 로드합니다.
4번이 실행되면 R4에 저장된 0x20000010 를 감소시켜 다시 저장한 후 그 주소(0x2000000C) 에 저장된 값을 R8에 저장하고, R4의 주소를 다시 감소한 후 그 주소(0x20000008)에 저장된 값을 R7에 저장하기를 반복합니다.
4번이 완전히 실행된 후에는 R4에 0x20000000 이 저장되어 있습니다.
