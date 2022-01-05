# 백준 2231 분해합

def decomposition(n):
    for m in range(n):
        answer = m
        tmp = m
        while m > 0:
            tmp += (m % 10)
            m //= 10
        if tmp == n:
            return answer
    return 0

n = int(input())
print(decomposition(n))



