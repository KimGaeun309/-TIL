## 큰 숫자만 계속 고르기
>n개의 숫자가 주어졌을 때 그 중 가장 큰 숫자를 골라 1씩 빼는 작업을 m번 반복하려고 합니다. 이를 반복한 이후 남아있는 숫자들 중 최댓값을 구하는 프로그램을 작성해보세요. 단, 가장 큰 숫자가 여러 개라면 이 중 아무거나 하나를 골라 진행하면 됩니다.     
>**입력 형식**    
>첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어집니다.    
>두 번째 줄에는 n개의 숫자가 공백을 사이에 두고 주어집니다.    
>* 1 ≤ n, m ≤ 100,000  
>* 1 ≤ 주어지는 숫자들 ≤ 10^9
> 
>**출력 형식**    
>남아있는 숫자들 중 최댓값을 출력합니다. 결과가 음수가 될 수도 있음에 유의합니다.

**풀이** : heapq는 min heap이다. 여기에 값을 넣고 뺄 때 '-' 를 붙인다면 max heap으로 활용할 수 있다. 

```python
import heapq

n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

pq = []  # heap

for elem in arr:
    heapq.heappush(pq, -elem) # 음수 부호를 붙여 push

for i in range(m):
    pop = -heapq.heappop(pq) # 음수 부호를 붙여 pop
    heapq.heappush(pq, -(pop - 1)) # 1 뺀 후 다시 음수 부호 붙여 push


print(-pq[0]) # 답 출력
```

## 최소 정수 출력
>비어있는 배열에 연산을 하려 합니다. 연산은 다음 2가지입니다.    
>입력이 자연수 xx라면, 배열에 자연수 xx를 넣습니다.    
>입력이 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거합니다.    
>입력된 연산을 실행하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에 연산의 개수 n이 주어집니다.    
>두 번째 줄부터 n + 1 번째 줄 까지는 정수 xx 가 주어집니다.    
>* 1 ≤ n ≤ 100,000
>* 0 ≤ xx ≤ 2^31
>
>**출력 형식**    
>입력에서 0이 주어진 회수만큼 답을 출력합니다. 배열이 비어있고 0이 입력되었다면 0을 출력합니다.

**풀이** : heapq 를 최소 힙으로 사용해 최소 정수를 출력하는데 사용한다.

```python
import heapq
n = int(input())
pq = []

for _ in range(n):
    num = int(input())
    # 0이 입력되었다면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거
    if num == 0: 
        if pq: # pq가 비어있지 않다면
            print(pq[0])  # 
            heapq.heappop(pq)
            
        else: # pq가 비어있다면
            print(0) # 0 출력
    # 0이 아닌 수가 입력되었다면 배열에 입력받은 수를 삽입
    else:
        heapq.heappush(pq, num)
```

## 가장 가까운 점
>2차 평면 위에 서로 다른 위치에 놓여있는 n개의 점이 주어집니다. 이때 원점에서 가장 가까운 점을 하나 골라,
> 해당 점의 x, y 값에 2씩 더해주는 작업을 m번 반복하려고 합니다. 이를 전부 반복한 이후 원점에 가장 가까이 있는 점을 출력하는 프로그램을 작성해보세요. 
> 원점과 특정 점 (x, y)과의 거리는 |x| + |y| 로 생각하며, 만약 원점과의 거리차 최소인 점이 여러 개 있다면 x값이 가장 작은 점을, 
> 만약 그러한 점이 여러 개라면 y값이 가장 작은 점이 원점과 가장 가까이에 있는 점이라 생각합니다. 
> 단, 같은 지점에 서로 다른 점이 여러 개가 있는 경우는 발생하지 않는다고 가정해도 좋습니다.    
>**입력 형식**    
>첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어집니다.    
>두 번째 줄 부터는 n개의 줄에 걸쳐 각 점의 위치 (x, y)가 공백을 사이에 두고 한 줄에 하나씩 주어집니다.    
>* 1 ≤ n, m ≤ 100,000
>* 1 ≤ x, y 값 ≤ 10^9
>
>**출력 형식**    
>m번 원점으로 부터 가장 가까운 점을 잡아 2씩 더해주는 작업을 진행한 이후 가장 원점에 가까운 점의 (x, y)값을 공백을 사이에 두고 출력합니다.

