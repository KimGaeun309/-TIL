### 가장 많이 겹치는 구간
>일직선 위에 n개의 구간이 주어졌을 때, 구간이 가장 많이 겹치는 부분에서 몇 개의 구간이 겹치는지를 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에 구간의 개수 n이 주어집니다.    
>두 번째 줄부터 n개의 줄에 걸쳐 각 줄에 각 구간을 나타내는 정보 (x_1, x_2) 값이 공백을 사이에 두고 주어집니다.    
>단, 주어지는 x값들은 모두 다름을 가정해도 좋습니다.    
>* 1 ≤ n ≤ 100,000
>* 1 ≤ x_1 < x_2 ≤ 200,000
>
>**출력 형식**    
>가장 많이 겹치는 구간의 횟수를 출력합니다.

```python
n = int(input())
lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

line = [0] * 200000 # +1 또는 -1을 해줄 리스트

for x, y in lines:
    line[x-1] += 1 # 인덱스 0 ~ 199999 까지이므로 1씩 빼서 시작점은 +1,
    line[y-1] -= 1 #   끝점은 -1

max_cnt = 0

k = 0

for i in range(200000): # 리스트의 값을 계속 더해가면 그때그때의 겹치는 구간의 개수를 구할 수 있다.
    k += line[i]

    max_cnt = max(max_cnt, k) # 겹치는 구간 중 최댓값을 갱신

print(max_cnt) # 최댓값 출력
```

### 서로 다른 구간의 수
>수직선 상에 n개의 구간이 주어졌을 때, 모든 구간을 합친 이후의 남아 있는 서로 다른 구간의 수를 구하는 프로그램을 작성해보세요.     
>**입력 형식**    
>첫 번째 줄에는 n이 주어집니다.    
>두 번째 줄 부터는 n개의 줄에 걸쳐 각 구간을 나타내는 정보 a_i, b_i 값이 공백을 사이에 두고 주어집니다. 주어지는 모든 좌표 값은 서로 다름을 가정해도 좋습니다.    
>* 3 ≤ n ≤ 100,000
>* 1 ≤ a_i < b_i ≤ 10^9
>
>**출력 형식**    
>주어진 모든 구간이 합쳐진 이후 남아 있는 서로 다른 구간의 수를 출력합니다.

```python
n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

points = []

for idx, (x, y) in enumerate(arr): 
    points.append((x, +1, idx)) # (점 위치, 시작점인지끝점인지, 인덱스)
    points.append((y, -1, idx))

points.sort()

segs = set()

answer = 0
for x, v, idx in points:
    if v ==  +1: # 시작점이 주어졌는데
        if not segs: # 남아있는 구간이 없다면 
            answer += 1 # 합쳐진 구간에서의 새로운 구간이 주어진 것
        segs.add(idx) # 시작점이 주어졌다면 set에 인덱스를 add
    else:
        segs.remove(idx) # 끝점이 주어졌다면 set에서 인덱스를 remove

print(answer) 
```

### 가장 많이 겹치는 구간 2
> 일직선 위에 n개의 구간이 주어졌을 때, 구간이 가장 많이 겹치는 부분에서 몇 개의 구간이 겹치는지를 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에 구간의 개수 n이 주어집니다.    
>두 번째 줄부터 n개의 줄에 걸쳐 각 줄에 각 구간을 나타내는 정보 (x_1, x_2) 값이 공백을 사이에 두고 주어집니다.    
>단, 주어지는 x값들은 모두 다름을 가정하여도 좋습니다.    
>* 1 ≤ n ≤ 100,000
>* 1 ≤ x_1 < x_2 ≤ 10^9
>
>**출력 형식**    
>가장 많이 겹치는 구간의 횟수를 출력합니다.

```python
n = int(input())
sections = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

points = [] # 각 점을 저장할 리스트 

for x1, x2 in sections:
    points.append((x1, 1)) # 시작점은 +1
    points.append((x2, -1)) # 끝점은 -1

points.sort() # 정렬

max_overlap = 0 # 답 구하기 위한 변수
overlap = 0 # 그때그때 겹치는 구간의 개수 구하기 위한 변수

for x, n in points:
    overlap += n
    max_overlap = max(max_overlap, overlap)

print(max_overlap)
```

