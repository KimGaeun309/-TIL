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

## top k 숫자
>n개의 숫자가 주어졌을 때, 중복을 제외하고 내림차순으로 정렬했을 때 앞에 있는 k개의 숫자를 출력하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 원소의 개수 n과 k가 공백을 사이에 두고 주어집니다.    
>두 번째 줄에는 n개의 원소가 공백을 사이에 두고 주어집니다.    
>* 1 ≤ k ≤ n ≤ 100,000
>* 1 ≤ 주어지는 원소 값 ≤ 10^9
>
>**출력 형식**    
>중복을 제외하고 내림차순으로 정렬했을 때 앞에 있는 k개의 숫자를 공백을 사이에 두고 출력합니다. 중복을 제외했을 때 원소의 개수가 k보다 작은 경우는 없다고 가정해도 좋습니다.

**풀이** : 정렬된 순서대로 순회하는 트리셋을 활용해 풀었다. 

```python
from sortedcontainers import SortedSet
n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

s = SortedSet()  # treeset 

for elem in arr:
    s.add(-elem)  # 내림차순 정렬을 위해 treeset에 숫자에 -를 붙여 저장 

for i in range(k):   # s[0]부터 s[k-1]까지의 값에 -를 붙여 출력하면 
    print(-s[i], end=' ')  #내림차순으로 k개의 숫자를 출력함. 


```

## 작지만 큰 숫자
>n개의 숫자로 이루어진 수열이 하나 주어지고, 그 이후 m개의 질의가 주어집니다. 각 질의마다 하나의 숫자가 주어진다 했을 때, 순서대로 수열 내에서 주어진 숫자보다 같거나 작은 숫자들 중 최댓값을 하나 골라 제거하는 것을 반복하는 프로그램을 작성해보세요. 단, 같거나 작은 숫자가 없는 경우에는 제거하지 않고 넘어갑니다.
>**입력 형식**    
>첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어집니다.    
>두 번째 줄에는 n개의 숫자가 공백을 사이에 두고 주어집니다. 주어지는 n개의 숫자는 서로 다름을 가정해도 좋습니다.    
>세 번째 줄에는 질의에 해당하는 m개의 숫자가 공백을 사이에 두고 주어집니다.    
>* 1 ≤ n, m ≤ 100,000   
>* 1 ≤ 주어지는 모든 숫자들 ≤ 10^9
>
>**출력 형식**    
>m개의 질의에 대해 각 질의마다 해당 숫자보다 같거나 작은 숫자들 중 최댓값을 한 줄에 하나씩 출력합니다. 이러한 숫자가 존재하는 경우에는 수열에서 해당 숫자를 제거한 뒤 그 다음 질의를 진행해야 하며, 이러한 숫자가 존재하지 않는 경우에는 -1을 출력하고 그 다음 질의로 넘어갑니다.

**풀이** : treeset인 SortedSet을 이용한다. bisect_right로 해당 숫자보다 큰 수 중 최솟값의 인덱스를 얻은 뒤 1을 빼면 해당 숫자보다 같거나 작은 숫자들 중 최댓값의 인덱스를 구할 수 있다.

```python
from sortedcontainers import SortedSet
n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

s = SortedSet(arr)

for num in queries:
    # num보다 큰 수 중 최솟값의 인덱스에서 1을 빼면 
    # num보다 같거나 작은 숫자들 중 최댓값의 인덱스가 나온다.
    index = s.bisect_right(num) - 1 
    if index >= 0:
        print(s[index])
        s.remove(s[index])
    else:
        print(-1)
```

## 자리 차지하기
>처음 m개의 비어있는 의자가 주어집니다. 이 의자들은 순서대로 1번부터 m번까지 번호가 붙여져 있습니다. 이후 사람들이 앉고자 하는 의자에 대한 정보 a_i 값이 n개 주어집니다. a_i 는 1에서 m 사이로, i번째 사람은 1번에서 a_i 번 사이의 의자에만 앉고 싶다는 것을 의미합니다. 1번 사람부터 순서대로 해당 규칙에 맞춰 앉기 시작하며, 최초로 앉지 못하는 사람이 생기면 종료한다고 했을 때 사람들이 앉을 자리를 적절하게 배정하여 앉게 되는 사람 수를 최대로 만드는 프로그램을 작성해보세요.
>**입력 형식**    
>첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어집니다.     
>두 번째 줄에는 n개의 숫자가 공백을 사이에 두고 주어집니다.    
>* 1 ≤ n, m ≤ 100,000    
>* 1 ≤ 주어지는 숫자들 ≤ m    
>
>**출력 형식**    
>최대로 앉힐 수 있는 사람의 수를 출력합니다.