**풀이** : 원하는 기준에 따라 정렬하기를 원한다면 그 값을 튜플의 첫 번째 원소로 써서 heap에 삽입한다.

```python
import heapq
n, m = tuple(map(int, input().split()))
pq = []

for _ in range(n):
    x, y = tuple(map(int, input().split()))
    heapq.heappush(pq, (x+y, x, y)) # heap에 (거리, x, y) 를 삽입

for _ in range(m):
    _, x, y = heapq.heappop(pq) # 최솟값을 삭제했다가
    heapq.heappush(pq, (x+y+4, x+2, y+2)) # x, y 에 2씩 더해 다시 삽입

# 결과 출력
_, x, y = pq[0]
print(x, y)
```

## 배열 추출
>배열에 다음과 같은 연산을 할 수 있습니다.    
>배열에 자연수 x를 넣습니다.    
>배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거합니다.    
>비어있는 배열에서 시작하여 입력된 연산을 실행하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에 연산의 개수 n이 주어집니다.    
>다음 n개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어집니다.    
>x가 자연수라면 배열에 x라는 값을 넣습니다.    
>x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거합니다.    
>* 1 ≤ n ≤ 10,000   
>* 0 ≤ 입력되는 수 ≤ 100,000
>
>**출력 형식**
>입력에서 0이 주어진 횟수만큼 답을 출력합니다.    
>만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 됩니다.

**풀이** : 값을 삭제하면서 최댓값을 확인해야 하므로 Priority Queue 를 사용한다. heapq 모듈을 가져와 값을 음수로 삽입, 삭제하여 max heap처럼 사용하면 쉽게 풀 수 있다.

```python
import heapq

n = int(input())
pq = []

for _ in range(n):
    x = int(input())
    # 0이 입력되면 최댓값 출력하고 삭제 (배열이 비어있다면 0 출력)
    if x == 0:
        if pq:
            m = -heapq.heappop(pq) # 음수로 꺼내기 (max heap)
            print(m)
        else:
            print(0)
    # 0 외의 수가 입력된다면 삽입
    else:
        heapq.heappush(pq, -x) # 음수로 삽입 (max heap)
```
## 마지막으로 남은 숫자
>n개의 숫자가 주어졌을 때 가장 큰 숫자 2개를 뽑아 제거하고 두 숫자의 차이에 해당하는 숫자를 다시 집어넣는 것을 2개 이상의 숫자가 남아 있는 한 계속 반복하려고 합니다. 만약 뽑은 가장 큰 숫자 2개가 동일하다면, 이 경우에는 차이가 0이기 때문에 새롭게 집어넣지 않는다고 합니다. 이 과정을 진행한 이후 마지막으로 남게되는 숫자를 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 n이 공백을 사이에 두고 주어집니다.    
>두 번째 줄에는 n개의 숫자가 공백을 사이에 두고 주어집니다.    
>* 1 ≤ n ≤ 100,000  
>* 1 ≤ 주어지는 숫자들 ≤ 10^9
> 
>**출력 형식**    
>마지막으로 남게되는 숫자가 정확히 하나라면 해당 숫자를 출력합니다. 만약 아무 숫자도 남지 않게 된다면 -1을 출력합니다.

**풀이** : heapq 에 '-'를 붙인 숫자를 넣고 빼서 max heap으로 활용한다. while문을 활용해 배열에 1개 이하의 원소가 남으면 반복문을 빠져나오도록 한다.

```python
import heapq

n = int(input())
nums = list(map(int, input().split()))
pq = []

# heapq에 정수 삽입
for num in nums:
    heapq.heappush(pq, -num) # (음수 부호 붙여 넣어 max heap으로 활용)

# pq에 2개 이상의 원소가 존재할 동안
while len(pq) >= 2:
    # 최댓값 두 개를 삭제해 num1, num2에 저장하고
    num1 = -heapq.heappop(pq) # (음수 부호)
    num2 = -heapq.heappop(pq) # (음수 부호)
    
    # 두 값의 차이를 다시 pq에 push한다 (num1 == num2 이면 삽입X)
    if num1 != num2:
        new = abs(num1-num2) # (음수 부호)
        heapq.heappush(pq, -new) # (음수 부호)

# 답 출력
if pq: 
    print(-pq[0])
else:
    print(-1)

```

