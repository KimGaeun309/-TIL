### 숫자 빠르게 찾기
>n개의 숫자가 오름차순으로 정렬된 상태로 주어집니다. 이후 m개의 숫자가 추가적으로 주어졌을 때, 각각의 숫자가 처음 주어진 n개의 숫자 중 몇 번째로 나온 숫자인지를 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 n, m이 공백을 두고 주어집니다.    
>두 번째 줄에는 n개의 숫자가 공백을 사이에 두고 주어집니다. 단, n개의 숫자는 오름차순으로 정렬되어 주어지며, 주어지는 모든 숫자는 서로 다름을 가정해도 좋습니다.    
>세 번째 줄 부터는 m개의 줄에 걸쳐 숫자가 한 줄에 하나씩 주어집니다.
>* 1 ≤ n, m ≤ 100,000
>* 1 ≤ 주어지는 값 ≤ 1,000,000,000
>
>**출력 형식**    
>m개의 줄에 걸쳐 주어진 각 숫자가 처음 주어진 n개의 숫자들 중 몇 번째 숫자로 나왔는지를 출력합니다. 만약 n개의 숫자 그 어디에도 나와있지 않는다면, -1을 출력합니다.

**풀이** : 이진탐색을 통해 O(logn) 시간 안에 오름차순 정렬된 리스트 안에서 타겟이 몇 번째로 등장했는지 알아본다.

```python
n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

# 이진탐색으로 몇 번째로 해당 숫자가 등장하는지 알려줄 함수
def binary_search(q):
    left, right = 0, n-1
    while left <= right: 
        mid = (left + right) // 2
        if arr[mid] == q:
            return mid+1
        elif arr[mid] > q:
            right = mid - 1
        else:
            left = mid + 1
    return -1 # 해당 숫자가 arr에 존재하지 않는다면 -1 리턴

for _ in range(m):
    quiz = int(input())
    print(binary_search(quiz))
```

### 숫자의 개수
?n개의 숫자가 오름차순으로 정렬된 상태로 주어집니다. 이후 m개의 숫자가 추가적으로 주어졌을 때, 각각의 숫자가 처음 주어진 n개의 숫자 중 몇 번 나왔는지를 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 n, m이 공백을 두고 주어집니다.    
>두 번째 줄에는 n개의 숫자가 공백을 사이에 두고 주어집니다. 단, n개의 숫자는 오름차순으로 정렬되어 주어지며, 동일한 숫자가 여러 번 주어질 수 있습니다.    
>세 번째 줄 부터는 m개의 줄에 걸쳐 숫자가 한 줄에 하나씩 주어집니다.   
>* 1 ≤ n, m ≤ 100,000
>* 1 ≤ 주어지는 값 ≤ 1,000,000,000
>
>**출력 형식**    
>m개의 줄에 걸쳐 주어진 각 숫자가 처음 주어진 n개의 숫자들 중 몇 번 나왔는지를 출력합니다.

**풀이** : 타겟 이상의 값이 처음으로 등장하는 위치를 반환하는 lower_bound라는 함수와 타겟을 초과하는 값이 처음으로 등장하는 위치를 반환하는 upper_bound라는 함수를 
만들어서 upper_bound(x) - lower_bound(x) 를 통해 x가 몇 번 나왔는지 알아낸다.

```python
n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

# 타겟 이상의 값이 처음으로 등장하는 위치 반환
# 중앙값을 타겟과 비교하는데, 만약 중앙값이 타겟보다 같거나 크다면 min()을 사용해 리턴할 값 갱신
def lower_bound(target):
    left, right = 0, n-1
    min_idx = n         # 반환할 값 저장할 변수 (가장 큰 인덱스 값보다 1 큰 값으로 설정)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:      # 타겟 이상이라면
            min_idx = min(min_idx, mid)    # 리턴할 값 갱신하고
            right = mid - 1                # 왼쪽으로 더 탐색해보기
        else:               # 타겟 미만이라면
            left = mid + 1      # 오른쪽으로 더 탐색해보기
    return min_idx

# 타겟을 초과하는 값이 처음으로 등장하는 위치를 반환
# 중앙값이 타겟보다 크다면 min() 사용해 리턴할 값 갱신
def upper_bound(target):
    left, right = 0, n-1
    min_idx = n
    while left <= right: 
        mid = (left + right) // 2
        if arr[mid] > target:       # lower_bound와 이 코드의 부등호만 다르다
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx

for _ in range(m):
    x = int(input())
    answer = upper_bound(x) - lower_bound(x)

    print(answer)

```

