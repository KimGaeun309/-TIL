## 정수 명령어
>정수만 저장하는 큐가 있습니다. 이 큐에는 다음과 같은 3가지의 연산을 할 수 있습니다.    
>I n : 정수 n을 큐에 삽입하는 연산을 의미합니다.    
>D 1 : 큐에서 최댓값을 삭제하는 연산을 의미합니다.    
>D -1 : 큐에서 최솟값을 삭제하는 연산을 의미합니다.    
>삽입되는 값에 중복되는 숫자는 주어지지 않습니다.    
>만약 큐가 비어있는데 적용할 연산이 ‘D’라면 이 연산은 무시합니다.    
>큐에 적용될 일련의 연산이 주어질 때 이를 처리한 후 최종적으로 큐에 저장된 데이터 중 최댓값과 최솟값을 출력하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 입력의 테스트 데이터의 수를 나타내는 정수 T가 주어집니다.    
>각 테스트 데이터의 첫째 줄에는 큐에 적용할 연산의 개수를 나타내는 정수 k가 주어집니다.    
>이어지는 k 줄 각각엔 연산을 나타내는 문자(‘D’ 또는 ‘I’)와 정수 n이 주어집니다.    
>* 1 ≤ T ≤ 3
>* 1 ≤ k ≤ 100,000    
>* -10^9 ≤ n ≤ 10^9
>
>**출력 형식**    
>각 테스트 데이터에 대해 모든 연산을 처리한 후 큐에 남아 있는 값 중 최댓값과 최솟값을 공백을 두고 출력합니다. 만약 큐가 비어있다면 ‘EMPTY’를 출력합니다.

**풀이** : 트리셋은 최대값 최소값을 순간순간마다 구해야 할 때 유용한 자료구조로, 이 문제와 같은 상황에 적합하다.

```python
from sortedcontainers import SortedSet # SortedSet (트리셋) import

T = int(input())

for _ in range(T): # 각 테스트 데이터마다
    k = int(input()) # k 개의 명령 
    s = SortedSet()
    
    for _ in range(k):
        command, x = tuple(input().split()) # 명령 입력받기
        x = int(x) # 정수형으로 바꾸는 것 잊지 말기
        
        if command == 'I': # 각 명령어에 맞는 연산 수행
            s.add(x)
        elif s:
            if x == 1:
                s.remove(s[-1])
            else:
                s.remove(s[0])
    if not s:        # 명령 수행 결과 트리셋에 남은 원소 중 최대 최소 출력 (남은 원소가 없으면'EMPTY' 출력)
        print("EMPTY")
    else:
        print(s[-1], s[0])
```

## 숫자 빠르게 찾기 2
>서로 다른 n개의 숫자가 주어집니다. 이후 m개의 숫자가 추가적으로 주어졌을 때, 각각의 숫자에 대해 처음 주어진 n개의 숫자 중 같거나 큰 최초의 숫자를 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 n, m이 공백을 두고 주어집니다.    
>두 번째 줄에는 n개의 숫자가 공백을 사이에 두고 주어집니다. 주어지는 모든 숫자는 서로 다름을 가정해도 좋습니다.    
>세 번째 줄 부터는 m개의 줄에 걸쳐 숫자가 한 줄에 하나씩 주어집니다.
>* 1 ≤ n, m ≤ 100,000
>* 1 ≤ 주어지는 값 ≤ 1,000,000,000
>
>**출력 형식**    
>m개의 줄에 걸쳐 주어진 n개의 숫자들 중 해당 숫자보다 같거나 큰 최초의 숫자를 출력합니다. 만약 그러한 숫자가 존재하지 않는다면, -1을 출력합니다.

**풀이** : treeset인 SortedSet()의 <code>bisect_left</code>를 사용해 답을 찾을 수 있다.
```python
from sortedcontainers import SortedSet

n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
s = SortedSet(arr)
queries = [int(input()) for _ in range(m)]

for query in queries:
    if s.bisect_left(query) == len(s): # 같거나 큰 최초의 숫자 존재X
        print(-1)
    else:
        print(s[s.bisect_left(query)]) # 존재 (출럭!)
```

## 친한 점
>2차 평면 위에 서로 다른 n개의 점이 주어집니다. 이후 m개의 질의가 주어지는데, 각 질의마다는 한 개의 점이 주어집니다. 각 질의에 대해 주어진 점 마다 가장 친근한 점을 찾아 출력하는 프로그램을 작성해보세요. (x, y)에 대해 (x', y')가 친근한 점이기 위해서는 x < x' 혹은 (x=x', y ≤ y')을 만족해야 합니다. 이 중 가장 친근한 점은 x좌표 값이 가장 작은 점이며, x좌표가 작은 점이 여러 개인 경우 y좌표 값이 가장 작은 점이 가장 친근한 점이 됩니다.    
>**입력 형식**    
>첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어집니다.    
>두 번째 줄부터는 n개의 줄에 걸쳐 점의 위치 (x, y)가 한 줄에 하나씩 공백을 사이에 두고 주어집니다.    
>이후 m개의 줄에 걸쳐 질의에 해당하는 점의 위치가 한 줄에 하나씩 공백을 사이에 두고 주어집니다.    
>* 1 ≤ n, m ≤ 10^5
>* 1 ≤ 주어진 점들의 x, y 값 ≤ 10^9
>
>**출력 형식**    
>m개의 질의에 대해 각 점마다 가장 친근한 점의 위치를 한 줄에 하나씩 공백을 사이에 두고 출력합니다. 만약 친근한 점이 존재하지 않는다면 -1 -1을 출력합니다.