### 겹치는 선분들
>수직선 위에 1부터 N까지 번호가 매겨진 N개의 선분이 있습니다. 선분 1은 원점에서 시작해서 M(1)만큼 왼쪽 혹은 오른쪽으로 그려집니다. 선분 2는 선분 1을 그리고 마친 지점에서 시작해서 M(2)만큼 왼쪽 혹은 오른쪽으로 그려집니다. 이런식으로 선분 i는 선분 i-1을 그리고 마친 지점에서 시작해 M(i)만큼 왼쪽 혹은 오른쪽으로 그려집니다. 각 선분의 길이와 그려진 방향이 주어질 때, 이 N개의 선분들이 K개 이상 겹치는 곳의 길이 합을 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 N과 K가 공백을 사이에 두고 차례대로 주어집니다.    
>두 번째 줄 부터는 N개 줄에 걸쳐 i+1번째 줄에 M(i)와 선분이 그려진 방향이 공백을 사이에 두고 차례대로 주어집니다. R은 오른쪽, L은 왼쪽을 뜻합니다.    
>* 1 ≤ K ≤ N ≤ 100,000
>* 원점으로부터 좌, 우 1,000,000,000 안에는 모든 선분들이 위치합니다.
>
>**출력 형식**    
>첫 번째 줄에 선분들이 K개 이상 겹치는 곳의 길이 합을 출력합니다.

```python
n, k = tuple(map(int, input().split()))
M = [
    tuple(input().split())
    for _ in range(n)
]

points = []
curr = 0

for length, direction in M:
    length = int(length)
    if direction == 'R':
        points.append((curr, 1)) # 1 은 시작점
        curr += length
        points.append((curr, -1)) # -1 은 끝점
    elif direction == 'L':
        points.append((curr, -1)) # -1 은 끝점
        curr -= length
        points.append((curr, 1)) # 1 은 시작점

points.sort()

overlap = 0 # 현재 위치에서 겹치는 선분의 개수 세는 변수
start_x = 0  # k개 이상 겹치는 구간의 길이를 구하기 위해
            # 구간이 시작하는 지점을 저장하기 위한 변수 
isNew = True # k개 이상 겹치는 구간의 시작점인지 아닌지 확인하기 위한 flag 
answer = 0 # 정답 (k개 이상 겹치는 구간의 길이)

for x, v in points:
    overlap += v
    
    if overlap >= k: # 현재 위치에서 겹치는 구간이 k 이상일 때
        # 만약 k개 이상 겹치는 구간이 시작하는 지점이라면
        if isNew == True:
            isNew = False # flag을 False로
            start_x = x
    else: # 현재 위치에서 겹치는 구간이 k 미만일 때
        # 만약 k개 이상 겹치던 구간이 끝나는 지점이라면
        if isNew == False: 
            isNew = True # flag 초기화
            answer += (x - start_x) # 정답 갱신

print(answer)
```

### 호텔 예약
>n명의 사람이 동일한 호텔에 투숙을 하는데, i번째 사람은 s_i 날에 들어와서 e_i 날에 나가게 됩니다. 서로 다른 사람끼리 같은 방을 쓸 수 없다 했을 때 n명의 예약을 문제 없이 처리하기 위해 필요한 최소 방의 수를 구하는 프로그램을 작성해보세요. 단, 한 사람이 나가는 날과 다른 사람이 들어오는 날이 일치하는 경우 두 사람은 같은 방에 머무를 수 없다고 가정합니다.
>**입력 형식**    
>첫 번째 줄에는 n이 주어집니다.    
>두 번째 줄 부터는 n개의 줄에 걸쳐 i번째 사람에 해당하는 s_i, e_i 정보가 공백을 사이에 두고 주어집니다.    
>* 1 ≤ n ≤ 100,000   
>* 1 ≤ s_i < e_i ≤ 10^9 
>
>**출력 형식**    
>문제 없이 모든 예약을 받기 위해 필요한 최소 방의 수를 출력합니다.

```python
n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

points = []

for s, e in arr:
    points.append((s, 1)) # 1이면 시작점
    points.append((e, 2)) # 2이면 끝점 

points.sort()

overlap = 0
max_overlap = 0

for x, v in points:
    if v == 1:
        overlap += 1
    elif v == 2:
        overlap -= 1
    
    max_overlap = max(max_overlap, overlap)

print(max_overlap)
```

### 구간 크기의 합
>수직선 상에 n개의 구간이 주어졌을 때, 모든 구간을 합친 이후의 총 구간 크기의 합을 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 n이 주어집니다.    
>두 번째 줄 부터는 n개의 줄에 걸쳐 각 구간을 나타내는 정보 a_i, b_i 값이 공백을 사이에 두고 주어집니다. 주어지는 모든 좌표 값은 서로 다름을 가정해도 좋습니다.
>* 3 ≤ n ≤ 100,000  
>* 1 ≤ a_i < b_i ≤ 10^9
>**출력 형식**    
>주어진 모든 구간이 합쳐진 이후 각 구간 크기의 합을 출력합니다.

