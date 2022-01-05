def reverse(L, a):
	n = len(L)
	if a < n//2: # if a < n-a-1: 도 통과됨
		L[a], L[n-a-1] = L[n-a-1], L[a]
		reverse(L, a+1)
    
L = list(input())  # 문자열을 입력받아 리스트로 변환
reverse(L, 0)
print(''.join(str(x) for x in L))
