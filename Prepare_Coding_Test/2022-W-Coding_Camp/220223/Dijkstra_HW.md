### 각 정점까지의 최단 경로 3
>n개의 정점이 존재하고 m개의 간선의 양 끝 정점과 가중치가 주어질 때, 1번 정점에서 다른 모든 정점으로 가는 최단 경로를 구하는 프로그램을 작성해보세요. 이때 주어지는 정점과 간선들로 구성되는 그래프는 단방향 그래프라고 가정합니다.    
>**입력 형식**    
>첫 번째 줄에 정점의 개수 n과 간선의 개수 m이 공백을 두고 주어집니다.    
>두 번째 줄부터 m개의 줄에 걸쳐, 각 간선의 시작 정점의 번호, 끝 정점의 번호, 그리고 해당 간선에 주어진 가중치가 공백을 두고 주어집니다. 단, 동일한 간선이 여러 번 주어지는 경우는 없다고 가정해도 좋습니다.    
>* 1 ≤ n ≤ 100
>* 1 ≤ m ≤ 1,000
>* 1 ≤ 간선의 가중치 ≤ 10
>
>**출력 형식**    
>첫 번째 줄부터 n - 1개의 줄에 걸쳐, 1번 정점에서 출발하여 2번 정점, 3번 정점, ..., n번 정점까지 이동하기 위한 최단 거리를 한 줄에 하나씩 출력합니다. 만약 도달이 불가능하다면 -1을 출력합니다.

**풀이** : V(=n)가 10000개를 넘지 않는다면 O(|V|^2) 시간으로 풀어도 된다. 그래프를 인접행렬로 나타낸 뒤 for 문 안에서 지금까지 방문하지 않은 정점들 중 가장 거리가 가까운 정점을 찾아 방문했음을 표시한다. 
그리고 그 정점에 연결된 간선들을 확인하며 그 간선을 통해 가는 거리가 현재 저장된 거리보다 짧다면 값을 갱신해준다.

```python
import sys
INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))
graph = [
    [0] * (n+1)
    for _ in range(n+1)
]
visited = [False] * (n+1)
dist = [INT_MAX] * (n+1)

for _ in range(m):
    s, e, w = tuple(map(int, input().split()))
    graph[s][e] = w

dist[1] = 0 # 1번 정점부터 시작

for i in range(1, n+1):
    # 가장 작은 정점 칮기
    min_idx = -1  # visited[1] 이 False라는 보장이 없으므로 -1로 시작
    for j in range(1, n+1):
        if visited[j]:
            continue
        if min_idx == -1 or dist[j] < dist[min_idx]:
            min_idx = j
    
    visited[min_idx] = True # 가장 작은 정점에 방문한 것으로 표시
    
    # 가장 작은 정점에 연결된 간선들을 보며 최단 거리 값 갱신
    for j in range(1, n+1):
        if graph[min_idx][j] == 0: # 간선이 없는 경우
            continue
        # 간선이 있는 경우
        if dist[j] > dist[min_idx] + graph[min_idx][j]:
            dist[j] = dist[min_idx] + graph[min_idx][j]

# 1번 정점에서 다른 모든 정점들로 가는 최단 거리 출력
for i in range(2, n+1):
    if dist[i] == INT_MAX:
        print(-1)
    else:
        print(dist[i])
```

### 각 정점까지의 최단 경로
>n개의 정점이 존재하고 m개의 간선의 양 끝 정점과 가중치가 주어질 때, k번 정점에서 다른 모든 정점으로 가는 최단 경로를 구하는 프로그램을 작성해보세요. 이때 주어지는 정점과 간선들로 구성되는 그래프는 양방향 그래프라고 가정합니다.    
>**입력 형식**    
>첫 번째 줄에 정점의 개수 n과 간선의 개수 m이 공백을 두고 주어집니다.    
>두 번째 줄에 k가 주어집니다.    
>세 번째 줄부터 m개의 줄에 걸쳐, 각 간선의 양 끝 정점의 번호와 해당 간선에 주어진 가중치가 공백을 두고 주어집니다. 중복되는 간선은 주어지지 않는다고 가정해도 좋습니다.  
>* 1 ≤ n ≤ 20,000
>* 1 ≤ m ≤ 300,000
>* 1 ≤ k ≤ n
>* 1 ≤ 간선의 가중치 ≤ 10
>
>**출력 형식**    
>첫 번째 줄부터 n개의 줄에 걸쳐, k번 정점에서 출발하여 1번 정점, 2번 정점, ..., n번 정점에 도달하기 위한 최단 거리를 한 줄에 하나씩 출력합니다. 만약 도달하는 것이 불가능하다면 -1을 출력합니다.

