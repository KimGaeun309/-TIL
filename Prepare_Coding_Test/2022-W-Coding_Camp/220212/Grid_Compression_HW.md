## 점 개수 세기 3
>수직선 상의 서로 다른 위치에 n개의 점에 주어졌을 때, q개의 질의에 대해 각각 구간 내 점의 개수를 출력하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 n과 q가 공백을 사이에 두고 주어집니다.    
>두 번째 줄에는 수직선 상 n개의 점의 위치가 공백을 사이에 두고 주어집니다.
>세 번째 줄 부터는 q개의 줄에 걸쳐 구간에 대한 정보 a_i, b_i 값이 공백을 사이에 두고 주어집니다. 이는 a_i ≤ x ≤ b_i 를 만족하는 위치에 있는 점의 개수를 세어야 함을 의미합니다.    
>단, 중복되는 점은 주어지지 않으며, 주어지는 모든 a_i, b_i 값에 해당하는 위치에는 항상 점이 놓여있음을 가정해도 좋습니다.   
>* 1 ≤ n, q ≤ 100,000   
>* -10^9 ≤ 주어지는 점의 위치 ≤ 10^9
>* 10^9 ≤ a_i ≤ b_i ≤ 10^9
>
>**출력 형식**    
>q개의 질의에 대해 각 구간 내에 놓여있는 점의 개수를 한 줄에 하나씩 출력합니다.

**풀이** : `점 point가 i번째로 작다면 mapper[point] = i` 로 초기화한 mapper 딕셔너리를 활용해서 구간 내에 놓인 점의 개수를 빠르게 구할 수 있다.

```python
from sortedcontainers import SortedSet
n, q = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
queries = [
    tuple(map(int, input().split()))
    for _ in range(q)
]

points = SortedSet(arr) # 트리셋 사용해 정렬

mapper = dict() # mapper
cnt = 1 # 몇 번째로 작은 점인지 확인하기 위한 변수
for point in points: # 작은 점부터 차례대로
    mapper[point] = cnt # 몇 번째 점인지를 빠르게 찾을 수 있도록 mapper 딕셔너리에 저장
    cnt += 1

for s, e in queries: 
    n_s, n_e = mapper[s], mapper[e]
    print(n_e - n_s + 1) # 구간에 있는 점의 개수 출력
```
