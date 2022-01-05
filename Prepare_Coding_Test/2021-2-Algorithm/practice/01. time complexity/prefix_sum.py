import time, random

def prefixSum1(X, n):
	S = []
	for i in range(n):
		S.append(0)
		for j in range(i+1):
			S[i] += X[j]	
	return S
	# code for prefixSum1
	
def prefixSum2(X, n):
	S = [X[0]]
	for i in range(n-1):
		S.append(S[i]+X[i+1])
	return S
	# code for prefixSum2
	
random.seed()		# random 함수 초기화
# n 입력받음
n = int(input())
# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
X = []
for i in range(n):
	X.append(random.randint(-999, 999))
# prefixSum1 호출
s_1 = time.process_time()
prefixSum1(X, n)
e_1 = time.process_time()

# prefixSum2 호출
s_2 = time.process_time()
prefixSum2(X, n)
e_2 = time.process_time()

# 두 함수의 수행시간 출력
print(e_1 - s_1)
print(e_2 - s_2)
