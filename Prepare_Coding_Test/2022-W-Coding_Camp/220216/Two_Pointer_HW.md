## 가장 짧은 부분합 
>원소가 n개 들어 있는 수열에서 특정 구간을 잡았을 때 그 합이 s 이상이 되는 것 중, 가장 짧은 구간의 길이를 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에 n과 s가 공백을 두고 주어집니다.     
>두 번째 줄에 수열의 각 원소가 공백을 두고 차례대로 주어집니다.    
>* 1 ≤ n ≤ 100,000
>* 1 ≤ s ≤ 10^9
>* 1 ≤ 원소 값 ≤ 10,000  
>
>**출력 형식**    
>수열 내 특정 구간을 잡았을 때 그 합이 s 이상이 되는 것 중 가장 짧은 구간의 길이를 출력합니다.    
>만약 불가능 하다면 -1을 출력합니다.

```python
import sys
INT_MAX = sys.maxsize

n, s = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))

answer = INT_MAX # 최솟값을 구하기 위한 초기화값
j = 1 # j 는 후진하지 않는 끝 인덱스 
sum_val = arr[1]

for i in range(1, n+1): # i 는 for문으로 돌아가는 시작 인덱스
    # j+1이 범위를 벗어나지 않으면서 sum_val이 s보다 작은 동안
    while j+1 <= n and sum_val < s: 
        sum_val += arr[j+1] # sum_val에 다음 값 더하기
        j += 1 # 끝 인덱스 += 1

    if sum_val < s: # while문 빠져나오고도 s보다 작다면 arr를 모두 순회했지만 
        break      # 그 합이 s보다 작다는 뜻이므로 break  

    answer = min(answer, j - i + 1) # 최솟값으로 갱신
    sum_val -= arr[i] # 다음 i를 시작점으로 가지는 sum_val을 위해 현재 시작값 빼주기

if answer == INT_MAX: # answer가 초기값 그대로라면 -1 출력
    print(-1)
else:
    print(answer) # answer 출력
```

## 겹치는 숫자가 없는 최대 구간
>n개의 숫자가 주어졌을 때, 구간 내에 중복되는 숫자가 전혀 없는 경우 중 가능한 최대 구간의 크기를 구하는 프로그램을 작성해보세요.     
>**입력 형식**     
>첫 번째 줄에는 n이 주어집니다.    
>두 번째 줄에는 n개의 숫자가 공백을 사이에 두고 주어집니다.
>* 3 ≤ n ≤ 100,000
>* 1 ≤ 주어지는 숫자 ≤ 100,000
>
>**출력 형식**    
>중복되는 숫자가 없는 구간 중 최대 구간의 크기를 출력합니다.

```python
n = int(input())
arr = [0] + list(map(int, input().split()))
counting = [0] * 100001 # 숫자가 몇 번 나타났는지 세기 위한 리스트

j = 1 
counting[arr[1]] += 1
answer = 0

for i in range(1, n+1): # i 는 시작점. 
    # j는 끝점. j+1이 범위를 벗어나지 않으면서 arr[j+1]이 아직 구간 내에 없다면
    while j+1 <= n and counting[arr[j+1]] == 0: 
        counting[arr[j+1]] += 1  # counting 리스트의 arr[j+1]에 += 1
        j += 1  # 끝 인덱스 += 1
    
    answer = max(answer, j - i + 1) # answer를 최솟값으로 갱신

    counting[arr[i]] -= 1 # arr[i] 를 빼기 위해 -= 1

print(answer)
```

