def max_sum(A, left, right):
	if left >= right:
		return A[left]
	m = (left + right) // 2
	L = max_sum(A, left, m)
	R = max_sum(A, m+1, right)
	sumL = A[m]
	maxL = A[m]
	for i in range(m-1, -1, -1):
		sumL += A[i]
		if sumL > maxL:
			maxL = sumL
	sumR = A[m+1]
	maxR = A[m+1]
	for i in range(m+2, right+1, 1):
		sumR += A[i]
		if sumR > maxR:
			maxR = sumR
	M = maxL + maxR
	
	return max(L, M, R)		
	
	# A[left], ..., A[right] 중 최대 구간 합 리턴

A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)
