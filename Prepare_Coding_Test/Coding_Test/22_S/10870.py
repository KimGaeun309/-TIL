# 백준 10870 피보나치 수 5

def fibonacci(N):
  if N <= 1:
    return N
  return fibonacci(N-1) + fibonacci(N-2)

n = int(input())

print(fibonacci(n))
