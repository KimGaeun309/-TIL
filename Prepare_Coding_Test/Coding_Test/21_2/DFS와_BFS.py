# 백준 1260 DFS와 BFS

from collections import deque

n, m, start = map(int, input().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

def DFS(v):
    for curr_v in range(1, n+1):
        if graph[v][curr_v] == 1 and visited[curr_v] == False:
            print(curr_v, end=' ')
            visited[curr_v] = True
            DFS(curr_v)

def BFS():
    Q = deque([start])
    while Q:
        curr_v = Q.popleft()
        if visited[curr_v] == False:
            visited[curr_v] = True
            print(curr_v, end=' ')
        for next_v in range(1, n+1):
            if visited[next_v] == False and graph[curr_v][next_v] == 1:
                Q.append(next_v)

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

print(start, end=' ')
visited[start] = True
DFS(start)

visited = [False for _ in range(n+1)]
print()
BFS()

