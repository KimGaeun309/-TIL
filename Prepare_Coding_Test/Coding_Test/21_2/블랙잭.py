# 백준 2798 블랙잭

n, m = map(int, input().split())
L = list(map(int, input().split()))

maximum = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            tmp = L[i] + L[j] + L[k]
            if tmp > maximum and tmp <= m:
                maximum = tmp
print(maximum)
