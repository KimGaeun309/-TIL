# 프로그래머스 - 전화번호 목록

phone_prefix = set()

def add_prefix(string, length):
    if length <= 0: return
    phone_prefix.add(string)
    add_prefix(string[:length-1], length-1)

def solution(phone_book):
    answer = True
    
    for phone_number in phone_book:
        add_prefix(phone_number[:len(phone_number)-1], len(phone_number)-1)
        
    for phone_number in phone_book:
        if phone_number in phone_prefix:
            answer = False
            break
    
    return answer