**풀이** : V(=n)의 개수가 20000개이므로 우선순위 큐를 이용해 다익스트라를 구현해 O(|E|log|V|) 만에 거리를 구한다. 그래프를 연결리스트로 표현하고 우선순위 큐를 이용해 최솟값을 뽑는다.


```python
import heapq, sys
INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))
k = int(input())
graph = [
    [] for _ in range(n+1)
]
dist = [INT_MAX] * (n+1)
pq = []

# 양방향 그래프
for _ in range(m):
    s, e, w = tuple(map(int, input().split()))
    graph[s].append((e, w))
    graph[e].append((s, w))

dist[k] = 0 # k번부터 시작
heapq.heappush(pq, (0, k)) # k번 미리 넣어두기 (거리, 정점 번호)

while pq:
    min_dist, min_idx = heapq.heappop(pq)

    # 하나의 정점에 대해 여러 개의 거리가 pq에 저장되어있을 수 있기 때문에
    if dist[min_idx] != min_dist: # 굳이 확인할 필요가 없는 경우는 흘려보내기
        continue

    # 가장 작은 정점에 대해 
    for target_idx, target_dist in graph[min_idx]:
        # 그와 연결된 간선들을 확인해보며 dist[target_idx] 갱신하고 pq에 넣기
        new_dist = dist[min_idx] + target_dist
        if dist[target_idx] > new_dist:
            dist[target_idx] = new_dist
            heapq.heappush(pq, (new_dist, target_idx))

for i in range(1, n+1):
    if dist[i] == INT_MAX:
        print(-1)
    else:
        print(dist[i])
```

### 가장 오래 걸리는 학생
>N개의 서로 장소가 있습니다. 1번부터 N - 1번 장소에는 학생이 한 명씩 살고 있고, N번 장소는 학교입니다. 두 개의 장소를 연결하는 간선은 없거나, 있다면 최대 1개만 있으며 주어지는 모든 간선은 방향성을 갖지 않습니다. 간선마다 길이가 주어지며, 각 학생은 등교시 최단거리로 학교로 이동한다고 합니다. 모든 학생은 거리 1을 이동하는 데 1초의 시간이 걸린다 했을 때, 학교에 등교하는 데 가장 오래 걸리는 학생의 소요 시간을 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 N(장소의 개수)과 M(간선의 개수)이 공백을 사이에 두고 차례대로 주어집니다.    
>두 번째 줄에는 간선을 이루고 있는 두 장소의 번호 i, j와 간선의 길이 d가 각각 공백을 사이에 두고 차례대로 주어집니다.    
>모든 학생이 등교하는 것이 가능함을 가정해도 좋습니다.
>* 1 ≤ N ≤ 100,000
>* 1 ≤ M ≤ 100,000
>* 1 ≤ 간선의 길이 ≤ 1,000
>
>**출력 형식**    
>첫 번째 줄에 가장 등교하는 데 오래 걸리는 학생의 소요 시간을 출력합니다.

**풀이** : 다른 모든 정점에서 한 정점으로 가는 거리를 구하고 싶은 경우, 단방향 그래프이면 방향을 모두 반전시켜주고, 양방향이면 그대로 한 정점에서 다른 모든 정점으로 가는데 필요한 거리를 구하면 된다.

