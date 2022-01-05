def max_sum(A):
	L = [0]

	for i in range(len(A)):
		L.append(L[i] + A[i])
		
	maximum = L[1] - L[0]
	
	for j in range(1, len(L), 1):
		for i in range(j):
			tmp = L[j] - L[i]
			if tmp > maximum:
				maximum = tmp
	return maximum
	
	# 최대 구간 합 리턴

A = [int(x) for x in input().split()]
sol = max_sum(A)
print(sol)