## 부분수열 여부 판단하기    
>두 수열 A와 B가 주어졌을 때 B가 A의 부분수열인지 판단하는 프로그램을 작성해보세요. B가 A의 부분수열이라 함은 B의 원소가 차례대로 A의 원소에 존재할 때를 의미합니다.    
>예를 들어 A = [5, 1, 20, 3, 4] 일 때, B = [5, 1, 4] 라면 5 1 4가 차례대로 수열 A에 존재하므로 B는 A의 부분수열입니다. 하지만 만약 A = [5, 1, 20, 3, 4], B = [5, 3, 1] 이라면 5 3 1이 수 열 A에 차례대로 존재하지 않으므로 B는 A의 부분수열이 아닙니다.    
>**입력 형식**    
>첫 번째 줄에는 수열 A의 원소의 개수 n과 수열 B의 원소의 개수 m가 공백을 사이에 두고 주어집니다.    
>두 번째 줄에는 수열 A의 원소 n개가 공백을 사이에 두고 주어집니다.    
>세 번째 줄에는 수열 B의 원소 m개가 공백을 사이에 두고 주어집니다.    
>* 1 ≤ n, m ≤ 100,000
>* 1 ≤ 주어지는 원소의 값 ≤ 10^9
>
>**출력 형식**    
>수열 B가 수열 A의 부분수열이라면 Yes를, 그렇지 않다면 No를 출력합니다.

```python
n, m = tuple(map(int, input().split()))
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

def is_subsequence(): # 부분수열인지 확인하는 함수
    i = 1 # i는 A를 순회할 인덱스
    for j in range(1, m+1): # j는 B를 순회할 인덱스
        # i가 A의 범위를 벗어나지 않도록 A[i]가 B[i]와 같아질 때까지 반복
        while i <= n and A[i] != B[j]:
            i += 1
        # 반복문을 빠져나왔을 때 i가 A를 초과했다면 부분수열이 아니다
        if i == n+1:
            return False
        # 반복문을 빠져아왔을 때 i가 A를 초과하지 않았다면 i에 1을 더해
        # A의 다음 원소를 확인할 수 있도록 한다.
        else:
            i += 1
    # 1부터 m까지 위의 반복문이 돌아가는 동안 return False가 실행되지 않았다면
    # 부분수열이 맞으므로 True를 return해준다.
    return True

if is_subsequence():
    print("Yes")
else:
    print("No")
```

## 정수 n개의 합
>크기가 n인 수열이 주어졌을 때, 이 중 연속하는 몇 개의 원소들의 합이 m이 되는 경우의 수를 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 n과 m이 주어집니다.     
>두 번째 줄에는 n개의 정수가 공백을 두고 차례대로 주어집니다.     
>* 1 ≤ n ≤ 10,000
>* 1 ≤ m ≤ 300,000,000
>* 1 ≤ 원소의 크기 ≤ 30,000
>
>**출력 형식**    
>경우의 수를 출력합니다.

```python
n, m = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))

answer = 0
curr_sum = 0
i = 0 
for j in range(1, n+1):
    curr_sum += arr[j] # 0번째부터 1번째까지를 맨 처음으로 확인

    # i가 범위를 넘지 않으며 curr_sum이 m보다 큰 동안
    while i <= n and curr_sum > m:
        curr_sum -= arr[i] # curr_sum의 값 감소시키고
        i += 1 # i 값 증가시키기

    # while문을 빠져나왔을 때 curr_sum이 m과 같다면 답 += 1
    if curr_sum == m:
        answer += 1

print(answer)
```

## 정수 두 개의 합 2
>n개의 정수 주어졌을 때, 이 중 두 개의 원소를 골라 그 합이 k 이하가 되는 경우의 수를 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 정수 n의 개수와 k가 주어집니다.    
>두 번째 줄부터 n개의 줄에 걸쳐 n개의 정수가 주어집니다.    
>* 2 ≤ n ≤ 100,000 
>* 1 ≤ k ≤ 1,000,000
>* 1 ≤ 정수의 크기 ≤ 1,000,000
>
>**출력 형식**    
>가능한 경우의 수를 출력합니다.

