# 백준 15650 N과 M (2)

"""
N과 M (1)에서는 출력할 수열을 저장하는 용도로 쓰였던 리스트 answer를 이번에는 숫자를 선택할지 말지 저장하는 용도로 사용하였다. 
(예시: answer = [0, 0, 1] 이면 3, [1, 0, 1] 이면 1 3)
"""

N, M = map(int, input().split())
answer = []

def Print():
    for i in range(N):
        if answer[i] == 1:
            print(i+1, end=' ')
    print()


def Choose(curr_num):
    if curr_num > N:
        cnt = 0
        for i in range(N):
            if answer[i] == 1:
                cnt += 1
        if cnt == M:
            Print()
        return

    answer.append(1)
    Choose(curr_num + 1)
    answer.pop()

    answer.append(0)
    Choose(curr_num + 1)
    answer.pop()



Choose(1)
