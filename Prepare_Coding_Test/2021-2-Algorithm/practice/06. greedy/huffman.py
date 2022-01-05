from heapq import *

f = list(map(int, input().split()))

H = []
n = len(f)
for i in range(n):
	heappush(H, (f[i], str(i)))

while len(H) > 1:
	a = heappop(H)
	b = heappop(H)
	heappush(H, (a[0]+b[0], '( ' + a[1] + ' ' + b[1] + ' )'))

tree_string = heappop(H)[1]

tree_list = tree_string.split()

# 괄호 검사하며 비트수 계산해 nbits 리스트에 저장
nbits = [0] * n
bit = 0
for t in tree_list:
	if t == '(':
		bit += 1
	elif t == ')':
		bit -= 1
	else:
		nbits[int(t)] = bit
		
		
# nbits에 저장된 값을 토대로 정답 구하기
answer = 0
for i in range(n):
	answer += (f[i] * nbits[i])

print(answer)

