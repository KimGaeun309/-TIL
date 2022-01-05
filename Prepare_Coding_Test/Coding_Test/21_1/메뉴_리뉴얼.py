# 프로그래머스 2단계 메뉴 리뉴얼

from itertools import combinations
from collections import Counter # [a, a, b, c] -> {a:2, b:1, c:1}

def solution(orders, course):
    answer = []
    
    for num in course: 
        menu_count = [] 
        for order in orders: # 조합 만들기
            new_menu = combinations(sorted(order), num) #sorted() 문자열정렬,리스트로 리턴
            menu_count += new_menu # menu_count 리스트에 만들어진 조합을 저장.
            #[('A', 'C'), ('C', 'D'), ......]
        
        menu_count = Counter(menu_count) # {('A', 'C'): 4, ('C', 'D'): 3, .....}
        
        # menu_count 가 빈 딕셔너리가 아니고 요소의 갯수의 최댓값이 1이 아닐 때
        if len(menu_count) != 0 and max(menu_count.values()) != 1:
            # value 값이 최댓값인 조합을 answer에 추가
            for menu in menu_count: 
                if menu_count[menu] == max(menu_count.values()): # menu의 개수가 최댓값
                    answer += [str.join("", menu)] # -> 문자열로 바꾸어 answer에 추가
    answer.sort() # 오름차순 정리 후 리턴
    return answer