```python
import heapq, sys
INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))
graph = [
    [] for _ in range(n+1)
]
dist = [INT_MAX] * (n+1)
visited = [False] * (n+1)
pq = []

for _ in range(m):
    s, e, w = tuple(map(int, input().split()))
    graph[s].append((e, w))
    graph[e].append((s, w))


dist[n] = 0 # n번부터
heapq.heappush(pq, (0, n)) # n번 미리 넣어두기 (거리, 정점 번호)

while pq:
    min_dist, min_idx = heapq.heappop(pq)

    # 하나의 정점에 대해 여러 개의 거리가 pq에 저장되어있을 수 있기 때문에
    if dist[min_idx] != min_dist: # 굳이 확인할 필요가 없는 경우는 흘려보내기
        continue

    # 가장 작은 정점에 대해 
    for target_idx, target_dist in graph[min_idx]:
        # 그와 연결된 간선들을 확인해보며 dist[target_idx] 갱신하고 pq에 넣기
        new_dist = dist[min_idx] + target_dist
        if dist[target_idx] > new_dist:
            dist[target_idx] = new_dist
            heapq.heappush(pq, (new_dist, target_idx))

answer = 0

for i in range(1, n+1):
    if dist[i] != INT_MAX:
        answer = max(answer, dist[i])

print(answer)
```

### 최단 거리 9
>n개의 정점과 m개의 간선에 대한 정보로 각 간선의 길이가 주어질 때, 정점 A에서 정점 B까지의 최단 거리와 그 때의 경로를 구하는 프로그램을 작성해보세요. 이때 주어지는 정점과 간선들로 구성되는 그래프는 양방향 그래프라고 가정합니다.    
>**입력 형식**    
>첫 번째 줄에 정점의 개수 n, 간선의 개수 m 이 공백을 두고 주어집니다.    
>두 번째 줄부터 m개의 줄에 걸쳐 각 간선 양쪽 끝 정점의 번호와 해당 간선의 길이가 공백을 사이에 두고 주어집니다. 단, 동일한 간선이 여러 번 주어지는 경우는 없다고 가정해도 좋습니다.    
>m+2 번째 줄에는 구하려는 도시 A와 B의 정점 번호가 공백을 사이에 두고 주어집니다.    
>* 1 ≤ n ≤ 1,000
>* 1 ≤ m ≤ 100,000
>* 1 ≤ 각 간선의 길이 ≤ 100,000
>
>**출력 형식**    
>첫 번째 줄에 정점 A에서 정점 B까지의 최단 거리를 출력합니다.    
>두 번째 줄에 최단 거리로 이동하기 위해 거쳐야 하는 경로 내 도시들의 방문 순서를 순서대로 공백을 사이에 두고 출력합니다. 최단 거리를 만족하는 경로는 오직 하나 뿐임을 가정해도 좋습니다.

**풀이** : 경로는 도착점을 시작으로 path 리스트를 사용해 시작점까지 거슬러 가며 거쳐가는 점들을 적어주고 리스트를 뒤집으면 구할 수 있다.

```python
import heapq, sys
INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))
graph = [
    [] for _ in range(n+1)
]
dist = [INT_MAX] * (n+1)
visited = [False] * (n+1)
pq = []

for _ in range(m):
    s, e, w = tuple(map(int, input().split()))
    graph[s].append((e, w))
    graph[e].append((s, w))

A, B = tuple(map(int, input().split()))

path = [0] * (n+1) # 경로 구하기 위한 리스트

dist[A] = 0 # A번부터
heapq.heappush(pq, (0, A)) # A번 미리 넣어두기 (거리, 정점 번호)

while pq:
    min_dist, min_idx = heapq.heappop(pq)

    # 하나의 정점에 대해 여러 개의 거리가 pq에 저장되어있을 수 있기 때문에
    if dist[min_idx] != min_dist: # 굳이 확인할 필요가 없는 경우는 흘려보내기
        continue

    # 가장 작은 정점에 대해 
    for target_idx, target_dist in graph[min_idx]:
        # 그와 연결된 간선들을 확인해보며 dist[target_idx] 갱신하고 pq에 넣기
        new_dist = dist[min_idx] + target_dist
        if dist[target_idx] > new_dist:
            dist[target_idx] = new_dist
            path[target_idx] = min_idx  # 경로 저장
            heapq.heappush(pq, (new_dist, target_idx))

print(dist[B]) # 최단거리 출력

# 끝점을 x로 두고
x = B
vertices = [] # 경로 저장할 리스트
vertices.append(x)

# 시작점에 도착할 때까지 추적
while x != A:
    x = path[x]
    vertices.append(x)

# 경로 출력
for num in vertices[::-1]:
    print(num, end=' ')
```

