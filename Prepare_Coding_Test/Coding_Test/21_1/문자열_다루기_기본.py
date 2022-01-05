# 프로그래머스 1단계 문자열 다루기 기본

def solution(s):
       
    answer = True
    
    if len(s) != 4 and len(s) != 6:
        return False
    
    for i in s:
        if i in '1234567890':
            continue
        else:
            return False
    return answer
