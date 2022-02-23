
### 각 정점까지의 최단 경로 2
>n개의 정점이 존재하고 m개의 간선의 양 끝 정점과 가중치가 주어질 때, 모든 정점 쌍 (i, j) 에 대해 정점 i 에서 출발하여 정점 j에 도착하기 위한 최단 거리를 구하는 프로그램을 작성해보세요. 단, 주어진 정점과 간선으로 이루어지는 그래프는 방향 그래프 입니다.    
>**입력 형식**    
>첫 번째 줄에 정점의 개수 n과 간선의 개수 m이 공백을 두고 주어집니다.    
>두 번째 줄부터 m개의 줄에 걸쳐, 각 간선을 연결하는 두 정점의 번호와 가중치가 공백을 두고 주어집니다. 두 정점을 연결하는 간선이 여러 개 주어질 수도 있습니다.  
>* 1 ≤ n ≤ 100
>* 1 ≤ m ≤ 100,000
>* 1 ≤ 간선의 가중치 ≤ 100,000
>**출력 형식**    
>모든 정점 쌍 i, j에 대한 최단거리를 출력합니다.     
>n개의 줄에 걸쳐 각 정점에서 출발하여 1번 정점, 2번 정점, ..., n번 정점까지 도달하기 위한 최단거리 값을 공백을 사이에 두고 출력합니다. 만약 불가능하다면 -1을 출력합니다.    

**풀이** : 모든 정점에 대한 최단 거리를 구하기 위해 플로이드 워셜 알고리즘을 사용한다.

```python
import sys
INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))
edges = []
for _ in range(m):
    edges.append(tuple(map(int, input().split())))

dist = [[INT_MAX] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신까지의 거리 0으로 설정
for i in range(1, n+1):
    dist[i][i] = 0

# 직접 연결된 간선들의 정보에 맞춰 dist 업데이트
for i, j, w in edges:
    dist[i][j] = min(dist[i][j], w)
    
# Floyd - Warshall
for k in range(1, n+1): # 경유할 정점 
    for i in range(1, n+1): # 시작점
        for j in range(1, n+1): # 끝점
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) # 갱신

# 정답 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == INT_MAX:
            print(-1, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
```

### 행렬로 주어진 간선
>n개의 정점이 존재하는 그래프에서 각 간선의 정보가 행렬로 주어집니다.    
>i 행의 j 열에 해당하는 정수가 1이라면, 정점 i에서 정점 j로 가는 간선이 놓여있다는 뜻 입니다.    
>모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에 정점의 개수 n이 주어집니다.    
>두 번째 줄부터 n개의 줄에 걸쳐 간선의 정보가 행렬로 주어집니다. 각 줄마다 각 행에 해당하는 정보가 공백을 사이에 두고 주어집니다.    
>i 행의 j 열에 해당하는 정수가 1이라면, 정점 i에서 정점 j로 가는 간선이 놓여있다는 뜻 이고, 0이라면, 정점 i에서 정점 j로 직접 연결된 간선이 없다는 뜻 입니다.   
>*  1 ≤ n ≤ 100
>
>**출력 형식**    
>첫 번째 줄부터 n개의 줄에 걸쳐 행렬로 표현하는데, 정점 i에서 j로 가는 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력합니다. i와 j가 동일한 곳은 항상 도달이 가능하므로 1을 출력합니다.

**풀이** : 모든 정점에 대해 경로의 유무를 확인해야 하므로 플로이드 워셜 알고리즘을 사용해 경로가 있으면 dist[i][j]를 1로 만든다.

```python
n = int(input())
edges = []
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    graph[i] = [0] + list(map(int, input().split()))

# 자기 자신으로 가는 경로는 항상 있으므로 1로 설정
for i in range(1, n+1):
    graph[i][i] = 1

# 플로이드 워셜 알고리즘
for k in range(1, n+1): # 경유할 정점
    for i in range(1, n+1): # 시작점
        for j in range(1, n+1): # 끝점
            if graph[i][k] and graph[k][j]: # k를 경유해 i에서 j로 갈 수 있다면
                graph[i][j] = 1             # graph[i][j]를 1로 설정

# 정답 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j], end=' ')
    print()
```