```python
n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

points = []

for idx, (a, b) in enumerate(arr): # 인덱스값도 튜플에
    points.append((a, 1, idx))
    points.append((b, -1, idx))

points.sort()

S = set() 
answer = 0
start_x = 0 # 구간의 시작점 저장할 변수

for x, v, i in points:
    if v == 1: 
        if not S: # 시작점이면서 S가 비어있다면 겹치는 구간의 시작
            start_x = x
        S.add(i)
    else:
        S.remove(i)
        if not S: # 끝점이면서 S가 비었다면 겹치는 구간의 끝
            answer += (x - start_x)

print(answer)
```

### 최대 구간의 크기
>수직선 상에 n개의 구간이 주어졌을 때, 모든 구간을 합친 이후 남아 있는 구간들 중 가장 큰 구간의 크기를 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 n이 주어집니다.    
>두 번째 줄 부터는 n개의 줄에 걸쳐 각 구간을 나타내는 정보 a_i, b_i 값이 공백을 사이에 두고 주어집니다. 주어지는 모든 좌표 값은 서로 다름을 가정해도 좋습니다.    
* 3 ≤ n ≤ 100,000
>* 1 ≤ a_i < b_i ≤ 10^9
> 
>**출력 형식**    
>주어진 모든 구간이 합쳐진 이후 남아있는 구간들 중 가장 큰 구간의 크기를 출력합니다.

```python
n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

points = []

for idx, (a, b) in enumerate(arr): # 인덱스값도 튜플에
    points.append((a, 1, idx))
    points.append((b, -1, idx))

points.sort()

S = set() 
answer = 0
start_x = 0 # 구간의 시작점 저장할 변수

for x, v, i in points:
    if v == 1: 
        if not S: # 시작점이면서 S가 비어있다면 겹치는 구간의 시작
            start_x = x
        S.add(i)
    else:
        S.remove(i)
        if not S: # 끝점이면서 S가 비었다면 겹치는 구간의 끝
            answer = max(answer, x - start_x) # 최댓값 갱신

print(answer)
```

### 컴퓨터 이용시간
>n명의 사람이 컴퓨터를 하려 합니다.    
>컴퓨터에는 1번 부터 순서대로 번호가 매겨져 있고, 컴퓨터 이용 시 남아있는 자리 중 번호가 가장 작은 자리에 앉는 것이 규칙입니다.    
>모든 사람이 기다리지 않고 이용할 수 있는 컴퓨터의 최소 개수와 컴퓨터별로 몇 명의 사람이 그 컴퓨터를 이용하였는지를 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에 사람의 수를 나타내는 n이 주어집니다.    
>두 번째 줄부터 n+1 번째 줄 까지 각 사람의 컴퓨터 시작 시간 p와 종료 시간 q가 주어집니다.    
>시작 시간과 종료 시간이 다른 사람과 겹치는 경우는 없습니다.   
>* 1 ≤ n ≤ 100,000
>* 0 ≤ p ≤ q ≤ 1,000,000
>
>**출력 형식**
>첫 번째 줄에 n명의 사람에 대해 각 사람이 사용한 컴퓨터의 번호를 순서대로 공백을 사이에 두고 출력합니다.

```python
import heapq # min heap 사용

n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

answers = [0] * n # answers[i] 에 i번째 사람이 이용한 컴퓨터 번호 저장.

computers = [] # 컴퓨터 번호가 1부터 n까지 최소 힙으로 저장됨 (초기값으로)
for i in range(1, n+1): 
    heapq.heappush(computers, i)

points = [] # 각 점 저장 
for idx, (p, q) in enumerate(arr):
    points.append((p, 1, idx)) # 시작점
    points.append((q, -1, idx)) # 끝점

points.sort() # 각 점 저장된 리스트 정렬

for x, v, idx in points: # 정렬된 점들 확인
    # 시작점이라면
    if v == 1:
        # computers에서 가장 작은 번호를 가진 컴퓨터의 번호가
        computer = heapq.heappop(computers) # (heappop!)
        # idx번째 사람이 이용하는 컴퓨터 번호이다
        answers[idx] = computer    
    # 끝점이라면
    else:
        # idx번째 사람이 이용한 컴퓨터 번호를
        computer = answers[idx]
        # 다시 computers에 heappush해 다음 사람이 이용할 수 있도록 함.
        heapq.heappush(computers, computer)        

# 정답 출력
for answer in answers:
    print(answer, end=" ")
```

