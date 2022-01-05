# 프로그래머스 3단계 최고의 집합

def solution(n, s):
    answer = []
    if n > s:
        answer.append(-1)
    else:
        for i in range(n - (s%n)):
            answer.append(s//n)
        for j in range(s%n):
            answer.append(s//n+1)
    return answer