### 가장 먼저 나오는 숫자
>오름차순으로 정렬되어있는 n개의 숫자가 주어집니다. 이후 m개의 질의가 주어지며 각 질의마다 하나의 숫자 x가 주어졌을 때, 주어진 x 중에서 최초로 등장하는 위치를 출력하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어집니다.    
>두 번째 줄에는 n개의 숫자가 공백을 사이에 두고 주어집니다.    
>세 번째 줄에는 m개의 질의에 해당하는 숫자가 공백을 사이에 두고 주어집니다.
>* 1 ≤ n, m ≤ 100,000
>* 1 ≤ 주어지는 숫자 ≤ 10^9
> 
>**출력 형식**    
>각 질의마다 한 줄에 하나씩 숫자 x가 최초로 등장한 위치를 출력합니다. 만약 그러한 숫자가 등장한 적이 없다면, -1을 출력합니다.

**풀이** : 처음으로 타겟 이상의 값이 등장하는 위치를 반환하되, 그런 값이 없다면 `인덱스 최대값 + 1` 값을 반환하는 lower_bound 함수를 정의한다. 그리고 질의에 대해 
lower_bound() 를 사용하는데 반환된 값이 `인덱스 최대값 + 1` 이거나 arr[반환값]이 x가 아니라면 -1을 출력하고, 옳은 답이 나왔다면 `반환값 + 1` 을 출력한다.

```python
n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

# 처음으로 타겟 이상의 값이 등장하는 위치를 반환하되, 
# 그런 값이 없다면 `인덱스 최대값 + 1` 값을 반환하는 함수
def lower_bound(target):
    left, right = 0, n-1
    min_idx = n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    
    return min_idx

for x in queries:
    lower = lower_bound(x)
    if lower ==  n or arr[lower] != x: # x가 리스트에 없었다면
        print(-1)
    else:     # x가 리스트에 있었다면 
        print(lower + 1)
```

### 선분 위의 점
>n개의 점과 m개의 선분이 주어질 때, 각 선분 위에 몇개의 점이 있는지 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에 n과 m이 공백을 두고 주어집니다.    
>두 번째 줄에는 점의 좌표가 공백을 사이에 두고 주어집니다.    
>세 번째 줄부터 m개의 줄에 걸쳐 선분의 시작점과 끝점이 공백을 두고 한 줄에 하나씩 주어집니다.
>* 1 ≤ n, m ≤ 100,000
>* 1 ≤ 주어지는 수 ≤ 1,000,000,000
>
>**출력 형식**     
>첫 번째 줄부터 m개의 줄에 걸쳐 각 선분 위에 몇 개의 점이 존재하는지

**풀이** : 점들을 dots 리스트에 받아 오름차순으로 정렬해 이진탐색하기 쉽도록 만든다. 그리고 각 선분의 시작점과 끝점을 s, e 로 받아 upper_bound(e)로 끝점보다 큰 숫자의 dots에서의 인덱스를 
받고, lower_bound(s)로 시작점보다 같거나 큰 숫자의 dots에서의 인덱스를 받는다. 두 인덱스값의 차가 해당 선분 위에 있는 점의 개수이다.

```python
n, m = tuple(map(int, input().split()))
dots = list(map(int, input().split()))
lines = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

def lower_bound(target):
    left, right = 0, n-1
    min_idx = n
    while left <= right:
        mid = (left + right) // 2
        if dots[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx

def upper_bound(target):
    left, right = 0, n-1
    min_idx = n
    while left <= right:
        mid = (left + right) // 2
        if dots[mid] > target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx

dots.sort() # 정렬!

for s, e in lines:
    print(upper_bound(e) - lower_bound(s))
```
