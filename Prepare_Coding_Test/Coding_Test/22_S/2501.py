# 백준 2501 약수 구하기
N, K = map(int, input().split())
cnt = 0
answer = 0
for i in range(1, N+1):
  if N % i == 0:
    cnt += 1
  if cnt == K:
    answer = i
    break

print(answer)
