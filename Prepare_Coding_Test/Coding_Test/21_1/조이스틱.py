# 프로그래머스 2단계 조이스틱

def solution(name):
    answer = 0
    #위아래로 움직이는 횟수
    for i in range(len(name)):
        a = ord('Z') - ord(name[i]) + 1
        b = ord(name[i]) - ord('A')
        answer += min(a,b)
    
    #왼쪽 오른쪽으로 움직이는 횟수
    l = len(name)
    move = l - 1 #첫 글자부터 오른쪽으로 끝까지 갈 때
    
    for i in range(l): 
        n_i = i + 1 #첫 글자는 A이든 아니든 기본적으로 찍힌다
        while n_i < l and name[n_i] == 'A': #A가 몇 개?
            n_i += 1
        move = min(move, i + l - n_i + i)
        
    answer += move
    
    return answer
