# 프로그래머스 2단계 위장

def solution(clothes):
    answer = 1
    cloth_num = dict()
    
    # {의상 종류 : 옷 개수, ...}
    for i, j in clothes: 
        if j in cloth_num:
            cloth_num[j] += 1
        else:
            cloth_num[j] = 1
    
    for num in cloth_num.values(): 
        answer *= (num + 1) # 계산
    
    return answer - 1 # 최소 한 개의 의상은 입음
