### 자연수 n개의 합
>1부터 n까지의 자연수의 합이 s이하인 경우 중 가능한 n의 최댓값을 구하는 프로그램을 작성해보세요.     
>**입력 형식**    
>첫 번째 줄에 자연수 s가 주어집니다.
>* 1 ≤ s ≤ 1,000,000,000
>
>**출력 형식**    
>가능한 n의 최댓값을 출력합니다.

**풀이** : 답을 기준으로 이진탐색을 해보자. 정답의 후보가 된다면 정답을 max()를 통해 갱신해주고 오른쪽으로 더 탐색한다. 정답의 후보가 아니라면 왼쪽으로 더 탐색한다.

```python
s = int(input())

left, right = 1, s
max_num = 0

while left <= right:
    mid = (left + right) // 2
    if mid * (mid + 1) / 2 <= s: # 합이 정답의 후보라면
        max_num = max(max_num, mid) # 갱신
        left = mid + 1 
    else:
        right = mid - 1

print(max_num)
```

### 정수 분배하기
>n개의 정수를 분배하여 같은 크기의 정수 k를 m개 만드려 할 때, 만들 수 있는 k값의 최댓값을 구하는 프로그램을 작성해보세요.    
>단, n개의 정수를 분배할 때는 제한 없이 정수를 분배해도 괜찮지만, 각 정수에서 분배하고 남은 정수들을 합쳐서 새로운 정수로 만들 수는 없습니다.    
>**입력 형식**    
>첫 번째 줄에 n, m이 공백을 두고 주어집니다.    
>두 번째 줄부터 n개의 줄에 걸쳐 한 줄에 정수가 하나씩 주어집니다.  
>* 1 ≤ n ≤ 10,000
>* 1 ≤ m ≤ 100,000
>* 1 ≤ n개의 정수의 크기 ≤ 100,000
>
>**출력 형식**    
>만들 수 있는 k값의 최댓값을 출력합니다.

**풀이** : is_possible() 함수를 만들어 특정 숫자가 답이 될 가능성이 있는지 없는지를 판별할 수 있게 한다. 그리고 이진탐색에 is_possible() 함수를 사용해 가능하다면 max()를 통해 정답을 
갱신하고 오른쪽으로 더 탐색한다. 불가능하다면 왼쪽으로 더 탐색한다.ㅣ

```python
import sys
INT_MAX = sys.maxsize
n, m = tuple(map(int, input().split()))
arr = [
    int(input())
    for _ in range(n)
]

def is_possible(num):
    cnt = 0
    for a in arr:
        cnt += (a // num)

    return cnt >= m

left, right = 1, INT_MAX
max_num = 0

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        max_num = max(max_num, mid)
        left = mid + 1
    else:
        right = mid - 1


print(max_num)
```

### 삼 오 무
>1부터 차례대로 숫자를 적는데, 3이나 5의 배수는 숫자 대신 "Moo"라고 적습니다. 예를 들어 1부터 16까지의 숫자를 적는다면 아래와 같습니다.    
>1, 2, Moo, 4, Moo, Moo, 7, 8, Moo, Moo, 11, Moo, 13, 14, Moo, 16    
>이 때, N번째로 적히는 숫자는 무엇인지 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에 N이 주어집니다.
>* 1 ≤ N ≤ 10^9
> 
>**출력 형식**     
>첫 번째 줄에 N번째로 적히는 숫자를 출력합니다.

