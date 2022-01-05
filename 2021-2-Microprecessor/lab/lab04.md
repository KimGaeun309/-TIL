## Lab 4-1
* code

``` assembly
NAME    main
        
        PUBLIC  __iar_program_start
        
        SECTION .intvec : CODE (2)
        
__iar_program_start
        B       main

        
        SECTION .text : CODE (2)

main    
        LDR r0, =0xFFFFFFF7
        LDR r1, =0x7FFFFFFF
        MOV r2, #00001111b
        
        ASR r3, r0, #4 ; r3 = r0 >> 4 (Arithmetic shift right)
        ASR r4, r1, #4 ; r4 = r1 >> 4 (Arithmetic shift right)
        LSL r5, r2, #4 ; r5 = r2 << 4 (Logical shift left)
        LSR r6, r2, #4 ; r6 = r2 >> 4 ((Logical shift right)
        ROR r7, r2, #4 ; r7 = r2 rot by 4 (Rotate right)
        
        END

```

* 코드 설명

0xFFFFFFF7과 0x7FFFFFFF는 32비트이므로 LDR 명령어를 사용해 각각 레지스터 r0, r1에 저장해주고, 0000111b는 MOV 명령어를 사용해 r2에 저장해줍니다.
ASR는 Arithmetic Shift Right로, 이 명령어를 사용해 shift 해주면 기존의 MSB 값이 비는 자리에 채워지게 됩니다. 위 코드를 실행하면 r0을 4만큼 ASR 명령어를 사용해 오른쪽으로 shift한 결과를 r3에 저장하고, r1을 4만큼 ASR 명령어를 사용해 오른쪽으로 shift한 결과를 r4에 저장해줍니다.
LSL는 Logical Shift Left이고 LSR는 Logical Shift Right입니다. 이 명령어들을 사용해 shift 해주면 비는 자리에 0이 채워집니다. 위 코드를 실행하면 r2를 4만큼 LSL 명령어를 사용해 왼쪽으로 shift한 결과를 r5에 저장하고, r2를 4만큼 LSR 명령어를 사용해 오른쪽으로 shift한 결과를 r6에 저장합니다.
ROR은 Rotate Right로, 오른쪽으로 shift하면서 빠져나간 값을 비는 자리에 채웁니다. 위 코드를 실행하면 r2를 4만큼 ROR 명령어를 사용해 로테이션한 결과를 r7에 저장합니다.

* memory, register 분석

이번 실습에서 Memory의 변화는 없었습니다.
main의 첫 세 개의 명령어를 실행하면 r0에 0xFFFFFFF7, r1에 0x7FFFFFFF, r2에 00001111b (== 0x0000000F)의 값이 저장됩니다.
r0에 저장된 값은 이진수로 1111 1111 1111 1111 1111 1111 1111 0111 입니다.이 값을 4만큼 shift해 r3에 저장하는데 ASR 명령어를 사용하므로 본래의 MSB 값인 1이 빈 곳에 채워집니다. 따라서 r3에는 1111 1111 1111 1111 1111 1111 1111 1111 이 저장되며, 이는 16진수로 0xFFFFFFFF 입니다.
r1에 저장된 값은 이진수로 0111 1111 1111 1111 1111 1111 1111 1111 입니다. 이 값을 ASR 명령어를 사용해 4만큼 shift해 r4에 저장하면 빈 곳에 0이 채워집니다. 따라서 r4에는 0000 0111 1111 1111 1111 1111 1111 1111 이 저장되며, 이는 16진수로 0x07FFFFFF입니다.
LSL이나 LSR 명령어를 사용하면 빈 자리에 무조건 0이 채워집니다. 따라서 r5에 r2의 값인 0x0000000F를 4만큼 LSL 시킨 결과를 저장하면 0x000000F0 이 저장됩니다. 그리고 r6에 r2에 저장된 값을 4만큼 LSR 시킨 결과를 저장하면 0x00000000 이 저장됩니다.
ROR명령어를 사용하면 버려질 값들이 비는 공간에 채워지므로 r7에는 r2의 가장 오른쪽의 비트 네 개( 1111 )가 왼쪽에 채워진 결과인 0xF0000000 이 저장됩니다.


