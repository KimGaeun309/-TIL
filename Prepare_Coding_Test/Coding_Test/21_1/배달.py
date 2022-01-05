# 프로그래머스 2단계 배달

def solution(N, road, K):
    answer = 0
    arr = [[0 for _ in range(N)] for _ in range(N)]
    visited = {} # 방문 여부 확인 딕셔너리
    queue = []
    
    for i in range(N):
        visited[i+1] = False
        
    for i, j, k in road:
        if arr[i-1][j-1] == 0 and arr[j-1][i-1] == 0:
            arr[i-1][j-1], arr[j-1][i-1] = k, k
        else:
            if k < arr[i-1][j-1]:
                arr[i-1][j-1], arr[j-1][i-1] = k, k
    
    
    queue.append((1, 0))
    visited[1] = True
    
    while queue:
        pop = queue.pop(0)
        if pop[1] <= K:
            answer += 1

        for i in range(N):
            dist = arr[pop[0]-1][i]
            if dist > 0 and visited[i+1] == False:
                queue.append((i+1, pop[1] + dist))
                visited[i+1] = True
            
 

    return answer
