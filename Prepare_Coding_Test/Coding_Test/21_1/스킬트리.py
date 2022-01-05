# 프로그래머스 2단계 스킬트리

def solution(skill, skill_trees):
    answer = 0
    
    for i in skill_trees:
        skill_index = [] #스킬의 인덱스값 저장할 리스트
        
        for j in skill:
            if i.find(j) == -1: #해당 스킬이 스킬트리에 없으면 큰 수 저장
                skill_index.append(100)
            else: #해당 스킬이 스킬트리에 있으면 스킬의 인덱스값을 리스트에 저장
                skill_index.append(i.find(j))

        #스킬의 인덱스값이 저장된 리스트가 오름차순이면 가능한 스킬트리
        if sorted(skill_index) == skill_index:
            answer += 1
        
    return answer