### 최단 거리 11
>n개의 정점과 m개의 간선에 대한 정보로 각 간선의 길이가 주어질 때, 정점 A에서 정점 B까지의 최단 거리와 그 때의 경로를 구하는 프로그램을 작성해보세요. 이때 주어지는 정점과 간선들로 구성되는 그래프는 양방향 그래프라고 가정합니다.    
>**입력 형식**    
>첫 번째 줄에 정점의 개수 n, 간선의 개수 m 이 공백을 두고 주어집니다.    
>두 번째 줄부터 m개의 줄에 걸쳐 각 간선 양쪽 끝 정점의 번호와 해당 간선의 길이가 공백을 사이에 두고 주어집니다. 단, 동일한 간선이 여러 번 주어지는 경우는 없다고 가정해도 좋습니다.    
>m+2 번째 줄에는 구하려는 도시 A와 B의 정점 번호가 공백을 사이에 두고 주어집니다.    
>* 1 ≤ n ≤ 1,000
>* 1 ≤ m ≤ 100,000
>* 1 ≤ 각 간선의 길이 ≤ 100,000
>
>**출력 형식**    
>첫 번째 줄에 정점 A에서 정점 B까지의 최단 거리를 출력합니다.    
>두 번째 줄에 최단 거리로 이동하기 위해 거쳐야 하는 경로 내 도시들의 방문 순서를 순서대로 공백을 사이에 두고 출력합니다. 만약 최단 거리를 만족하는 경로가 여러 개라면, 그 중 사전순으로 가장 앞선 경로를 출력합니다. 사전순으로 앞서다는 말은 현재 위치에서 최단 경로로 이동할 수 있는 경우가 여러 가지라면, 그 중 정점의 번호가 가장 작은 경우를 선택해야 함을 뜻합니다.

**풀이** : 최단 경로를 만족하는 경로가 여러 가지라면 그 중 사전순으로 가장 빠른 경로를 출력해야 한다. 이 경우 모든 간선의 방향을 뒤집고 도착점을 시작점으로 해서 다익스트라를 사용해 최단 거리를 구한다. 
그 다음 시작점부터 1번부터 n번까지 순회하며 최단경로 상에 위치할 수 있는 정점들을 찾아 출력하고 이동하기를 도착점에 도달할 때까지 반복한다.

```python
import sys
INT_MAX = sys.maxsize

# 입력받기
n, m = tuple(map(int, input().split()))
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    s, e, w = tuple(map(int, input().split()))
    graph[s][e] = w # 양방향!
    graph[e][s] = w
a, b = tuple(map(int, input().split()))

visited = [False] * (n+1) # 방문한 정점 표시하기 위한 리스트
dist = [INT_MAX] * (n+1) # 최단 거리 저장하기 위한 리스트
dist[b] = 0  # b를 시작점으로 삼고 다익스트라 진행

# 다익스트라
for _ in range(1, n+1):
    # 아직 방문하지 않은 정점 중 가장 가까운 정점 찾기
    min_idx = -1
    for j in range(1, n+1):
        if visited[j]:
            continue
        if min_idx == -1 or dist[j] < dist[min_idx]:
            min_idx = j
        
    # 방문 표시
    visited[min_idx] = True

    # 가장 가까운 정점에 연결된 간선들 모두 확인하며 최단거리 갱신
    for j in range(1, n+1):
        if graph[min_idx][j] == 0:
            continue
        if dist[j] > dist[min_idx] + graph[min_idx][j]:
            dist[j] = dist[min_idx] + graph[min_idx][j]

print(dist[a])  # a에서 b까지으 최단 거리 출력

x = a   # 현재 노드를 a(시작점)로 설정
print(x, end=' ') # 시작점 출력

# x가 도착점에 도달할 때까지 반복
while x != b:
   # 1에서 n까지 순서대로 살피며 다음 경로가 될 수 있는 정점을 찾으면 x값 갱신하고 break
    for i in range(1, n+1):
        if graph[x][i] == 0:
            continue
        if dist[i] + graph[x][i] == dist[x]:
            x = i
            break # 다음 경로 정점 구한 뒤 break 꼭 해주기

    print(x, end=' ') # 이번 경로 출력
```
