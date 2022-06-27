# 프로그래머스 1단계 신고 결과 받기

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    reported_dict = {}
    reporter_dict = {}
    for id in id_list:
        reported_dict[id] = set()
        reporter_dict[id] = set()
        
    for str in report:
        reporter, reported = str.split()
        reported_dict[reported].add(reporter)
        reporter_dict[reporter].add(reported)
        
    for i in range(len(id_list)):
        for reported in reporter_dict[id_list[i]]:
            if len(reported_dict[reported]) >= k:
                answer[i] += 1
    
    return answer
