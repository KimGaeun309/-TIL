# 프로그래머스 월간 챌린지 시즌3 n^2배열 자르기

def solution(n, left, right):
    answer = []

    while left <= right:
        r = left // n
        c = left % n
        answer.append(max(r, c)+1)
        left += 1
    
    return answer
