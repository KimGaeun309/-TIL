# 백준 1654 랜선 자르기

k, n = map(int, input().split())
L = []
for i in range(k):
    L.append(int(input()))

left = 1
right = max(L)

while left <= right:
    mid = (left + right) // 2
    newK = 0 # 잘라서 나온 랜선 개수 저장
    for i in range(k):
        newK += (L[i] // mid)

    if n <= newK: # 랜선 개수가 맞거나 더 큰 경우 랜선의 길이를 더 길게 할 수 있는지 확인하기 위해 탐색
        left = mid + 1
    else: # 랜선 개수가 부족한 경우 랜선의 길이를 줄여 탐색
        right = mid - 1

print(right)
