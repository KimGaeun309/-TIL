# 백준 12865 평범한 배낭

"""
동적계획법으로 kanpsack 알고리즘을 푸는 방법을 공부하였다.
"""

def knapsack(W, V, n, k):
   DP =  [[0 for _ in range(k+1)] for _ in range(n)]

   for j in range(k+1): # DP 테이블 첫째줄 채우기
       if W[0] <= j:
            DP[0][j] = V[0]

   for i in range(1, n, 1):
       for j in range(k+1):
           if W[i] <= j:
               DP[i][j] = max(DP[i-1][j], DP[i-1][j-W[i]]+V[i])
           else:
               DP[i][j] = DP[i-1][j]

   return DP[n-1][k]

n, k = map(int, input().split())
W, V = [], []

for i in range(n):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

print(knapsack(W, V, n, k))

