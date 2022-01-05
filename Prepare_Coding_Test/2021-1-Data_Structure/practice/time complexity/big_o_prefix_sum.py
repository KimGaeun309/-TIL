import time, random

# 이중 for문으로 prefix sum 구함 O(n^2)
def prefixSum1(X, n):
	S = []
	
	for i in range(n):
		S.insert(i, 0)	
		for j in range(i-1):
			S[i] += X[j]
		
	return S

# 하나의 for문으로 구함 O(n)
def prefixSum2(X, n):
	S = [X[0]]
	for i in range(1, n, 1):
		S.insert(i, S[i-1]+X[i])

	return S
	
random.seed()		# random 함수 초기화
n = int(input())  # n 입력받음

X = []
for i in range(n):   # 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
	X.append(random.randint(-999, 999))

# prefixSum1 의 수행시간 측정
before = time.process_time()
prefixSum1(X, n)
after = time.process_time()
print(after-before)

# prefixSum2 의 수행시간 측정
before = time.process_time()
prefixSum2(X, n)
after = time.process_time()
print(after-before)