**풀이** : 최솟값을 계속 삭제하면서 최솟값을 확인해야 하므로 treeset을 사용합니다. 그리고 queries에 질의를 입력받아 저장하고 정렬해 앉을 수 있는 자리가 더 적은 사람들부터 확인하여
최대한 많은 사람들이 착석할 수 있도록 합니다.

```python
from sortedcontainers import SortedSet
n, m = tuple(map(int, input().split()))
queries = list(map(int, input().split()))

chairs = list(range(1, m+1))
chairset = SortedSet(chairs) # treeset으로 의자 번호 관리
queries.sort() # 질의를 정렬해 최대한 많은 사람들이 앉을 수 있도록 함.
answer = 0 # 앉을 수 있는 사람의 수를 저장할 변수

# 정렬된 요청들을 하나씩 확인하면서
for num in queries:
    if chairset and chairset[0] <= num: # 의자가 아직 남아 있으면서 이번 사람이 현재 남은 의자 번호 중 가장 작은 번호에 앉을 수 있다면
        chairset.remove(chairset[0])  # 그 사람을 의자에 앉히므로 chairset에서 가장 작은 번호를 가진 의자를 삭제하고
        answer += 1  # 사람 수 += 1 을 하기를 반복한다.

print(answer)
```

## 차이가 가장 작은 수
>n개의 정수로 이루어진 수열에서 두 수를 골랐을 때, 그 차이가 m 이상이면서 제일 작은 경우의 그 차이를 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에 정수 n과 m이 주어집니다.    
>두 번째 줄부터 n개의 줄에 걸쳐 n개의 정수가 차례대로 한 줄에 하나씩 주어집니다.    
>* 1 ≤ n ≤ 100,000 
>* 1 ≤ m ≤ 2 * 10^9
>* -10^9 ≤ 정수의 크기 ≤ 10^9
> 
> **출력 형식**    
>차이가 m이상이면서 제일 작은 경우의 그 차이를 출력합니다. 만약 그러한 경우가 없다면 -1을 출력합니다.

**풀이** : <code>s.bisect_left(elem+m)</code>로 각 원소에 따라 차이가 m 이상이면서 제일 작은 경우의 차이들을 구해 그 중 가장 작은 수를 구한다.

```python
import sys
INT_MAX = sys.maxsize
from sortedcontainers import SortedSet

n, m = tuple(map(int, input().split()))
arr = [int(input()) for _ in range(n)]
s = SortedSet(arr)

min_diff = INT_MAX

# treeset에 담긴 수열을 순회하면서
for elem in s:
    # elem보다 크면서 m 이상 차이나는 수 중 가장 작은 수의 인덱스를 구해
    idx = s.bisect_left(elem + m) 
    if idx < len(s): # s에 존재한다면 
        curr_diff = s[idx] - elem  # 차이를 구해 갱신하기를 반복한다.
        min_diff = min(min_diff, curr_diff)
    
if min_diff == INT_MAX:
    print(-1)
else:
    print(min_diff)
```

## 점 빼기
>2차 평면 위에 서로 다른 n개의 점이 주어집니다. 이후 m개의 질의가 주어지는데, 각 질의마다는 한 개의 숫자 k가 주어집니다. 각 질의에 대해 주어진 숫자 k보다 x값이 같거나 큰 점 중 x값이 가장 작은 점을 찾아 지우려고 합니다. 만약 x값이 가장 작은 점이 여러 개라면, 그 중 y값이 가장 작은 점을 지우면 됩니다. 각 질의에 대해 해당하는 점을 순서대로 출력하고 지우는 프로그램을 작성해보세요.
>**입력 형식**    
>첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어집니다.    
>두 번째 줄부터는 n개의 줄에 걸쳐 점의 위치 (x, y)가 한 줄에 하나씩 공백을 사이에 두고 주어집니다.    
>이후 m개의 줄에 걸쳐 질의에 해당하는 숫자 k가 한 줄에 하나씩 주어집니다.    
>* 1 ≤ n, m ≤ 10^5 
>* 1 ≤ 주어진 점들의 x, y 값 ≤ 10^9
>* 1 ≤ k ≤ 10^9 
>
>**출력 형식**    
>m개의 질의에 대해 해당하는 점의 위치를 한 줄에 하나씩 공백을 사이에 두고 출력합니다. 만약 그러한 점이 존재하지 않는다면 -1, -1을 출력합니다.

