# 최대공약수 구하기

# 큰 수에서 작은 수 빼가며 구하기
def gcd_sub(a, b):
	while a * b != 0:
		if a > b:
			a = a - b
		else:
			b = b - a
	return a+b

# gcd_sub의 worst case를 극복하기 위해 나머지 연산 적용하기
def gcd_mod(a, b):
	while a * b != 0:
		if a > b:
			a = a % b
		else:
			b = b % a 
	return a+b

# 재귀함수로 구현
def gcd_rec(a, b):
	if a*b == 0:
		return a+b
	if a > b:
		return gcd_rec(a%b, b)
	else:
		return gcd_rec(a, b%a)


# a, b를 입력받는다
# gcd_sub, gcd_mod, gcd_rec을 각각 호출하여, x, y, z에 리턴값을 저장한다
a,b = input().split()
a = int(a)
b = int(b)

x = gcd_sub(a,b)
y = gcd_mod(a,b)
z = gcd_rec(a,b)

print(x, y, z)
