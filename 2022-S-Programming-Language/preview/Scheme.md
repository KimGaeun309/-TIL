# Scheme

- 컴파일 환경
    
    [C, C++, Java, Python, PHP Online Compliers, Terminals and Editors](https://www.tutorialspoint.com/codingground.htm)
    
    [JDoodle - free Online Compiler, Editor for Java, C/C++, etc](https://www.jdoodle.com/)
    

### 1. 식

```scheme
> (+ 1 3) ;; 전위 표기법. 이는 1과 3을 +하는 의미
Value: 4

> (* (+ 2 4) (- 6 2)) ;; (2 + 4) * (6 - 2)
Value: 24

(1 3 5) ;; 오류. 평가를 시도하기 때문

> (quote(1 3 5)) ;; quote를 사용하여 평가를 막을 수 있음
Value: (1 3 5)

'(1 3 5) ;;  ' 는 quote를 축약한 표현.
```

### 2. 정의 함수

```scheme
(define (square x) (* x x))

> (square 5)
Value: 25

;;__________________________________

(define pi 3.24259265)
(define (square x) (* x x))
(define (circlearea radius)
		(* pi (square radius)))

> (circlearea 5)
Value: 78.53981625

;;__________________________________

(lambda (x) (* x x)) ;; x의 제곱을 반환하는 무명 함수

((lambda (x) (* x x)) 5) ;; 25를 반환하는 무명함수

(define square (lambda (x) (* x x))) ;; square라는 이름을 부여. 
;; (define (square x) (* x x)) 와 같은 의미.

;;__________________________________

(let ((x 7) (y 10)) (+ x y)) ;; 7에 x라는 이름이, 10에 y라는 이름이 임시로 바인딩,
														 ;; let 본체에 해당하는 식인 (+ x y) 에서 x와 y라는 이름이 사용됨

>x        ... 오류 ;; let 영역을 벗어나면 이름이 유지되지 않음
```

### 3. 입출력 함수

```scheme
;; Scheme 인터프리터는 식을 만나면 '읽기-평가-쓰기' 를 하여 평가한 결과를 출력한다.

> (+ 2 3) ;; 식을 읽고 평가한 결과인 5를 출력
Value: 5

> (display 21) ;; 평가 결과에 대한 출력 말고, 단순히 인자를 출력하는 display 함수
 21

> (display "hello")
hello

> (define x 21) ;; 21로 x를 정의
Value: x
> (display x) ;; x를 출력
21 ;; x의 값이 출력됨

> (read)   ;; read 함수는 키보드에서 친 내용을 그대로 반환.
123      ... 입력
Value: 123

> (define x (read)) ;; 키보드에서 입력한 내용인 7을 x의 값으로 정의하고, x의 값을 출력한다.
7      ... 입력
Value: 7
> x
Value: 7
```

### 4. 리스트 함수

```scheme
> (car '(1 3 5))  ;; car는 리스트의 첫 번째 원자를 반환하는 함수.
Value: 1

> (car '((1 3) 5 7)) ;; 첫 번째 원자는 (1 3)
Value: (1 3)

> (car 1)    ... 오류 ;; 1이 리스트가 아니므로 오류 발생

> (cdr '((1 3) 5 7) ;; cdr은 car를 제거한 후 나머지를 반환합니다.
Value: (5 7)

> (cdr 1)    ... 오류 ;; 1이 리스트가 아니므로 오류 발생

> (define (second lst) (car (cdr lst)))  ;; second 함수로 정의한 예, 인자 1st의 cdr의 car,
Value: second                                ;; 즉, lst의 두 번째 원자를 구하는 함수이다.

> (second '(1 3 5)) ;; 정의한 후에 다음과 같이 실행하면 우선 cdr '(1 3 5) 에 의해 (3 5)가 되고,
Value: 3                   ;; car '(3 5) 에 의해 3이 반환된다. 결국 두번째 원자인 3이 반환된다.

> (cons 1 ' (2 3))  ;; cons는 첫 번째 인자를 두 번째 인자의 새로운 car로 삽입한다.
Value: (1 2 3)

> (define lst '(2 3 4)) ;; 다음은 (2 3 4) 로 정의된 lst에
Value: lst
> (cons 1 lst)  ;; 1 을 새로운 car로 삽입하는 예이다.
Value: (1 2 3 4)

> (list 1 2 3) ;; lst는 여러 개의 원자를 리스트로 만드는 함수이다.
Value: (1 2 3)

> (list '(1 2) '(3 4)) ;; 다음은 (1 2)와 (3 4) 를 리스트로 만드는 에이다.
Value: ((1 2) (3 4)) 
```

### 5. 술어 함수

```scheme
> (define x 11)  ;; x를 11로 정의
Value: x

> (= x 11)  ;; 11로 정의된 x가 11과 같으므로 #t가 반환된다.
 Value: #t

> (> x 11)  ;; x가 11보다 크지 않으므로 거짓을 의미하는 ()가 반환됨.
Value: ()
> (< x 15) ;; x가 15보다 작으므로 #t가 반환됨
Value: #t

> (even? x) ;; x가 짝수가 아니므로 거짓을 의미하는 () 가 반환됨
Value: ()
> (odd? x) ;; x가 홀수이므로 #t 가 반횐됨
Value: #t

> (define y 0)  ;; y를 0으로 정의
Value: y
> (zero? y) ;; y가 0이므로 #t가 반환됨
Value: #t

> (null? '()) ;; ()는 공 리스트이므로 #t 가 반환됨
Value: #t
> (null? '(1 3)) ;; (1 3)은 공 리스트가 아니므로 () 가 반환됨
Value: ()

> (list? '(1 3)) ;; (1 3)은 리스트이므로 #t가 반환됨
Value: #t
> (list? '1) ;; 1은 리스트가 아니므로 ()가 반환됨 
Value: ()
> (list? '()) ;; ()는 리스트이므로 #t가 반환됨.
Value: #t
```

### 6. 제어

```scheme
;; 조건 구조 : if 함수와 cond 함수 
;; if 함수의 형식 : (if  조건 식1 식2) ; 조건이 참이면 식1을, 거짓이면 식2를 실행

> (if (> 3 2) 'yes 'no) ; (> 3 2) 가 참이므로 'yes' 가 반환됨
Value: yes

> (define x 7)
> (define y 10)
> (if (> x y) ; x보다 y가 크므로 (- y x) 가 실행되어 3이 반환됨
		(- x y)
		(- y x)) ; 
Value: 3

> (define (test x) ;; test는 인자 x가 70보다 크거나 같으면 'pass'를 출력하고
		(if (>= x 70)                        ;; 그렇지 않으면 'fail'을 출력한다.
			(display "pass")
			(display "fail"))
	)
> (test 75) ;; 75는 70 이상이므로 'pass'가 출력된다.
pass

> (define (difference x y) ;; difference는 x가 y보다 크면 x에서 y를 뺀 값을 출력하고
		(if (>= x y)                         ;; 그렇지 않으면 y에서 x를 뺀 값을 출력한다.
			(- x y)
			(- y x))
	)
> (difference 7 10)
Value: 3
> (difference 10 7)
Value: 3

;; case 구조와 유사한 cond 함수
> (define age 5)
> (cond 
		((<= age 6) 0) ;; age가 6보다 작거나 같으면 0을,
		((< age 60) 5000) ;; 그렇지 않고 age가 60보다 작으면 5000을,
		(else 2500) ;; 위 두 조건 모두 거짓이면 2500을 반환한다.
	)
Value: 0

> (define (admissionfee age) ;; 위 내용에서 cond 부분을 함수화한 것. 
		(cond
			((<= age 6) 0)
			((< age 60) 5000)
			(else 2500))
	)
> (admissionfee 65)
Value: 2500

> (define (compare x y)
		(cond
			((> x y) (display x) ;; x가 y보다 크면
				(display " is greater than ") ;; x가 y보다 크다는 문장을 출력한다.
				(display y)
				(newline))
			((< x y) (display y) ;; y가 x보다 크면
				(display " is greater than ") ;; y가 x보다 크다는 문장을 출력한다.
				(display x)
				(newline))
			((else (display x) ;; 위 두 조건 모두 거짓이면
				(display " and ") ;; x와 y가 같다는 문장을 출력한다.
				(display y)
				(display " are equal")
				(newline)))
	)
> (compare 20 30)
30 is greater than 20
> (compare 30 10)
30 is greater than 10

> (define (compare) ;; 위의 compare 함수에  키보드로부터 직접 두 값을 입력받는 기능을 추가.
		(display "input two integer: ")
		(newline)
		(define x (read))
		(define y (read))
		(cond
			((> x y) (display x) ;; x가 y보다 크면
				(display " is greater than ") ;; x가 y보다 크다는 문장을 출력한다.
				(display y)
				(newline))
			((< x y) (display y) ;; y가 x보다 크면
				(display " is greater than ") ;; y가 x보다 크다는 문장을 출력한다.
				(display x)
				(newline))
			((else (display x) ;; 위 두 조건 모두 거짓이면
				(display " and ") ;; x와 y가 같다는 문장을 출력한다.
				(display y)
				(display " are equal")
				(newline)))
	)
> (compare)
input two integer:
7     ...입력
11    ...입력
11 is greater than 7

;; 반복 구조는 재귀(recursion)에 의해 제공된다.
> (define (factorial n) 
		(if (= n 0) ;; 인자 n이 0이면 1을 반환, 
			1            ;; 그렇지 않으면 factorial을 재귀 호출하여 (n-1)! 을 계산하고
			(* n (factorial (- n 1))))                    ;; 이 결과에 n을 곱한 값을 반환.
	)
> (factorial 3)
Value: 6

> (define (adder lst) ;; lst에 속한 원자의 합을 구하는 함수
		(if (null? lst)
			0
			(+ (car lst) (adder (cdr lst)))) ;; [[car, cdr 블록 링크]](https://www.notion.so/Programming-973a5fceaf04413d9fdc5241bf38ba65)
	)
> (adder '(1 2 3))
Value: 6
> (adder '(1 (2) 3))    ...오류

> (define (adder lst) ;; lst의 car이 리스트이면 그에 대해서도 adder를 재귀 호출해 문제 해결
		(cond
			((null? lst) 0)
			((list? (car list)) (+ (adder (car list)) (adder (cdr lst))))
			(else (+ (car lst) (adder (cdr lst)))))
	)
> (adder '(1 (2) 3))
Value: 6
```

### 7. 예제

1. 정렬 프로그램

```scheme
;; 원자를 리스트에 삽입하는 함수의 예
> (define (insert atm lst) ;; 오름차순 정렬된 lst의 알맞은 위치에 atm을 삽입하는 함수
		(cond
			((null? lst) (cons atm '()))
			((< atm (car lst)) (cons atm lst))
			(else (cons (car lst) (insert atm (cdr lst)))))
	)

;; insert를 이용해서 lst의 데이터들을 정렬하는 함수
> (define (sort lst)
		(if (null? lst)
			'()
			(insert (car lst) (sort (cdr lst))))
	)

> (sort '(3 7 5 1 9))
Value: (1 3 5 7 9)
```

1. 하노이 탑 프로그램

```scheme
;; 규칙 1 : 왼쪽 기둥에서 n-1 개의 원판을 가운데 기둥으로 옮긴다. 이때 오른쪽 기둥을 이용한다.
;; 규칙 2 : 왼쪽 기둥의 원판을 오른쪽 기둥으로 옮긴다.
;; 규칙 3 : 가운데 기둥의 n-1 개의 원판을 오른쪽 기둥으로 옮긴다. 이때 왼쪽 기둥을 이용한다.
> (define (hanoi n a b c)
		(cond
			((= n 1)
				(display " move ")
				(display n)
				(display " from ")
				(display a)
				(display " to ")
				(display c)
				(newline))
			(else
				(hanoi (- n 1) a c b)
				(display " move ")
				(display n)
				(display " from ")
				(display a)
				(display " to ")
				(display c)
				(newline)
				(hanoi (- n 1) b a c)))
	)

> (hanoi 3 "left" "middle" "right")
move 1 from left to right
move 2 from left to middle
move 1 from right to middle
move 3 from left to right
move 1 from middle to left
move 2 from middle to right
move 1 from left to right
```
