# 백준 11047 동전 0

'''
그리디 알고리즘으로 풀이
'''

n, k = map(int, input().split())
C = []
for i in range(n):
    C.append(int(input()))

answer = 0

for i in range(len(C)-1, -1, -1):
    if k <= 0:
        break
    answer += (k // C[i])
    k %= C[i]

print(answer)
