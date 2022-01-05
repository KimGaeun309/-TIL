L = []
n = int(input()) 
for i in range(n): # L 입력받기
	a, b = map(int, input().split())
	L.append((a, -1)) # 왼쪽 끝 점은 음수
	L.append((b, 1)) # 오른쪽 끝 점은 양수
	
L.sort() # 좌표 순서대로 오름차순 정렬되는데, 같은 좌표를 가지는 점은 왼쪽 끝 점이 더 먼저 위치하도록 정렬됨.

answer = 0
stick = 0
i = 0 # L 을 탐색하는 데 사용할 변수 (인덱스로 활용)
while i < 2*n:
	tmp = L[i][0] # 현재 확인하고 있는 좌표
	while i < 2*n and L[i][0] == tmp and L[i][1] < 0: # 현재 확인하는 좌표에 있는 시작점의 개수 세어 stick 증가
		i += 1
		stick += 1
	answer = max(answer, stick) # answer update (maximum 값으로 유지)
	while i < 2*n and L[i][0] == tmp and L[i][1] > 0: # 현재 확인하는 좌표에 있는 끝점의 개수 세어 stick 감소
		i += 1
		stick -= 1
		
print(answer)

"""
<알고리즘 설명>
구간의 왼쪽 끝 점 a와 오른쪽 끝 점 b를 입력받아서 (a, -1), (b, 1) 를 리스트 L에 넣어주고 L을 오름차순으로 정렬합니다. 그러면 L은 끝 점들의 좌표 순서대로 정렬되는데, 같은 좌표이면 a가 b보다 먼저 위치하도록 정렬됩니다. 이를 이용해 while문에서 같은 좌표에 있는 왼쪽 끝 점들의 개수만큼 stick에 더해주고 answer를 update해준 후 같은 좌표에 있는 오른쪽 긑 점들의 개수만큼 stick에 빼줍니다.
<수행 시간 분석>
L을 정렬할 때는 O(nlogn)시간이 걸리고, 답을 구하기 위해 L을 탐색할 때는 i가 0부터 2*n-1이 될 떄까지 진행되므로 O(n) 시간이 걸립니다. 따라서 이 알고리즘의 수행 시간은 총 O(nlogn)입니다.
"""