## Lab 4-2
* code

``` assembly
NAME    main
        
        PUBLIC  __iar_program_start
        
        SECTION .intvec : CODE (2)
        
__iar_program_start
        B       main

        
        SECTION .text : CODE (2)

main    
        MOV r0, #3
        MOV r1, #3
        MOV r2, #7
        MOV r3, #7
        MOV r4, #2
        MOV r5, #3
        MOV r6, #6
        MOV r7, #6
        MOV r8, #4
        MOV r9, #5
        
        LDR r10, =0x20000000
        
        STMIA r10!, {r0-r9}
        
        MOV r0, #3
        MOV r1, #2
        MOV r2, #8
        MOV r3, #5
        MOV r4, #2
        MOV r5, #3
        MOV r6, #4
        MOV r7, #6
        MOV r8, #3
        MOV r9, #5
        
        LDR r11, =0x20002000
        
        STMIA r11!, {r0-r9}
        
        bl Search+1
        
        LDR r12, =0x20000028
        
        STMIA r12!, {r2-r4}
        
        B end
        
Search
        LDR r10, =0x20000000
        LDR r11, =0x20002000
        MOV r0, #0
        MOV r1, #0
        MOV r2, #0
        MOV r3, #0
        MOV r4, #0
        MOV r5, #0
        
Loop
        LDR r0, [r10], #4
        LDR r1, [r11], #4
        
        
        CMP r0, r1
        
        ITTE GT
        ADDGT r2, r2, #1
        ADDGT r3, r3, #2
        ADDLE r4, r4, #1
        
        ADD r5, r5, #1
        CMP r5, #10

        BNE Loop
        
        MOV PC, LR
       
end
        
        END

```

* 코드 설명

Array1을 만들기 위해 MOV 명령어를 사용해 r0 ~ r9 에 Array1의 낮은 주소에 들어가야 하는 값부터 차례대로 저장해주고, LDR 명령어로 r10에 Array1이 시작되는 주소를 저장한 후, STMIA 명령어에 ! 를 같이 써서 r0 ~ r9에 저장된 값들을 r10 이 가리키는 주소에 하나씩 저장하고 r10이 가리키는 주소값을 증가시키기를 반복합니다. Array2도 이와 같은 방식으로 만듭니다.
bl 명령어를 사용해 서브루틴 ‘Search’로 branch 하고 링크 레지스터에 기존에 실행되고 있던 주소를 저장합니다.
‘Search’에서는 LDR 명령어를 사용해 r10과 r11에 각각 Array1과 Array2가 시작되는 주소를 저장하고, r1 ~ r0 를 MOV 명령어를 통해 초기화해준 뒤 Loop 를 실행합니다.
Loop에서는 r5에 1씩 더하고 r5가 10이 아니면 다시 Loop로 돌아가도록 하
여 그 사이의 명령어들이 열 번 반복되도록 하였습니다.
열 번 반복되는 명령어로는 r0와 r1에 r10과 r11에 든 메모리 주소의 값을 저
장한 후 r10과 r11에 저장된 주소를 4씩 증가시키는 post-indexed addressing
이 사용되었습니다. 그래서 CMP 명령어로 r0와 r1의 값을 비교하고 ITTE GT 
명령어를 사용해 r0가 r1보다 크다면 r2는 1만큼, r3는 2만큼 증가시키고, 그
렇지 않다면 r4를 1만큼 증가시키는 과정을 반복할 때마다 r0와 r1이 각각 
array의 다음 값을 저장하도록 하여 Array1과 Array2의 모든 값을 비교해보도
록 합니다.
반복을  빠져나온 후에는 PC에 LR이 저장하고 있는 branch 이전의 실행 주
소를 옮겨 되돌아갑니다. 돌아온 후에는  LDR 명령어와 STMIA 명령어를 사
용해 r2, r3, r4가 각각 메모리주소 0x20000028, 0x2000002C, 0x20000030 에 
저장되도록 한 후 b 명령어를 사용해 end로 branch 해주어 프로그램을 종료
합니다.

