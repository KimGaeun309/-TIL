# 백준 15649 N과 M (1)

"""
백트래킹 이용해 풀이.
"""

N, M = map(int, input().split())
answer = []


def Print():
    for i in range(M):
        print(answer[i], end=' ')
    print()


def Choose():
    for i in range(1, N+1):
        if len(answer) == M:
            Print()
            return
        if i not in answer:
            answer.append(i)
            Choose()
            answer.pop()


Choose()