```python
n, k = tuple(map(int, input().split()))
arr = [0] + [
    int(input())
    for _ in range(n)
]

arr.sort() # 작은 수부터 확인해야 하므로 정렬

j = n+1 # j 는 n+1부터 
answer = 0

# i 는 1부터
for i in range(1, n+1): 
    # j-1 이 범위를 벗어나지 않으면서 i번째와 j-1번째 원소의 합이 k보다 큰 동안
    while 1 <= j-1 and arr[i] + arr[j - 1] > k: 
        j -= 1 # j 값 -= 1 해서 두 원호의 합이 k 이하일 때 while문을 벗어나도록 함
    
    # i가 j보다 크거나 같다면 break
    if i >= j:
        break
    print(i, j)
    # (i, j-1) (i, j-2) .. (i, i+1) 까지 모두 합이 k 이하이다
    answer += (j - i - 1)

print(answer)
```

## 1이 k개 이상 존재하는 부분 수열
>1과 2로 이루어진 크기가 n인 수열에서, 1이 k개 이상 존재하는 가장 짧은 연속된 부분 수열의 길이를 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에 n과 k가 주어집니다.    
>두 번째 줄에 n개의 1 또는 2가 공백을 두고 출력됩니다. 
>* 1  ≤  k  ≤  n  ≤  10^6
> 
>**출력 형식**    
>1이 k개 이상 존재하는 연속된 부분 수열 중 가장 짧은 부분 수열의 길이를 출력합니다. 만약 불가능 하다면 -1을 출력합니다. 

```python
import sys
INT_MAX = sys.maxsize
n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

i = 0
count = 0
answer = INT_MAX

for j in range(n):
    if arr[j] == 1: # 1의 개수가 늘어났다면 count += 1
        count += 1

    if count > k: # 1의 개수가 k보다 커졌다면 i 증가
        i += 1
        count -= 1

    while arr[i] == 2: # 구간의 왼쪽 끝이 1이 되도록 반복문
        i += 1

    if count == k: # 1의 개수가 k개라면 정답 갱신
        answer = min(answer, j - i + 1)
    

if answer == INT_MAX:
    print(-1)
else:
    print(answer)
```

## 화재 진압
>1차 수직전 상 위에 화재가 발생할 가능성이 있는 서로 다른 n개의 위치와 소방서 m개의 위치가 주어집니다. 화재는 정확히 한 곳에서만 발생하며, 가장 근처에 있는 소방서에서 출동하여 진입한다고 합니다. 거리 1을 이동하는 데 시간이 1초가 소요된다고 했을 때, 각 위치에서 화재가 발생하는 데 이를 진압하는 데 걸리는 시간 중 가장 오래 걸리는 시간을 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어집니다.    
>두 번째 줄에는 n개의 불이 날 가능성이 있는 위치가 공백을 사이에 두고 주어집니다.    
>세 번째 줄에는 m개의 소방서의 위치가 공백을 사이에 두고 주어집니다.    
>* 1 ≤ n, m ≤ 100,000
>* -10^9 ≤ 주어지는 숫자 ≤ 10^9 
>
>**출력 형식**    
>화재 진압에 가장 오래 걸리는 위치에 불이 발생했다고 했을 때, 그 때의 진압 시간을 출력합니다.

```python
n, m = tuple(map(int, input().split()))
P = list(map(int, input().split()))
S = list(map(int, input().split()))

P.sort()
S.sort()

answer = 0
j = 0
for i in range(n):
    # 각 화재 장소로 가는데 가장 적은 시간이 걸리는 소방서 찾아 거리 구하기
    shortest = abs(P[i] - S[j])
    while j+1 < m and abs(P[i] - S[j+1]) < shortest:
        j += 1
        shortest = abs(P[i] - S[j])

    # 답 갱신하기
    answer = max(answer, shortest)

print(answer)
```

