# 백준 17952 과제는 끝나지 않아!

import sys
answer = 0
S = []

n = int(sys.stdin.readline())

for i in range(n):
    try:
        select, A, T = map(int, sys.stdin.readline().split())
    except:
        select = 0
    if select == 1:
        S.append([A, T])
    if S:
        S[-1][1] -= 1
        if S[-1][1] == 0:
            answer += S[-1][0]
            S.pop()

print(answer)
