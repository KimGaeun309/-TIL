"""
<알고리즘 설명>
이 알고리즘은 A[0] ~ A[i] 까지의 리스트에서의 m(i, j) 합을 Answer[i] 에 저장하며 해를 구하는 알고리즘입니다.
Answer[j]의 값은 for loop 을 돌며 m(0, j) + m(1, j) + ... + m(j, j) 를 answer 에 저장해두었다가 Answer[j] = Answer[j-1] + answer 로 구하는데, A[j] 가 A[0]~A[j] 중 최소일 때 m(i, j) 는 항상 A[j] 라는 점과, A[j] 가 A[0]~A[j] 중 최소가 아닌 경우, m(i, j) 는 i==j 이면 A[j] 이고, A[i]~A[j] 중 최소 원소가 있으면 최소 원소라는 점을 이용해 수행시간을 줄였습니다. 
<수행시간>
1. Worst Case
이 알고리즘은 A = [1, 2, 3, 4, 5, 6, 7, 8] 과 같이 서로 다른 수들이 오름차순으로 주어질 때 최악의 수행시간을 가집니다. 이 경우의 수행시간은 1 + 2 + ... + (n-2), 따라서 O(n^2) 입니다.
2. Best Case
이 알고리즘은 A = [10, 10, 8, 8, 7, 7, 6, 5, 4, 4, 2, 1, 1] 과 같이 내림차순으로 주어질 때 최적의 수행시간을 가집니다. 이 경우 이중 for loop이 실행되지 않으므로 수행시간은 O(n) 입니다.
"""
def solve(A):
	n = len(A)
	
	Answer = [A[0]] # Answer[i] 에 A[0] ~ A[i] 의 리스트에 대한 답 저장
	

	min_idx = 0 # A의 (지금까지 탐색한 원소 중) 가장 작은 원소의 인덱스 저장

	for j in range(1, n): # m(i, j) 찾기
		answer = 0  # i = 0 ~ j 인 m(i, j) 합 저장
		if A[j] <= A[min_idx]: # 1. A[j]가 min_idx인 경우, m(i, j)는 항상 A[j] 이다.
			min_idx = j
			answer += (A[min_idx] * (j+1))
		
		else:   # 2. A[j] 가 min-idx가 아닌 경우
			answer += A[j] # 2-1. i == j 일때 최소는 A[k] 이고
			answer += (A[min_idx] * (min_idx + 1)) # 2-2. i 와 j 사이에 min_idx가 있을 때 최소는 A[min_idx] 이고
			tmp_idx = j  # 2-3. i 와 j 사이에 min_idx가 없을 때 최소 원소의 인덱스를 tmp_idx 에 저장하고
			for i in range(j-1, min_idx, -1): # i == j-1 부터 min_idx 직전까지 감소시켜주며 확인
				if A[tmp_idx] > A[i]: 
					tmp_idx = i
				answer += (A[tmp_idx])

		Answer.append(Answer[j-1] + answer)
			
	return Answer[n-1]
	
A = [int(x) for x in input().split()]
print(solve(A))



