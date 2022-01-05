import random, time

# A리스트의 요소를 하나씩 불러와 B자료형에서 제거. B배열에 요소가 없어 에러가 나면 중복된 값.
def unique_n(A):
	B = set(A)
	for i in A:
		try:
			B.remove(i)
		except:
			print("NO")
			return
	print("YES")		

#A를 오름차순으로 정리해 요소들을 순서대로 다음 값과 비교해 중복 확인
def unique_nlogn(A):
	A.sort()
	for i in range(len(A)-1):
		if A[i] == A[i+1]:
				print("NO")
				return
	print("YES")

#중첩 for문을 이용해 요소들끼리 모두 비교
def unique_n2(A):
	for i in range(len(A)-1):
		for j in range(i+1, len(A)):
			if A[i] == A[j]:
				print("NO")
				return
	print("YES")

# input: 값의 개수 n
n = int(input())
# -n과 n 사이의 서로 다른 값 n 개를 랜덤 선택해 A 구성
A = random.sample(range(-n, n+1), n)

#n 수행시간 측정
s = time.process_time()
unique_n(A)
e = time.process_time()
print("n 수행시간 =", e-s)

#nlogn 수행시간 측정
s = time.process_time()
unique_nlogn(A)
e = time.process_time()
print("nlogn 수행시간 =", e-s)

#n2 수행시간 측정
s = time.process_time()
unique_n2(A)
e = time.process_time()
print("n^2 수행시간 =", e-s)

