# Prolog

- 컴파일 환경
    
    [SWISH -- SWI-Prolog for SHaring](https://swish.swi-prolog.org/)
    

### 1. 프로그램의 구조

```prolog
/* Prolog 프로그램은 사실(fact)와 규칙(rule)들을 데이터베이스에 등록하고
  이에 대해 질의(query)를 하면 프로그램이 실행되어 응답을 하는 구조이다. 
  사실(fact)의 구조: 이름(인자1, 인자2, ..., 인자n). */
male(a). % a는 남자다.
female(b). % b는 여자다.
father(a, c). % a는 c의 아버지다.
mother(b, d). % b는 d의 어머니다.

% 이와 같은 사실들을 데이터베이스에 등록하고 질의하면 프로그램이 실행되어 응답을 한다.
male(a).
female(b).
male(c).
% 이런 내용들을 데이터베이스에 등록하고 프롬프트에서 질의를 하면 Prolog 시스템이 응답한다.
?- male(a). % a는 남자냐고 질의
Yes    % Prolog 시스템의 응담: 그렇다
?- male(b). % b는 남자냐고 질의
No     % Prolog 시스템의 응답: 그렇지 않다

% 누가 남자인지를 질의할 수도 있다. (첫번째 문자가 대문자이면 변수로 인식한다.)
?- male(X). % male(X)를 만족하는 X가 있는가? 여기서 X는 변수에 해당된다. 
X = a    % 하나의 답을 응답하고 다른 답을 계속 찾을 것인지 기다린다. 
% (1) 여기서 ';' 입력 -> 다른 값 더 찾음
?- male(X)
X = a ;
X = c ; 
No
% (2) 'Enter' 입력 -> 중단

father(a, c). % a는 c의 father이다.
mother(b, c). % b는 c의 mother이다.
mother(d, e). % d는 e의 mother이다.
?- father(a, c). % 사용자의 질의: a가 c의 father인가?
Yes    % 시스템의 응답: 그렇다.
?- faher(X, c). % father(X, c)를 만족하는 X가 있는가?
X = a ;    % c의 father인 a를 출력
No     % 더 이상 없다는 No를 출력한다.

/* Prolog 시스템의 동작 과정을 알아보는 가장 좋은 방법은 trace를 이용하는 것이다.
	 trace는 동작하는 동안의 모든 단계를 보여 주며, 이는 다음과 같은 4가지 행위로 구분한다.
	 1. call(질의에 대한답을 찾기 위한 시도 초기에 발생), 
	 2. exit(질의에 대한 답을 찾았을 때 발생), 
	 3. redo(질의에 대한 답을 찾기 위하여 재시도했을 때 발생), 
	 4. fail(질의에 대한 답을 찾지 못했을 때 발생)  */
trace % 바로 앞 질의에 대해 trace하면 다음과 같이 출력된다
?- father(X, c).
1 Call: father(_G254, c) % call은 질의를 처음 시도했을 때 나타나는 것이다
1 Exit: father(a, c) % exit는 질의에 대한 답을 찾았을 때 나타난다. a는 임시변수 _G254에 대한 답을 의미한다.
X = a ;
No

% 이 질의에는 No를 응답한다.
?- mother(X, a). 
No
% 이 질의를 trace하면 다음과 같다.
?- mother(X, a). 
1 Call: mother(_G434, a)
1 Fail: mother(_G434, a) % fail은 질의에 대한 답을 찾지 못했을 때 나타난다.
No
```

### 2. 규칙

```prolog
/* 데이터베이스에 사실 외에 규칙을 등록할 수도 있다.
	 규칙(rule)의 구조: 결론:- 전제표현식1, 전제표현식2, ..., 전제표현식n 
   오른쪽의 '전제표현식1, 전제표현식2, ..., 전제표현식n' 은 if에 해당하는 전제이고,
	 왼쪽의 결론은 then에 해당하는 부분으로, 만약 전제가 참이면 결론도 참이 된다는 뜻이다. */

male(a) :- father(a, c) % father(a, c)기 참이면 male(a)가 참이 되는 규칙이다.
% 이 규칙의 의미를 일반화시키기 위해 다음과 같이 a와 c를 변수로 변환할 수 있다.
male(X) :- father(X, Y) 

% 다음과 같은 사실과 규칙으로 이루어진 데이터베이스가 있을 때, 
father(a, c).
mother(b, c).
male(X) :- father(X, Y).
female(X) :- mother(X, Y).
?- male(a). % a가 male인지 질의하면 Yes를 응답한다.
Yes
father(a, Y) % 이 질의는 다음을 만족하는 Y가 있는지 찾는다. 
% father(a, c) 가 이를 만족하므로 Prolog 시스템은 Yes를 응답한다.
% 이 질의를 trace한 결과는 다음과 같다.
trace
?- male(a).
1 Call: male(a)
2 Call: father(a, _L185)
2 Exit: father(a, c)
1 Exit: male(a)
Yes

?- male(X). % male(X)를 만족하는 X가 있는가?
X = a ;
No

/* 전제표현식이 여러 개인 규칙의 예는 다음과 같다. */

couple(X, Y) :- father(X, Z), mother(Y, Z). % 전제표현식들 사이 콤마는 AND 연산 의미 가짐.
% X가 Z의 아버지이고 Y가 Z의 어머니이면 X와 Y는 부부이다.

father(a, c). 
father(c, e).
mother(b, c).
mother(d, e).
couple(X, Y) :- father(X, Z), mother(Y, Z).

?- couple(a, X). % -> father(a, Z) 를 만족하는 Z를 찾음 -> father(a, c) 찾음
X = b ;           % -> mother(Y, c) 를 만족하는 Y를 찾는다. -> mother(b, c) 를 찾는다.
No                  % -> 시스템은 결국 a와 부부 관계에 있는 b를 출력한다. 
										 % -> mother(Y, c)에 대해 더 이상의 답이 없으므로 No 출력하고 종료.
 
% trace한 결과
trace
?- couple(a, X).
1 Call: couple(a, _G435)
2 Call: father(a, _L170)
2 Exit: father(a, c)
2 Call: mother(_G435, c)
2 Exit: mother(b, c)
1 Exit: couple(a, b)
X = b;
2 Redo: mother(_G435, c)
1 Fail: couple(a, _G435)
No

?- couple(X, Y).
X = a, 
Y = b ;

X = c,
Y = d ;

/* 여러 개의 전제표현식으로 구성된 규칙인 경우에서 역행이란 : 
	 임의의 전제표현식에서 답을 찾는 데 실패했을 때 Prolog 시스템이 다른 답을 찾기 위해 
	 바로 앞에 위치한 전제표현식으로 되돌아가서 질의를 하는 것.*/

parent(a, b).
parent(b, c).
parent(c, d).
grandparent(X, Y) :- parent(X, Y), parent(Y, Z). 

?- grandparent(X, d).
X = b ;
No
% 이 질의는 
% 1. parent(X, Y)를 찾는다 -> parent(a, b)를 찾아 parent(b, d)가 있는지 찾아보지만 실패한다.
% 2. 시스템은 다른 답을 찾기 위해 바로 앞에 위치한 첫 번째 전제표현식으로 되돌아간다. (역행)
% 3. parent(X, Y)를 찾는다 -> parent(b, c)를 찾아 parent(c, d)가 있는지 찾아보고 성공한다.
% 4. X = b 를 출력하고 더 이상 답이 없으므로 시스템은 No 를 출력하고 종료한다.

% 위 동작을 trace하면 다음과 같다.
trace
?- grandparent(X, d).
1 Call: grandparent(_G458, d)
2 Call: parent(_G458, _L170)
2 Exit: parent(a, b)
2 Call: parent(b, d)
2 Fail: parent(b, d)
2 Redo: parent(_G458, _L170)
2 Exit: parent(b, c)
2 Call: parent(c, d)
2 Exit: parent(c, d)
1 Exit: grandparent(b, d)
X = b;
2 Redo: parent(_G458, _L170)
2 Exit: parent(c, d)
2 Call: parent(d, d)
2 Fail: parent(d, d)
1 Fail: grandparent(_G458, d)
No
```

### 3. 재귀

```prolog
/* Prolog에서 임의의 코드를 반복해서 실행하려면 재귀를 사용해야 한다.*/

parent(a, b).
parent(b, c).
ancestor(X, Y) :- parent(X, Y). % X가 Y의 부모이거나 X가 Z의 부모이고 Z가 Y의 조상이면
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y). % X가 Y의 조상이다.

?- ancestor(X, c).
X = b ; 
X = a ; 
No 
% 이 질의는
% 1. parent(X, c) 를 적용하여 parent(b, c) 를 찾는다. 따라서 X = b를 출력한다.
% 2. 다른 답을 찾기 위해 역행하여 찾는데, parent(X, c)를 만족하는 경우는 더 이상 없다.
% 3. 따라서 재귀호출된 규칙을 찾아야 한다. 
% 4. 먼저 parent(X, Z) 를 만족하는 parent(a, b) 를 찾아 ancestor(b, c)를 찾는데, 
%               ancestor(b, c)를 만족하는 parent(b, c) 를 찾았으므로 X = a 를 출력한다.
% 5. 더 이상 답이 없으므로 시스템은 No를 출력하고 종료한다.

% 조상의 개념을 다음과 같이 작성하고
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- ancestor(X, Z), parent(Z, Y).
% 다음과 같이 질의를 하면
?- ancestor(X, Y).
% 종료되지 못하고 무한 재귀하는 문제가 발생한다. *설명 필요
X = a,
Y = b ;
X = b
Y = c ;
X = a ;
Y = c ;
ERROR: Out of local stack
```

### 4. 연산

```prolog
/* Prolg의 연산
	 is 연산자 : 산술표현식의 값을 변수의 값으로 한다
		X is 3*4 = 변수 X의 값을 12로 한다
	 + 연산자, - 연산자, * 연산자, > 연산자, < 연산자, >= 연산자, =< 연산자
	 / 연산자   : 실수 나누기
	 // 연산자  : 정수 나누기
	 mod 연산자 : 나눈 나머지
	 ** 연산자  : 거듭제곱
	 = 연산자   : 같다
	 , 연산자   : 그리고
	 ; 연산자   : 또는 */

non_zero(X) :- X<0 ; X>0. % 0보다 작거나 0보다 커야 한다는 규칙
?- non_zero(0).
No

score(a, 70, 90).
score(b, 60, 70).
score(c, 80, 100).
score(d, 70, 65).
score(e, 90, 95).
pass(X) :- score(X, S1, S2), Avs is (S1+S2)/2, Ave >= 70. % 평균이 70점 이상이면 합격
?- pass(X).
X = a ;
X = c ;
X = e ;
No

% 다음은 팩토리얼을 구하는 사실과 규칙이다
factorial(0, 1). % 0 팩토리얼은 2이다
factorial(N,F) :- % N 팩토리얼은 F이다 (재귀)
	N>0,  
	N1 is N-1,
	factorial(N1, F1),
	F is N * F1.
?- factorial(2, F).
W = 2
Yes
% factorial(2, F) -> factorial(1, F1) -> factorial(0, F2) -> F2 는 1
                                                 % -> F1 는 1 -> F 는 2

% 다음은 하노이 탑 프로그램이다.
hanoi(1, A, _, C) :- 
	write(),
	write(),
	write(),
	write(),
	n1.
hanoi(N, A, B, C) :-
	N>1,
	M is N-1,
	hanoi(M, A, C, B),
	hanoi(1, A, _, C),
	hanoi(M, B, A, C).

% 다음은 식당을 이용하려는 인원수와 식사를 위한 비용 정보로 이용 가능한 음식점을 출력한다.
restaurant(a, korean, 1000).
restaurant(b, western, 3000).
restaurant(c, korean, 5000).
restaurant(d, western, 10000).
restaurant(e, japanese, 20000).
restaurant(f, korean, 30000).
expert(Name, Style, Number, Money) -= restaurant(Name, Style, Y), Number*Y <= Money.

?- expert(Name, Style, 3, 50000).
Name = a,
Style = korean ;

Name = b,
Style = western ; 

Name = c,
Style = korean ;

Name = d,
Style = western ;

No

?- extern(Name, western, 5, 50000).
Name = b ;
Name = d ;
No
```

### 5. 리스트

```prolog
/* 리스트는 Prolog의 중요한 데이터 구조로, [] 로 표현하며 각 원자는 콤마로 구분한다. */

[H|T] % 이 리스트에서 H는 Scheme의 car에, T는 Scheme의 cdr에 대응된다.

% 다음은 리스트의 길의를 알아내는 것을 정의한 예이다 
length([], 0). % 공 리스트의 길이는 0이다
length([H|T], N) :- length(T, M), N is M+1. % 첫 번째 원자를 제외한 리스트의 길이 + 1

% 다음은 첫 번째 인자가 두 번째 인자인 리스트에 속하는지 파악하는지 알아보는 것을 정의한 예이다.
member(X, [X|List]). % X가 리스트의 첫 번째 원자라면 X가 리스트에 속한다
member(X, [Y|List]) :- member(X, List). % X가 리스트의 중간에 위치하면 X가 리스트에 속한다.

% 다음은 첫 번째 리스트 인자에 두 번째 리스트 인자를 추가하는 정의이다.
append([ ], L, L). % 공 리스트에 리스트 L을 추가하면 리스트 L이 된다.
append([H|A], L, [H|T]) :- append(A, L, T).% [H|A] 리스트에 L을 추가하면 [H|T] 가 된다.
																	% 이때 T는 A 리스트에 L을 추가한 것이다. 

```
