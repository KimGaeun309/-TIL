def QuickSelect(L, k):
	if len(L) == 1:
		return L[0]
	p = L[0]
	A, M, B = [], [], []

	for x in L:
		if x < p: 
			A.append(x)
		elif x > p: 
			B.append(x)
		else: 
			M.append(x)

	if len(A) >= k: 
		return QuickSelect(A, k)
	elif len(A)+len(M) < k: 
		return QuickSelect(B, k - len(A) - len(M))
	else:
		return p

n, k = map(int, input().split())

L = list(map(int, input().split()))

answer = QuickSelect(L, k)

print(answer)
