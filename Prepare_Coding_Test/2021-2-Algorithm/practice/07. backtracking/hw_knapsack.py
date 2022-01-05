def frac_knapsack(i, size):
	total = 0
	for f, idx in F:
		if idx < i:
			continue
		if size <= 0:
			break
		if S[idx] <= size:
			size -= S[idx]
			total += P[idx]
		else:
			total += (f * size)
			size = 0
	return total
	
def knapsack(i, size):
	global MP
	if i >= n or size <= 0:
		return 
	p = 0
	s = 0
	for j in range(i):
		if x[j] == 1:
			p += P[j]
			s += S[j]
			
	# x[i] = 1을 따라가야하는지 결정
	if S[i] <= size:
		B = frac_knapsack(i+1, size-S[i])
		
		if p + P[i] + B > MP:
			if p + P[i] > MP:
				MP = p + P[i]
			x[i] = 1
			knapsack(i+1, size-S[i])
			
	# x[i] = 0을 따라가야하는지 결정
	x[i] = 0
	B = frac_knapsack(i+1, size)
	if p + B > MP:
		x[i] = 0
		knapsack(i+1, size)

K = int(input())
n = int(input())
S = list(map(int, input().split()))
P = list(map(int, input().split()))
x = [0] * n
MP = 0

F = []
for i in range(n):
	F.append((P[i] / S[i], i))
	
F.sort(reverse=True)
		
knapsack(0, K)
print(MP)


