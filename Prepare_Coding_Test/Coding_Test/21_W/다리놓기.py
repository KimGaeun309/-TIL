# 백준 1010 다리놓기

def solution(N, M): # M개 중 N개 고르는 가짓수
    mother, child = 1, 1
    for i in range(1, N+1, 1):
        mother *= i
    for i in range(M-N+1, M+1, 1):
        child *= i
    return child // mother

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(solution(n, m))
