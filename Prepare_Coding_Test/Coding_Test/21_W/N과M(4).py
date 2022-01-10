# 백준 15652 N과 M (4)

"""
if answer and answer[-1] > i:
            continue
를 추가해 항상 오름차순인 수열만 만들어지도록 한다.
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
        if answer and answer[-1] > i:
            continue
        answer.append(i)
        Choose()
        answer.pop()


Choose()