**풀이** : 특정 숫자 mid에서 (mid // 3) 값과 (mid // 5) 값을 뺀 후 두 값에서 반복되어 빼진 값을 더하기 위해 (mid // 15) 를 더해 그 숫자가 3, 5에서 Moo를 적을 때 몇 번째 숫자인지를 
확인할 수 있도록 한다. 만약 위 식을 진행했을 때 나오는 값이 n보다 같거나 크다면 답이 될 가능성이 있으므로 답을 min()을 이용해 갱신하고 왼쪽으로 더 탐색한다. 만약 값이 n보다 작다면 
오른쪽으로 더 탐색한다.

```python
import sys
INT_MAX = sys.maxsize

n = int(input())

left, right = 1, INT_MAX
answer = INT_MAX

while left <= right:
    mid = (left + right) // 2
    if mid - mid // 3 - mid // 5 + mid // 15 >= n: # 답이 될 수 있는지 확인
        answer = min(answer, mid) # 답 갱신
        right = mid - 1 # 왼쪽으로 더 탐색
    else:
        left = mid + 1 # 오른쪽으로 더 탐색

print(answer)
```

### 최대 거리의 점
>수직선 위에 서로 다른 n개의 점이 있습니다.    
>이 n개의 점들 위에 m개의 물건을 설치한다고 할 때, 가장 인접한 두 물건의 거리를 가능한 크게 하여 설치하려고 합니다.    
>이 때 가장 인접한 두 물건의 거리의 최댓값을 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에 n, m이 공백을 두고 주어집니다.    
>두 번째 줄부터 n개의 줄에 걸쳐 각 점의 좌표가 한 줄에 하나씩 주어집니다.  
>* 2 ≤ n ≤ 200,000
>* 2 ≤ m ≤ n
>* 0 ≤ 점의 좌표 ≤ 1,000,000,000
>
>**출력 형식**    
>가장 인접한 두 물건의 거리의 최댓값을 출력합니다.

**풀이** : dist를 인수로 받아서 가장 인접한 두 물건의 거리가 dist 이상이도록 물건을 둘 수 있다면 True, 없다면 False를 반환하는 함수 is_possible을 정의한 후 dist로 전달할 숫자를 
이진탐색으로 정한다.

```python
import sys
INT_MAX = sys.maxsize
n, m = tuple(map(int, input().split()))
points = [
    int(input())
    for _ in range(n)
]

points.sort()

# dist 를 가장 인접한 두 물건의 거리로 정해두고 
# cnt로 최대 몇 개의 물건을 놓을 수 있는지 센 다음
# cnt가 m개 이상이라면 True, 미만이라면 False를 반환할 함수
def is_possible(dist):
    curr_dist = 0 # 두 물건 사이의 거리를 그때 그때 재기 위한 변수
    cnt = 1 # points[0]에는 물건을 무조건 넣는다고 가정
    for i in range(1, n):
        # i번째에 다음 물건을 놓는다고 가정하고 curr_dist 계산
        curr_dist += (points[i] - points[i-1])
        # curr_dist가 dist 이상이라면 물건을 놓을 수 있으므로 
        if curr_dist >= dist: 
            cnt += 1 # cnt 증가시키고
            curr_dist = 0 # curr_dist를 0으로 바꾸기

    # 반복문 빠져나온 후 cnt가 m 이상이라면 
    if cnt >= m:  # 가능하므로 True 반환
        return True
    # 그렇지 않다면 False 반환
    return False
    

left, right = 0, INT_MAX
answer = 0 # 최댓값으로 갱신!

while left <= right:
    mid = (left + right) // 2
    # mid를 가장 인접한 두 물건의 거리로 했을 때 진행 가능하다면 (m개 이상)
    if is_possible(mid): 
        answer = max(answer, mid) # 정답 갱신하고
        left = mid + 1 # 더 큰 숫자로 다시 탐색
    else: # 진행 불가능하다면 (m개 미만)
        right = mid - 1 # 더 작은 숫자로 다시 탐색

print(answer)
```

### 최소 통과 시간
>n개의 물건을 m개의 통로를 통해 통과시키려 합니다.    
>m개의 통로를 통과하는데 걸리는 시간이 각각 다를 때, n개의 물건을 모두 통과시키는데 걸리는 최소 시간을 구하는 프로그램을 작성해보세요.    
>단, 통로에 물건이 이동하고 있다면 그동안 다른 물건은 그 통로로 들어가지 못합니다.     
>**입력 형식**    
>첫 번째 줄에 n과 m이 공백을 두고 주어집니다.    
>두 번째 줄부터 m개의 줄에 걸쳐 각 통로를 통과하는데 걸리는 시간이 차례대로 한 줄에 하나씩 주어집니다.
>* 1 ≤ n, m ≤ 100,000
>* 1 ≤ 각 통로를 통과하는데 걸리는 시간 ≤ 10^9
> 
>**출력 형식**    
>n개의 물건을 모두 통과시키는데 걸리는 최소 시간을 출력합니다.

**풀이** : time을 인수로 받아서 time 시간 안에 물건을 모두 운반할 수 있는지 없는지를 판별할 함수 is_possible() 을 정의해 사용한다. 이진탐색에서 is_possible(mid) 가 True를 반환한다면
정답을 mid()을 사용해 갱신하고 `right = mid - 1` 로 더 작은 숫자를 더 탐색하고, False를 반환한다면 `left = mid + 1` 로 더 큰 숫자를 더 탐색한다.

```python
import sys
INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))
time_costs = [
    int(input())
    for _ in range(m)
]

# time 시간 안에 물건을 모두 운반하는 것이 가능하다면 True,
# 불가능하다면 False를 반환할 함수
def is_possible(time):
    cnt = 0
    for cost in time_costs:
        cnt += (time // cost)
    if cnt >= n:
        return True
    return False

left, right = 1, INT_MAX
answer = INT_MAX

while left <= right:
    mid = (left + right) // 2
    # 만약 mid 시간 안에 물건을 운반하는 것이 가능하다면
    if is_possible(mid):
        answer = min(answer, mid) # 정답 갱신하고
        right = mid - 1  # 더 작은 숫자로 탐색 진행
    else: # 불가능하다면
        left = mid + 1 # 더 큰 숫자로 탐색 진행

print(answer)
```

### 수영장 효율적으로 활용하기
>m개의 레인이 있는 수영장이 있습니다. 수영장을 효율적으로 이용하기 위하여 다음 조건에 맞춰 각 사람들 마다 사용할 레인을 정해주려고 합니다.    
>총 n명의 사람이 수영장을 이용하게 되며, 수영장에 도착한 순서대로 1부터 n까지 번호를 매깁니다.    
>1번 부터 n번까지의 사람에 대해 i번째 사람의 수영장 이용시간은 T_i 입니다.    
>레인별로 사람들을 할당합니다. 각 레인에는 1부터 m까지 번호가 매겨져 있고, 모든 사람들은 하나의 레인에만 할당 되어야 하며, 도착한 순서가 늦은 사람이 할당받은 레인 번호가 먼저 도착한 사람의 레인 번호보다 앞설 수 없습니다.    
>위의 조건을 만족시키며 레인별 사람들의 수영장 이용시간의 합들 중 최댓값을 최소화 하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 n과 m이 주어집니다.    
>두 번째 줄에는 사람 별 수영장 이용시간이 공백을 사이에 두고 주어집니다.
>* 1 ≤ n, m ≤ 100,000
>* 1 ≤ 이용 시간 ≤ 1,440
>**출력 형식**    
>첫 번째 줄에 가능한 각 레인 별 수영장 이용시간의 총합 중 최댓값의 최솟값을 출력합니다.

**풀이** : time을 인수로 받아 time을 각 레인 별 수영장 이용 시간의 총합 중 최댓값으로 잡았을 때 m개 이하의 레인으로 가능하다면 True, 불가능하다면 False를 반환하는 함수 is_possible()을 
정의해 활용한다.

```python
import sys
INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))
people = list(map(int, input().split()))

# 레인별 사람들의 수영장 이용시간의 합들 중 최댓값을 time으로 잡았을 떄
# m개 이하의 레인으로 수영장 이용이 가능한지 확인해주는 함수 
def is_possible(time):
    rail = 1
    curr_time = 0
    for i in range(n):
        if people[i] > time: # 만약 time 보다 한 사람의 이용 시간이 더 길다면
            return False     # False 반환
        # curr_time에 이번 사람의 이용 시간을 더해도 time을 넘지 않는다면
        if curr_time + people[i] <= time: 
            curr_time += people[i]     # curr_time에 이번 사람의 이용시간 더하기
        # time을 넘는다면
        else:
            rail += 1 # 새로운 레일 사용하기
            curr_time = people[i] # 이번 사람의 이용시간을 새로운 curr_time으로

    # 반복문 빠져나온 후 사용한 레일 수가 m개 이하라면 True 반환
    if rail <= m:
        return True
    # 초과라면 False 반환
    return False

left, right = 1, INT_MAX
answer = INT_MAX

while left <= right:
    mid = (left + right) // 2
    # mid 시간을 최댓값으로 잡았을 때 필요한 레일 수가 m개 이하라면
    if is_possible(mid): 
        answer = min(answer, mid) # 답 갱신하고 
        right = mid - 1     # 더 작은 수로 탐색 진행
    # m개 초과라면
    else:
        left = mid + 1      # 더 큰 수로 탐색 진행

print(answer)
```

### 겹치지 않는 선분위의 두 점
>수평선 위에 M개의 서로 겹치지 않는 선분이 있습니다. N개의 점들을 선분 위의 정수 점에 오도록 배치했을 때, 가장 가까운 두 점의 거리의 최댓값을 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에 N, M이 공백을 사이에 두고 차례대로 주어집니다.     
>두 번째 줄부터 M개의 줄에 걸쳐 각 선분의 양 끝점 a, b가 공백을 사이에 두고 차례대로 주어집니다.   
>* 2 ≤ N ≤ 10^5
>* 1 ≤ M ≤ 10^5
>* 0 ≤ a ≤ b ≤ 10^18 , a, b는 정수
>
>**출력 형식**     
>첫 번째 줄에 가장 가까운 두 점의 거리의 최댓값을 출력합니다.

**풀이** : 가장 가까운 두 점의 거리를 dist로 할 때 n개의 물건을 놓을 수 있는지를 판별할 함수 is_possible()을 정의한다. 이때 미리 lines를 정렬해야 한다. is_possible()에서 for문을 
통해 선분들을 하나씩 살피면서 해당 선분에 놓을 수 있는 점의 개수를 구하고 가장 마지막으로 놓여진 물건의 위치를 prev_x에 저장해주며 원하는 결과를 얻는다.

```python
import sys
INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))
lines = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

lines.sort() # 선분 정렬

# 가장 가까운 두 점의 거리를 dist로 할 때 n개의 물건을 놓을 수 있다면 True,
# 놓을 수 없다면 False를 반환하는 함수
def is_possible(dist):
    cnt = 0
    prev_x = lines[0][0] - dist
    # 각 선분의 시작점과 끝점을 가져오되
    for s, e in lines:
        # 가장 마지막을 놓은 물건의 위치에서 dist를 더한 값이 s보다 크다면
        s = max(s, prev_x + dist)  # s 를 그 값으로 바꾸고
        if s > e: # 만약 새로운 s가 e보다 커졌다면 continue
            continue
        # 선분의 길이에서 dist를 나눈 몫에 1을 더한 값이
        # 현재 선분에 놓을 수 있는 점의 개수이다.
        cnt += (e - s) // dist + 1
        # 새로 놓여진 점들을 토대로 마지막으로 놓인 점의 위치를 갱신해준다.
        prev_x = s + (e - s) // dist * dist

    # 반복문을 다 돌고 나서 놓을 수 있는 최대의 물건 개수 cnt가 n 이상이면
    if cnt >= n:    # True를 반환하고
        return True
    # n 미만이면 False를 반환한다.
    return False

left, right = 1, INT_MAX
answer = 0

while left <= right:
    mid = (left + right) // 2
    # 가능하다면 정답 갱신하고 더 큰 값을 탐색해본다.
    if is_possible(mid):
        answer = max(answer, mid)
        left = mid + 1
    # 불가능하다면 더 작은 값을 탐색해본다.
    else:
        right = mid - 1

print(answer)
```

### 가장 가까운 두 점 사이의 거리를 최대화하기
>수직선상에 n개의 선분이 주어졌을 때, 각 선분마다 그 위에 정확히 하나의 점을 잡아 x축 기준으로 가장 가까운 두 점 사이의 거리를 최대화하는 프로그램을 작성해보세요. 단, 한 선분이 다른 선분을 완전히 포함하는 경우는 절대 주어지지 않는다고 가정해도 좋습니다.    
>**입력 형식**    
>첫 번째 줄에는 n이 주어집니다.    
>두 번째 줄 부터는 n개의 줄에 걸쳐 각 선분의 나타내는 정보를 나타내는 x_1, x_2 값이 공백을 사이에 두고 주어집니다. 주어지는 모든 좌표 값은 서로 다름을 가정해도 좋습니다.
>* 3 ≤ n ≤ 100,000
>* 1 ≤ x_1 < x_2 ≤ 10^9
>
>**출력 형식**    
>가장 가까운 두 점 사이의 거리를 최대로 했을 때의 거리를 출력합니다.

**풀이** : dist를 인수로 받아 dist를 가장 가까운 두 점 사이 거리로 삼을 수 있다면 True, 없다면 False를 반환하는 함수 is_possible() 을 정의해 사용한다.

```python
import sys
INT_MAX = sys.maxsize

n = int(input())
lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

lines.sort() # 선분 정렬

# dist를 가장 가까운 두 점 사이 거리로 정했을 때 가능하다면 True,
# 불가능하다면 False 반환하는 함수
def is_possible(dist):
    # 첫번째 선분의 시작점에 점을 먼저 찍고 시작
    prev_x = lines[0][0] 
    # 두번째 선분부터 마지막 선분까지 확인
    for i in range(1, n): 
        x, y = lines[i]
        # 만약 마지막 점의 위치에 dist를 더했는데 이번 선분의 끝점을 초과한다면
        if prev_x + dist > y: # 이번 선분에 알맞은 점을 찍을 수 없다는 뜻이므로
            return False      # False 반환
        # 만약 알맞은 점을 찍을 수 있다면
        prev_x = max(prev_x + dist, x)  # 현재 선분에 찍을 점을 prev_x에 저장

    return True

left, right = 1, INT_MAX
answer = 0

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)
```

### 번호표를 든 N명의 사람
>1부터 N까지 번호표를 든 N명의 사람들이 있습니다. 사람들이 순서대로 무대에 올라와서 각자 d_i시간 동안 머무르며, 무대에는 한 번에 최대 K 명까지 올라올 수 있습니다. 처음에는 1번부터 K번 사람까지 올라와서 머무르다가 가장 먼저 무대를 끝낸 사람은 무대 아래로 내려가고 K+1번째 사람이 무대로 올라옵니다. 무대에는 남은 사람들이 K명 이하일 경우를 제외하고는 늘 K명의 사람들이 있습니다. 모든 사람이 무대에서 내려갈 때 까지 걸리는 시간이 T_max를 넘지 않도록 하려고 할 때, 가능한 K의 최솟값을 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에 N, T_max가 공백을 사이에 두고 차례대로 주어집니다.    
>두 번째 줄부터 N개의 줄에 걸쳐 i+1번째 줄에 i번 사람의 d_i 가 주어집니다. 
>* 1 ≤ N ≤ 10,000
>* 0 ≤ T_max ≤ 1,000,000
>* 1 ≤ d_i ≤ 100,000
>* K=N일 경우, T_max 가 무조건 만족되도록 값들이 주어집니다.
>
>**출력 형식**    
>첫 번째 줄에 모든 사람들이 무대에서 내려갈 때 까지 걸리는 시간이 T_max 를 넘지 않도록할 때, 가능한 K의 최솟값을 출력합니다.

**풀이** : k 를 인수로 받아 가능 여부를 판별하는 함수 is_possible()을 정의한다. 이 함수에서는 모든 사람이 무대에서 내려가기까지 걸리는 시간을 구해 t_max보다 같거나 작으면 True, 
크면 False를 반환하는데, 그 시간을 구하는데 heapq를 사용한다. 

```python
import heapq, sys
INT_MAX = sys.maxsize

n, t_max = tuple(map(int, input().split()))
people = [
    int(input())
    for _ in range(n)
]

# k 값을 받아 k명씩 무대에 선다고 가정할 때 걸리는 시간이 t_max를 넘으면 False,
# 넘지 않으면 True를 반환하는 함수
def is_possible(k):
    pq = []
    # k개를 heapq에 push
    for i in range(k):
        heapq.heappush(pq, people[i])
    # 아직 push하지 않은 원소 개수만큼 
    for i in range(k, n):  # heapq에서 pop한 수를 
        p = heapq.heappop(pq)  # 새로운 사람이 무대에 서야 하는 시간에 더해  
        heapq.heappush(pq, people[i] + p)     # 다시 push

    # 그렇게 나온 heapq의 수 중 가장 큰 값이 
    # 모든 사람이 무대에서 내려가기까지 걸리는 시간이므로 t_max 이하면 True 반환
    if max(pq) <= t_max:
        return True
    # t_max 초과면 False 반환
    return False

left, right = 1, n  # 정답은 1 ~ n 중에 있으므로 범위 이렇게 잡음
answer = INT_MAX # 정답 최솟값으로 갱신

while left <= right:
    mid = (left + right) // 2
    # 답의 후보라면
    if is_possible(mid): 
        answer = min(answer, mid) # 정답 갱신하고
        right = mid - 1    # 더 작은 수 탐색
    # 답의 후보가 아니라면
    else:
        left = mid + 1     # 더 큰 수 탐색

print(answer)
```