**출력** : 점이 튜플로 담긴 리스트를 treeset에 저장해 bisect_left()를 사용해 x값이 k보다 같거나 큰 점 중 가장 작은 점 중에서 y값이 가장 작은 점을 찾습니다.
그런 점이 존재한다면 출력하고 그 점을 treeset에서 삭제합니다. 그런 점이 존재하지 않는다면 "-1 -1"을 출력합니다.

```python
from sortedcontainers import SortedSet
n, m = tuple(map(int, input().split()))
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
queries = [
    int(input())
    for _ in range(m)
]

s = SortedSet(arr)

for k in queries:
    idx = s.bisect_left((k, 50))
    if idx < len(s):
        x, y = s[idx]
        print(f"{x} {y}")
        s.remove(s[idx])
    else:
        print("-1 -1")
```

## 문제 추천 시스템 1
>문제를 추천해주는 프로그램을 만드려합니다. 만드려는 명령어는 총 3가지입니다.    
>rc x : x가 1인 경우 문제 리스트에서 난이도가 가장 높은 문제의 번호를 출력합니다. 만약 난이도가 가장 높은 문제가 여러 개라면 문제 번호가 큰 것으로 출력합니다.    
>x가 -1인 경우 문제 리스트에서 난이도가 가장 낮은 문제의 번호를 출력합니다. 만약 난이도가 가장 낮은 문제가 여러 개라면 문제 번호가 작은 것으로 출력합니다.    
>명령어 rc는 문제 리스트에 문제가 하나 이상 있을 때만 주어집니다. x는 반드시 1 또는 -1으로만 주어집니다.    
>ad P L : 문제 리스트에 난이도가 L인 문제 번호 P를 추가합니다.    
>이전에 문제 리스트에 있던 문제 번호가 다른 난이도로 다시 들어 올 수 있습니다.    
>sv P L : 추천 문제 리스트에서 난이도가 L인 문제 번호 P를 제거합니다.    
>명령어 sv는 추천 문제 리스트에 난이도가 L이고 문제 번호가 P인 문제가 있을 때만 주어집니다.    
>위 명령어들을 수행하는 문제 추천 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에 추천 문제 리스트에 있는 문제의 개수 n이 주어집니다.    
>두 번째 줄부터 n+1 줄까지 문제 번호 P와 난이도 L가 공백을 두고 주어집니다.    
>n+2 번째 줄은 입력될 명령문의 개수 m이 주어집니다.    
>n+m+3 번째 줄부터 m개의 위에서 설명한 명령문이 입력됩니다.    
>* 1 ≤ n, P ≤ 100,000   
>* 1 ≤ L ≤ 100, L은 자연수
>* 1 ≤ m ≤ 10,000
>
>**출력 형식**    
>rc 명령이 주어질 때마다 문제 번호를 한 줄씩 출력합니다. 최소 한번의 rc 명령어가 들어옵니다.

**풀이** : P, L이 주어질 때 이를 (L, P) 튜플로 묶어 treeset에 저장해 해결한다.

```python
from sortedcontainers import SortedSet
n = int(input())
arr = [
    tuple(reversed(list(map(int, input().split())))) # (L, P) 튜플을 리스트에 저장
    for _ in range(n)
]
m = int(input())
queries = [
    list(map(str, input().split()))
    for _ in range(m)
]

s = SortedSet(arr) # treeset으로

# 명령 수행
for query in queries:
    if query[0] == 'rc':
        if query[1] == '1':
            print(s[-1][1])
        else:
            print(s[0][1])
    elif query[0] == 'ad':
        s.add((int(query[2]), int(query[1]))) # int()로 감싸는 것 잊지 말기 (query의 원소들은 모두 str형이므로)
    elif query[0] == 'sv':
        if (int(query[2]), int(query[1])) in s:
            s.remove((int(query[2]), int(query[1])))
```

