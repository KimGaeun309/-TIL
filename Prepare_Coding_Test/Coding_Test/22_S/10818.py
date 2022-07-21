# 백준 10818 최소, 최대
N = int(input())
L = list(map(int, input().split()))
print(min(L), max(L))


N = int(input())
L = list(map(int, input().split()))
minimum, maximum = L[0], L[0]

for i in range(1, N):
  if minimum > L[i]:
    minimum = L[i]
  if maximum < L[i]:
    maximum = L[i]

print(minimum, maximum)