**풀이** : 튜플을 treeset에 넣고 bisect_left(x, y)를 하면 x보다 같거나 큰 x'를 가진 튜플들 중 y'의 값이 가장 작은 것의 인덱스 위치를 찾아준다.

```python
from sortedcontainers import SortedSet

n, m = tuple(map(int, input().split()))
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
queries = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

s = SortedSet(points) # 트리셋 사용

# 질의마다 조건에 맞는 점 찾기
for target in queries:
    idx = s.bisect_left(target)
    if idx == n: # 존재하지 않는다면 (-1, -1) 출력
        print(-1, -1)
    else:  # 존재한다면 그 지점의 좌표값을 출력
        x, y = s[idx]
        print(x, y)
```

## 최대 숫자 구하기
>1부터 m까지의 숫자들이 적혀있는 공이 정확히 하나씩 놓여 있습니다. 이후 n개의 숫자들이 주어졌을 때, 순서대로 하나씩 해당 숫자가 적혀있는 공을 제거한 이후 남아 있는 공들 중 최대 공의 번호를 출력하는 프로그램을 작성해보세요. 더 이상 남아 있지 않은 공의 번호가 주어지는 경우는 없다고 생각해도 좋습니다.    
>**입력 형식**    
>첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어집니다.    
>두 번째 줄에는 n개의 숫자가 공백을 사이에 두고 주어집니다. 모든 숫자는 다르게 주어짐을 가정해도 좋습니다.    
>* 1 ≤ n < m ≤ 100,000
>* 1 ≤ 주어지는 숫자들 ≤ m
>
>**출력 형식**    
>n개의 줄에 걸쳐 한 줄에 하나씩 해당 숫자를 제거한 후 남아 있는 공들 중 가장 큰 번호를 출력합니다.

**풀이** : 값을 바로바로 삭제하면서 최댓값을 구해야 하므로 트리셋을 사용.

```python
from sortedcontainers import SortedSet

n, m = tuple(map(int, input().split()))
queries = list(map(int, input().split()))

s = SortedSet(range(1, m + 1)) # 1부터 m까지의 숫자들이 적힌 공

# 입력받은 숫자가 적힌 공 제거 후 남은 공 중 최댓값을 출력하는 것을 반복
for target in queries:
    # 해당 값을 제거
    s.remove(target)

    # 최댓값을 출력
    print(s[-1])

```

## 가까운 숫자
>처음 수직선 상에 x = 0 위치에만 점이 하나 놓여있습니다. 이후 n개의 숫자 주어졌을 때, 순서대로 하나씩 해당 숫자에 해당하는 x좌표 위치에 점을 하나 추가하며 추가한 직후 가장 가까운 두 점 사이의 거리를 출력하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 n이 주어집니다.    
>두 번째 줄에는 n개의 숫자가 공백을 사이에 두고 주어집니다. 이때 주어지는 숫자들은 전부 다름을 가정해도 좋습니다.    
>* 1 ≤ n ≤ 100,000
>* 1 ≤ 주어지는 숫자들 ≤ 10^9
>
>**출력 형식**    
>n번에 걸쳐 해당 숫자의 위치에 점을 추가한 이후 가장 가까운 두 점 사이의 거리를 한 줄에 하나씩 출력합니다.

**풀이** : 입력받은 숫자와 인접한 숫자들 사이 거리가 현재 최단 거리보다 더 짧으면 갱신하고, 점을 추가하고, 최단 거리를 출력하기를 반복하기 위해서는 <code>bisect_right()</code>를 사용해야
하므로 treeset를 사용함.

```python
from sortedcontainers import SortedSet
import sys
INT_MAX = sys.maxsize # 최대값 (최소값 구할 변수의 초기값으로 활용)

n = int(input())
s = SortedSet()
s.add(0) # x = 0 
queries = list(map(int, input().split()))
closest = INT_MAX

# 입력받은 숫자들을 하나씩 가져다 최단 거리를 갱신하고 점을 추가하고 최단 거리를 출력하기를 반복.
for query in queries:
    r_idx = s.bisect_right(query)
    if r_idx < len(s): # r_idx가 존재한다면
        closest = min(closest, s[r_idx] - query) # 점 사이 최단 거리 갱신
    # 처음 수직선 상에 x=0 점이 있고, 양수 점듦만 추가되므로 l_idx는 무조건 존재.
    l_idx = r_idx - 1
    closest = min(closest, query - s[l_idx]) # 점 사이 최단 거리 갱신
    s.add(query) # 점 추가
    print(closest) # 최단 거리 출력
```


