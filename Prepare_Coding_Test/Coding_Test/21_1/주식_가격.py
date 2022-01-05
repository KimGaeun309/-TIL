# 프로그래머스 2단계 주식 가격

def solution(prices):
    answer = []
    for i in range(len(prices)):
        sec = 0
        for j in range(i+1,len(prices)):
            sec+=1
            if prices[i] <= prices[j]:
                continue
            else:
                break
        answer.insert(i, sec)
    return answer
