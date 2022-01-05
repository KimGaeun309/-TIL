'''
<이 DP 알고리즘의 점화식>
LIS(i)는 i번째 문자를 마지막 원소로 가지는 최장 증가 부문자열의 길이

LIS(k) = max(LIS(j)+1, LIS(k)) (j < k , seq[j] < seq[i])

<알고리즘 설명>
이 알고리즘에서는 LIS의 길이 lis 를 구하기 위해 DP[i] 에 i번째 문자를 마지막 원소로 가지는 최장 부문자열의 길이를 저장합니다. seq의 길이만큼 i를 0부터 증가시키는 for loop을 돌면서 DP[i] 의 값을 구하기 위해 j를 i-1부터 0까지 감소시키는 for loop을 도는데, seq[j] < seq[i] 이면 DP[j]+1 과 DP[i] 중 더 큰 수를 DP[i] 에 저장합니다. 모든 반복이 끝나고 DP 에 든 값 중 가장 큰 값이 lis 입니다.

DP에 저장된 값들을 이용해 최장 증가 부문자열을 구합니다. lis 의 DP 에서의 인덱스 값을 idx로 하고, x[idx] 를 1로 수정합니다. 그리고 i를 idx-1 부터 0까지 감소시키는 for loop에서 i번째 문자가 최장 증가 부문자열에 포함될 수 있다면 x[i] 도 1로 수정합니다.

<수행시간>
DP를 구하는데 사용된 이중 반복문에서 O(n^2) 시간, lis와 idx를 구하는데 O(n), x를 구하는데 사용된 반복문에서 O(n) 시간이 걸리므로, LIS_DP 함수의 총 수행 시간은 O(n^2)입니다.

'''
def print_IS(seq, x):
	for i in range(len(seq)):
		if x[i]: 
				print(seq[i], end="")
		else:
				print("_", end="")
	print()

def LIS_DP(seq):
	x = [0] * len(seq)
	DP = [0] * len(seq)
	
	# lis 구하기
	for i in range(len(seq)):
		DP[i] = 1
		for j in range(i-1, -1, -1):
			if (seq[j] < seq[i]):
				DP[i] = max(DP[i], DP[j] + 1)
	
	lis = max(DP)
	idx = DP.index(lis)
	
	# x 구하기
	x[idx] = 1
	for i in range(idx-1, -1, -1):
		if seq[i] < seq[idx] and DP[i] == DP[idx] - 1:
			idx = i
			x[i] = 1
	
	return lis, x

seq = input()  # 알파벳 소문자로만 구성된 string 하나가 입력된다
lis, x = LIS_DP(seq)
print(lis)
#print_IS(seq, x)
