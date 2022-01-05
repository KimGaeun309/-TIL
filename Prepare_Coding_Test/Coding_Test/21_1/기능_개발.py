
# 프로그래머스 2단계 기능개발

def solution(progresses, speeds):
    answer = []
    day = 1
    i = 0
    while i < len(progresses):
        cnt = 0
        while i < len(progresses):
            if progresses[i] + speeds[i] * day >= 100:
                i += 1
                cnt += 1
            else:
                day += 1
                break
        if cnt != 0:
            answer.append(cnt)

    return answer
