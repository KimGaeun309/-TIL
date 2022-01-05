def print_subset(x):
	print([A[i] for i in range(len(x)) if x[i]])

def subset_sum(k):
	global flag
	v_sum = 0
	for i in range(k):
		if x[i]:
			v_sum += A[i]
	if k == len(A):
		if v_sum == S:
			print_subset(x)
			flag = True
		elif x == [0] * len(A) and flag == False:
			print([])
	else:
		# code for x[k] = 1 and x[k] = 0
		if v_sum + A[k] <= S:
			x[k] = 1
			subset_sum(k+1)
		x[k] = 0
		subset_sum(k+1)

flag = False

A = list(set(int(x) for x in input().split()))
A.sort()
S = int(input()) 
x = [0]*len(A)
subset_sum(0)
