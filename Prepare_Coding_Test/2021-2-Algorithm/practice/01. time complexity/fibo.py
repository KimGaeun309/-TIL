def fibo(n):
	if n == 0 or n == 1:
		return 1
	a = 1
	b = 1
	while n > 1:
		c = a+b
		a = b
		b = c
		n -= 1
	return c

n = int(input())
print(fibo(n))

# n을 입력받은 후
# fibo(n) 호출!
# 리턴값을 출력함
