## 비율 구하기
>여러가지의 문자열이 주어졌을때 그 문자열이 전체 문자열 중 어느정도의 비율을 차지하는지에 대해 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 문자열의 개수 n이 주어집니다.    
>두 번째 줄부터 n + 1 번째의 줄에는 각각의 문자열이 입력으로 주어집니다.
>* 1 ≤ n ≤ 10000
>* 1 ≤ 문자열의 길이 ≤ 30
>
>**출력 형식**    
>주어진 문자열을 사전순으로 출력하고, 그 문자열이 차지하는 비율을 백분율로 소수점 4째자리까지 반올림하여 공백을 두고 출력합니다.

**풀이** : sortedcontainers에서 SortedDict(Tree Map)를 가져와 dictionary 사용하듯이 key-value에 문자열과 문자열의 등장 횟수를 저장하고, 트리맵은 
<code>for key, value in freq.items(): </code>를 하면 사전 순으로 순회한다는 점을 이용해 답을 출력합니다.

```python
from sortedcontainers import SortedDict
n = int(input())

arr = [
    str(input())
    for _ in range(n)
]

freq = SortedDict() # SortedDict 사용

for string in arr: # 문자열 등장 횟수 기록
    if string in freq:
        freq[string] += 1
    else:
        freq[string] = 1

for key, value in freq.items(): # 트리맵은 균형이진트리 구조를 사용하므로 사전순으로 key-value 쌍을 알려줌
    percent = value / n * 100  # 비율 계산
    print(f"{key} {percent:.4f}") # 소수점 4자리까지 비율 출력
```

## 단어장
>n개의 단어(문자열)가 주어졌을 때, 각 단어가 몇 번씩 나왔는지를 앞선 단어가 먼저 나오도록 출력하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 n이 주어집니다.    
>두 번째 줄 부터는 n개의 줄에 걸쳐 각 단어가 한 줄에 하나씩 주어집니다. 모든 단어는 소문자 알파벳으로만 이루어져 있다고 가정해도 좋습니다.
>* 1 ≤ n ≤ 100,000
>* 1 ≤ 주어지는 단어의 길이 ≤ 5
>
>**출력 형식**    
>주어진 서로 다른 단어의 수 만큼 한 줄에 하나씩 (단어, 등장 횟수)를 공백을 사이에 두고 출력합니다. 사전순으로 앞선 단어부터 나오도록 출력해야함에 유의합니다.

**풀이** : 단어의 등장횟수를 사전순으로 출력해야 하므로 SortedDict(트리맵)에 단어-등장횟수를 key-value로 기록해 었다가 for문으로 순회하며 출력합니다. 트리맵은 사전순으로 key-value 쌍을 알려줍니다.

```python
from sortedcontainers import SortedDict
n = int(input())
words = [
    input()
    for _ in range(n)
]

freq = SortedDict() # SortedDict() 사용

for word in words: # 단어 등장 횟수 기록
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

for key, value in freq.items(): # 순회 (자동으로 사전순으로 출력)
    print(f"{key} {value}")
```

## 처음 등장하는 위치
>n개의 숫자가 주어졌을 때, 각 숫자마다 처음으로 주어진 위치를 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 원소의 개수 n이 주어집니다. 두 번째 줄에는 n개의 숫자가 주어집니다.
>* 1 ≤ n ≤ 100,000
>* -10^9 ≤ 주어지는 숫자 ≤ 10^9
>
>**출력 형식**    
>주어진 숫자들을 중복을 제거하고 오름차순 정렬했을 때의 결과를 한 줄에 하나씩 출력합니다. 단, 각 숫자 x를 출력할 때마다 해당 숫자 x가 처음으로 주어진 위치 p를 공백을 사이에 두고 x p 형태로 출력합니다. 위치는 1번부터 시작하여 입력으로 주어진 순서대로 n번까지 매겨져 있다고 가정합니다.

**풀이** : 트리맵을 사용합니다. for문으로 입력받은 숫자가 트리맵에 없다면 단어-위치 쌍을 트리맵에 새로 저장하고, for문으로 key, value 값을 순회하며 답을 출력합니다.

```python
from sortedcontainers import SortedDict
n = int(input())
nums = list(map(int, input().split()))

treemap = SortedDict()

for i in range(n):  # 처음으로 주어진 위치가 value에 저장될 수 있게끔 treemap에 nums[i]가 없을 경우에만 단어-위치 쌍을 저장.
    if nums[i] not in treemap:
        treemap[nums[i]] = (i+1)

for key, value in treemap.items(): # 오름차순으로 순회됨.
    print(f"{key} {value}")
```