## 중복되지 않는 가장 긴 문자열
>문자열 한 개가 입력으로 주어졌을 때 해당 문자열에 포함된 연속한 부분 문자열 중 중복되는 문자가 없는 가장 긴 부분 문자열을 구하는 코드를 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에 문자열 한 개가 입력으로 주어집니다. 문자열은 소문자 알파벳으로만 이루어져 있다고 가정해도 좋습니다.    
>* 1 ≤ 주어지는 문자열의 길이 (n) ≤ 100,000  
>**출력 형식**    
>연속 부분 문자열 중 중복되는 문자가 없는 가장 긴 부분 문자열의 길이를 출력합니다.

```python
string = "#" + input()
n = len(string) - 1

H = dict()  # 문자 개수 확인할 딕셔너리

H[string[1]] = 1

answer = 0
j = 1

for i in range(1, n+1):  
     # 같은 문자가 2개가 되기 전까지 계속 진행합니다.
    while j + 1 <= n and H.get(string[j+1], 0) != 1:
        H[string[j+1]] = H.get(string[j+1], 0) + 1
        j += 1
        
    # i부터 j까지의 구간이 현재 부분 문자열.
    answer = max(answer, j-i+1) # 답을 최댓값으로 갱신

    H[string[i]] -= 1 # 

print(answer)
```

## 서로 다른 k개의 문자
>문자열 한 개가 입력으로 주어졌을 때 해당 문자열에 포함된 연속한 부분 문자열 중 해당 문자열 내의 서로 다른 문자의 수가 k개를 넘지 않는 경우 중 가장 긴 부분 문자열의 길이를 구하는 코드를 작성해보세요.     
>**입력 형식**     
>첫 번째 줄에 문자열 한 개와 k가 공백을 사이에 두고 주어집니다. 문자열은 소문자 알파벳으로만 이루어져 있다고 가정해도 좋습니다.    
>* 1 ≤ 주어지는 문자열의 길이 (n) ≤ 100,000
>* 1 ≤ k ≤ 26    
>
>**출력 형식**    
>연속 부분 문자열 중 문자열을 이루고 있는 서로 다른 문자의 수가 k를 넘지 않는 경우 중 가장 긴 부분 문자열의 길이를 출력합니다.

```python
string, k = tuple(map(str, input().split()))
k = int(k)
string = "#" + string
n = len(string) - 1
count_array = dict()

def can_go(j): # j를 진행시켜도 되는지 판별하는 함수
    # j+1이 범위를 벗어나면 False
    if j + 1 > n: 
        return False
    # 서로 다른 문자들의 종류가 k개이면서 j+1번째 문자가 처음 등장한다면 False
    if diff_cnt == k and count_array.get(string[j+1], 0) == 0:
        return False
    # 그 외의 경우는 모두 True
    return True

count_array[string[1]] = 1 # count_array에 첫번째 문자 미리 넣기
diff_cnt = 1 # 문자의 종류 저장할 변수
answer = 0 # 답은 최소값으로 초기화 (최댓값으로 갱신할 것이므로)
j = 1 # j 는 1부터 (끝 인덱스)

for i in range(1, n+1): # i 는 1부터 for문 (시작 인덱스)
    while can_go(j): # j를 진행시킬 수 있다면
        # count_array에 j+1번째 문자를 하나 추가
        count_array[string[j+1]] = count_array.get(string[j+1], 0) + 1 
        # 만얄 j+1번째 문자가 처음 등장했다면 문자의 종류 값 증가
        if count_array[string[j+1]] == 1:
            diff_cnt += 1
        j += 1 # 끝 인덱스 += 1

    answer = max(answer, j - i + 1) # 최대 구간 길이로 answer 값 갱신
 
    count_array[string[i]] -= 1  # count_array 에서 i번째 문자 하나 없애기

    if count_array[string[i]] == 0: # 만약 i번째 문자가 더이상 없게 되었다면
        diff_cnt -= 1 # 문자의 종류 값 감소

print(answer)
```