## 최솟값 3개
>n개의 숫자가 순서대로 하나씩 주어졌을 때, 숫자가 하나씩 주어질 때마다 지금까지 주어진 숫자들 중 가장 작은 숫자 3개의 곱을 출력하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 n이 주어집니다.    
>두 번째 줄에는 n개의 숫자가 공백을 사이에 두고 주어집니다.    
>* 1 ≤ n ≤ 100,000
>* 1 ≤ 주어지는 숫자들 ≤ 100,000
>
>**출력 형식**    
>n개의 숫자가 순서대로 하나씩 주어질 때마다 지금까지 주어진 숫자들 중 가장 작은 숫자 3개의 곱을 한 줄에 하나씩 출력합니다. 만약 아직 주어진 숫자의 수가 채 3개가 되지 않는다면, -1을 출력합니다.

**풀이 1** : heappop한 숫자들을 변수에 저장했다가 원하는 값 출력 후 다시 heappush

```python
import heapq
n = int(input())
nums = list(map(int, input().split()))
pq = []

for num in nums:
    heapq.heappush(pq, num)
    if len(pq) >= 3:
        n1 = heapq.heappop(pq)
        n2 = heapq.heappop(pq)
        n3 = heapq.heappop(pq)
        print(n1 * n2 * n3)
        heapq.heappush(pq, n1)
        heapq.heappush(pq, n2)
        heapq.heappush(pq, n3)
    else:
        print(-1)
```

**풀이 2** : mul3() 함수 안에서 힙 성질 이용해 최솟값 찾기

```python
import heapq
n = int(input())
nums = list(map(int, input().split()))
pq = []

def mul3():
    if len(pq) == 3:
        return pq[0] * pq[1] * pq[2]
    num1  = pq[0]
    if len(pq) == 4:
        if pq[1] < pq[2]:
            num2 = pq[1]
            num3 = min(pq[2], pq[3])
        else:
            num2, num3 = pq[2], pq[1]
    else:
        if pq[1] < pq[2]:
            num2 = pq[1]
            num3 = min(pq[2], pq[3], pq[4])
        else:
            num2 = pq[2]
            if len(pq) == 5:
                num3 = pq[1]
            elif len(pq) == 6:
                num3 = min(pq[1], pq[5])
            else:
                num3 = min(pq[1], pq[5], pq[6])
    return num1 * num2 * num3

for num in nums:
    heapq.heappush(pq, num)
    if len(pq) >= 3:
        print(mul3())
    else:
        print(-1)
```

## 배열 추출 2
>배열에 다음과 같은 연산을 할 수 있습니다.    
>배열에 자연수 x (x ≠ 0) 를 넣습니다.    
>배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거합니다.    
>(절댓값이 가장 작은 값이 여러개일 때는, 그 중 가장 작은 수를 출력하고, 그 값을 배열에서 제거합니다.)    
>비어있는 배열에서 시작하여 입력된 연산을 실행하는 프로그램을 작성해보세요.       
>**입력 형식**    
>첫 번째 줄에 연산의 개수 n이 주어집니다.    
>다음 n개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어집니다.    
>x가 자연수라면 배열에 x라는 값을 넣습니다.    
>x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거합니다.    
>* 1 ≤ n ≤ 100,000 
>* -2^31 < 입력되는 수 < 2^31
>
>**출력 형식**    
>입력에서 0이 주어진 횟수만큼 답을 출력합니다.    
>만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 됩니다.

**풀이** : 배열에 원소를 삽입거나 배열에서 절댓값이 가장 작은 값을 찾아 삭제해야 하므로 heapq에 (x의 절댓값, x) 튜플을 넣어 절댓값이 가장 작은 수를 바로 찾을 수 있도록 해 해결한다.

```python
import heapq
n = int(input())
nums = [
    int(input())
    for _ in range(n)
]

pq = []

for x in nums:
    if x != 0:
        heapq.heappush(pq, (abs(x), x)) # pq에 (x의 절댓값, x) 삽입
    else:
        if pq: # pq에 원소가 있다면
            _, min_x = heapq.heappop(pq) # 절댓값이 가장 작은 원소 삭제하고
            print(min_x) # 원소 출력
        else: # pq에 원소가 없다면
            print(0) # 0 출력
```
