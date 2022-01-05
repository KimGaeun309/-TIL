# 백준 7568 덩치

n = int(input())
P = list() # (몸무게, 키) 저장할 리스트
L = list() # 등수 저장할 리스트

for i in range(n):
    P.append(tuple(map(int, input().split())))

for i in range(n):
    cnt = 1  # i 번째 사람보다 덩치가 큰 사람의 수 + 1 (= 등수) 저장
    for j in range(n):
        if (P[i][0] < P[j][0]) and (P[i][1] < P[j][1]):
            cnt += 1
    L.append(cnt)

for i in range(n):
    print(L[i], end=' ')
