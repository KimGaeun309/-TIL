# 프로그래머스 레벨1 모의고사 
# 완전탐색

def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(len(answers)):
        if s1[i % 5] == answers[i]:
            cnt1 += 1
        if s2[i % 8] == answers[i]:
            cnt2 += 1
        if s3[i % 10] == answers[i]:
            cnt3 += 1
            
    max_cnt = max(cnt1, cnt2, cnt3)
    if cnt1 == max_cnt: answer.append(1)
    if cnt2 == max_cnt: answer.append(2)
    if cnt3 == max_cnt: answer.append(3)
    
    return answer
