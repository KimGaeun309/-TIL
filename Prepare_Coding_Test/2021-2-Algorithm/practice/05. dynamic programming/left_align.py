def leftAlign(W, words):
	DP = [0]
	n = len(words)
	for i in range(n): # word[i]까지의 최소 패널티 DP[i+1] 구하기
		DP.append(DP[i] + (W - len(words[i]))**3)

		for j in range(i-1, -1, -1): # 마지막 문장 범위 조정
			# 마지막 문장 길이 계산
			tmp = i - j 
			for k in range(j, i+1, 1): 
				tmp += len(words[k])
			# DP[i+1]의 값을 최소로 유지
			if tmp <= W:
				DP[i+1] = min(DP[j] + (W - tmp)**3, DP[i+1])
			else: # 문장의 길이가 W 초과 -> break
				break

	return DP[n]

W = int(input())
words = input().split()
print(leftAlign(W, words))

'''
<DP 점화식>
DP[i]에 첫 번째 단어부터 i번째 단어까지 왼쪽 맞춤을 한 최소 panalty 값 저장
DP[i] = min(DP[j] + (j+1)번째 단어부터 i번째 단어까지 한 줄로 만들 경우 그 줄의 panalty 값) (j = i-1, i-2, ...)

<알고리즘의 수행시간> - leftAlign 함수의 수행시간
for i in range() 에서 n번, 그 안에 있는 for j in range()에서 최대 W/2번(모든 단어의 길이가 1일 경우), 그 안에 for k in range() 에서 i-j 만큼 연산하므로, 총 수행시간은 O(W^2 * n)입니다.
'''
