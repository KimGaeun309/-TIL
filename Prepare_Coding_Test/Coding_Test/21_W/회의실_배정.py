# 백준 1931 회의실 배정

'''
(끝나는 시간, 시작하는 시간) 튜플들을 리스트에 저장해 오름차순으로 정렬하면 강의가 빨리 끝나는 순서로 정렬되는 점과 그리디 알고리즘을 이용해 풀었다.
'''

n = int(input())
L = []
for i in range(n):
    a, b = map(int, input().split())
    L.append((b, a))

L.sort()

answer = 0
last_time = 0

for i in range(len(L)):
    if last_time <= L[i][1]:
        answer += 1
        last_time = L[i][0]
print(answer)

