L = []
n = int(input())
for i in range(n):
	a, b = map(int, input().split())
	L.append((b, a)) # 오른쪽 끝점 기준으로 오름차순 정렬하기 위해.

L.sort()

answer = 1 # L[0][0] 위치에 못 하나는 무조건 꽂음
prev = 0
for curr in range(1, n, 1):
	if L[curr][1] > L[prev][0]:
		answer += 1
		prev = curr
		
print(answer)

"""
<알고리즘 설명>
오른쪽 끝 점이 가장 먼저 나오는 곳에 못을 꽂고, 이보다 뒤에 왼쪽 끝 점이 있는 막대들 중에서 다시 오른쪽 끝 점이 가장 먼저 나오는 곳에 못을 꽂도록 하면 가장 적은 수의 못으로 모든 막대를 고정시킬 수 있습니다.
왼쪽 끝 점 a와 오른쪽 끝 점 b를 입력받아 (b, a) 튜플로 만들어 리스트 L에 넣어준 후 L을 오름차순으로 정렬합니다. 그 다음으로 L[0]의 오른쪽 끝 점에는 못을 무조건 꽂아야 하므로 answer를 1로 초기화해두고, for 문으로 i=1부터 i=n-1까지 반복하면서 curr번째 막대가 prev번째 막대와 겹치지 않는다면 answer를 증가시키고 prev를 curr로 재정의합니다. 그러면 for문을 빠져나왔을 때 answer에 최소 개수가 저장되어 있을 것입니다.
<수행 시간>
리스트 L을 오름차순으로 정렬하는데 O(nlogn) 시간, for문에서 i=1부터 n-1까지 반복하므로 O(n) 시간이 걸립니다. 따라서 이 알고리즘의 수행 시간은 총 O(nlogn) 입니다.
"""