* register, memory 분석

Array1을 만들기 위해 쓴 명령어들을 직접 실행하면 r0부터 r9에 3, 3, 7, 7, 2, 3, 6, 6, 4, 5 라는 값들이 저장되는 모습을 볼 수 있습니다. r10에는 0x20000000 이 저장되었다가, STMIA 명령어가 실행되면서 r10이 가리키는 메모리 주소인 0x20000000에 r0의 값 3을 저장하고 r10의 주소를 4 증가시켜 0x20000004 에 r1의 값 3을 저장하기를 반복해 결과적으로 0x20000000부터 0x20000024 까지 r0 ~ r9의 값들이 저장되고 r10은 0x20000028을 가리키는 모습을 확인할 수 있습니다.
 
Array2도 Array1을 만들었던 것과 똑같은 과정을 거쳐 0x20002000 부터 0x20002024 까지의 주소에 r0 ~ r9에 저장해두었던 값들이 저장되고 r10은 0x20002028을 가리키는 것을 확인할 수 있습니다.
 
bl Search+1 이 실행되면 LR (링크 레지스터) 에 값이 설정되고 PC의 값이 바뀐 모습을 확인할 수 있습니다. 이때 저장된 값은 Search 로 branch 되기 전의 PC 값입니다.
 
Search 로 와서 처음으로 Loop의 명령어들이 실행되면, r10과 r11에 각각 0x20000000, 0x20002000 이 저장되고, r10과 r11이 가리키는 메모리 주소의 값이 r0, r1에 저장된 후 r10과 r11의 값이 4 증가되어 업데이트되는 모습을 확인할 수 있습니다. 
그리고 CMP 명령어를 실행하면 r0에서 r1를 빼기 연산을 하는데, 두 레지스터는 모두 3을 저장하고 있으므로 결과가 0이 되기 때문에 Z flag 는 1이 됩니다. 따라서 ITTE GT 를 실행하면 ADDGT 는 실행되지 않아 r2, r3 레지스터 값은 그대로 0 이고, ADDLE 가 실행되어 r4 레지스터 값이 1 증가되는 모습을 확인할 수 있습니다. 또 r5의 값이 1 커져 r5는 1을 저장하게 되는데, 이는 10보다 작으므로 CMP 명령어를 실행했을 때 Z flag는 0 이 되고, N flag가 1이 됩니다. 따라서 BNE Loop 명령어를 실행했을 때 다시 Loop로 돌아가게 됩니다.
 
위 과정을 열 번 반복해 Array1과 Array2의 원소들을  모두 비교하며 r2, r3, r4의 값을 업데이트시켜주면 r2는 4, r3는 8, r4는 6 을 저장합니다. 
 
그리고 MOV PC, LR 을 실행하면 LR에 저장되었던 ‘Search’라벨로 branch되기 전의 실행 주소가 PC에 저장되어 그 주소로 돌아가 계속해서 명령어를 실행합니다.
bl 명령어의 다음 줄에 적힌 LDR과 STMIA 명령어가 실행되어 메모리 0x20000028 에 r2의 값인 4, 0x2000002C 에 r3의 값인 8, 0x20000030 에 r4의 값인 6 이 저장되는 모습을 확인할 수 있습니다.
 
그 다음 줄에 있던 b end 명령어가 실행되면서 ‘end’ 라벨로 branch되어 PC 값이 
바뀌고 프로그램이 종료되는 모습을 확인할 수 있습니다.

