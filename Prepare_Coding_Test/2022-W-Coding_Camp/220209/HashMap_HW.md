## 숫자 등장 횟수
> n개의 숫자로 이루어진 수열 정보가 하나 주어졌을 때, m번에 걸쳐 특정 숫자가 주어지면 해당 숫자가 수열에 몇 개 있는지를 출력하는 프로그램을 작성해보세요.    
>**입력 형식**     
> 첫 번째 줄에는 원소의 개수 n과 질의의 수 m이 공백을 사이에 두고 주어집니다.    
> 두 번째 줄에는 n개의 원소가 공백을 사이에 두고 주어집니다.    
> 세 번째 줄에는 m개의 숫자가 공백을 사이에 두고 주어집니다.   
>* 1 ≤ m ≤ n ≤ 100,000      
>* 1 ≤ 주어지는 원소, 숫자 값 ≤ 10^9 
>
>**출력 형식**    
> 첫 번째 줄에 m개의 주어진 숫자에 대해서 순서대로 수열에 몇 개씩 존재하는지를 공백을 사이에 두고 출력합니다.


**풀이 1** : 파이썬에 내장된 dictionary 사용 (if~else로 에러 발생 방지)
```python
n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
quries = list(map(int, input().split()))

freq = {}
for elem in arr:
    if elem in freq:  # try~except로 작성할 경우 보다 복잡한 일을 해야 하는 경우 복잡해질 수 있다.
        freq[elem] += 1
    else:
        freq[elem] = 1

for num in quries:
    if num in freq:
        print(freq[num], end=" ")
    else:
        print(0, end=" ")
```
**풀이 2** : collections 모듈의 defaultdict 클래스 사용 (value를 0으로 초기화)
```python
from collections import defaultdict

n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
quries = list(map(int, input().split()))

freq = defaultdict(lambda: 0) # defaultdict 사용

for elem in arr:
    freq[elem] += 1

for num in quries:
    print(freq[num], end=" ")

```
**풀이 3** : get() 사용
get(elem, 'default') 를 통해 딕셔너리 안에 elem에 해당하는 키 값이 없을 때 대신 가져올 디폴트 값을 정할 수 있다.
```python
n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
quries = list(map(int, input().split()))

freq = {}
for elem in arr:
    freq[elem] = freq.get(elem, 0) + 1

for num in quries:
    print(freq.get(num, 0), end=" ")
```

## 가장 많은 데이터
>알파벳 소문자로 이루어진 문자열들이 중복을 허용하여 입력되었을때, 최대로 등장한 문자열의 등장 횟수를 출력하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 입력될 문자열의 개수 n이 주어집니다.    
>두 번째 줄부터 n + 1 번째 줄 까지 문자열들이 입력됩니다.
>* 1 ≤ n ≤ 100,000    
>* 1 ≤ 문자열의 길이 ≤ 50 
>  
>**출력 형식**       
>첫 번째 줄에 가장 많이 입력된 데이터가 등장한 횟수를 출력합니다.

**풀이** : 각 문자열이 등장한 횟수를 dictionary를 사용해 기록하며 최대값 갱신
```python
n = int(input())
arr = [
    str(input())
    for _ in range(n)
]

freq = {}
answer = 0

for string in arr: # 각 문자열이 등장한 횟수를 hashmap에 기록
    if string in freq:
        freq[string] += 1
    else:
        freq[string] = 1

    answer = max(answer, freq[string]) # 최대값 갱신

print(answer)
```

## 대응되는 수와 문자
>n개의 문자열이 주어집니다. 각 문자열은 1부터 n까지 주어진 순서대로 각각 하나의 숫자와 대응됩니다.
>이 후, 조사할 m개의 숫자 혹은 문자열이 주어졌을 때, 숫자에 대해서는 대응되는 문자열을, 문자열에 대해서는 대응되는 숫자를 출력하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 숫자의 개수 n과 조사할 값의 개수 m이 공백을 두고 주어집니다.    
>두 번째 줄 부터 n + 1 번째 줄 까지는 번호에 해당하는 문자열을 입력받습니다. 문자열은 전부 알파벳 소문자로만 이루어져 있으며, 동일한 문자열이 주어지지 않음을 가정해도 좋습니다.    
>* n + 2 번째 줄 부터 n + m + 1 번째 줄 까지는 조사할 문자열이나 번호를 입력받습니다. 잘못된 입력은 주어지지 않는다고 가정해도 좋습니다.    
>* 1 ≤ n ≤ 100,000
>* 1 ≤ m ≤ 100,000
>* 1 ≤ 문자열의 길이 ≤ 20
>* 1 ≤ 조사할 숫자 ≤ n
>
>**출력 형식**
>첫째 줄부터 차례대로 m개의 줄에 걸쳐 각각의 입력값에 대응하는 값을 한 줄에 하나씩 출력합니다.

**풀이** : 문자열-숫자, 숫자-문자열을 key-value로 가지는 딕셔너리 두 개를 각각 정의해 값들을 저장하고, <code>if x in str_as_key</code> 로 찾으려는 값이 문자열-숫자 딕셔너리에 있는지
확인해 있다면 <code>str_as_key[x]</code> 를 출력하고, 없다면 <code>int_as_key[x]</code> 를 출력한다.
```python
n, m = tuple(map(int, input().split()))
str_as_key = {}
int_as_key = {}

for i in range(1, n + 1):
    string = input()
    str_as_key[string] = str(i)
    int_as_key[str(i)] = string


queries = [
    input()
    for _ in range(m)
]

for x in queries:
    if x in str_as_key:
        print(f"{str_as_key[x]} ")
    else:
        print(f"{int_as_key[x]} ")
```

## 낮은 지점들
>2차 평면 위에 n개의 점이 주어졌을 때, 동일한 x좌표를 갖는 점들에 대해서는 그 중 가장 작은 y값을 갖는 점을 제외한 다른 점들은 전부 제거하여 하나의 x좌표 당 최대 하나의 점만 놓여져 있도록 만들려고 합니다. 이후 남아있는 점들의 y값의 합을 구하는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 원소의 개수 n이 주어집니다.    
>두 번째 줄부터는 n개의 줄에 걸쳐 한 줄에 하나씩 해당 점의 위치 (x, y)가 공백을 사이에 두고 주어집니다. 모든 점은 서로 다른 위치에 놓여있음을 가정해도 좋습니다.    
>* 1 ≤ n ≤ 100,000
>* -10^9 ≤ x, y ≤ 10^9
>
>**출력 형식**    
 >를 진행한 이후 남아있는 점들의 y값의 합을 출력합니다.

**풀이** : x-y를 key-value로 가지는 딕셔너리를 만든다. <code>if x not in points</code> 로 같은 x 값을 가진 점이 없을 경우 딕셔너리에 x-y를 삽입하고, 그렇지 않으면서 y가 기존의 value 값
보다 작다면 value를 y로 갱신해주어 y 값이 최소가 되도록 한다. 마지막으로 <code>sum(points.values())</code>로 y값의 합을 구한다.
```python
n = int(input())
points = {}

for _ in range(n):
    x, y = tuple(map(int, input().split()))
    if x not in points:
        points[x] = y
    elif y < points[x]:
        points[x] = y
        
sum_of_y = sum(points.values())

print(sum_of_y)
```

## 순서를 바꾸었을 때 같은 단어 그룹화하기
>n개의 단어가 입력으로 주어질 때, 한 단어에 속한 문자들의 순서를 바꾸어 만들 수 있는 단어들은 같은 그룹에 속한다고 정의된다고 합니다. 이 때 동일한 그룹에 속한 단어가 가장 많은 그룹의 단어 개수를 출력하는 코드를 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 단어의 개수 n이 주어집니다.    
>두 번째 줄부터 n+1번째의 줄에는 각각의 단어가 입력으로 주어집니다.    
>단 알파벳만이 입력으로 주어지며, 대소문자를 구분합니다.    
>* 1 ≤ n ≤ 1,000
>* 1 ≤ 단어의 최대길이(m) ≤ 1,000
>
>**출력 형식**    
>동일한 그룹에 속한 단어가 가장 많은 그룹의 단어 개수를 출력합니다.

**풀이** : 입력받은 단어들을 정렬해 딕셔너리에 등장횟수를 기록하고 최대 등장횟수를 갱신한다.

```python
n = int(input())
words = [input() for _ in range(n)]

H = {}
answer = 0
for word in words:
    # word_list 를 사용해 단어 정렬
    word_list = []
    for alp in word:
        word_list.append(alp)
    sorted_word = (''.join(sorted(word_list))) # 정렬된 단어를 sorted_word에 저장

    # 정렬된 단어의 등장횟수를 딕셔너리에 기록
    if sorted_word not in H:
        H[sorted_word] = 1
    else:
        H[sorted_word] += 1
     
    answer = max(answer, H[sorted_word]) # 최대 등장횟수 갱신

print(answer)
```

## 특별한 문자
>소문자 알파벳으로만 이루어져 있는 문자열이 하나 주어졌을 때, 해당 문자열에 단 한번만 나오는 문자를 찾는 프로그램을 작성해보세요.    
>**입력 형식**    
>첫 번째 줄에는 문자열이 하나 주어집니다. 문자열은 전부 소문자 알파벳으로만 이루어져 있습니다.    
>* 1 ≤ 주어지는 문자열의 길이 ≤ 100,000
>
>**출력 형식**    
>주어진 문자열에 단 한번만 등장하는 문자를 출력합니다. 만약 그러한 문자가 여러 개라면, 문자열 내에서 가장 먼저 등장한 문자를 출력합니다. 그러한 문자가 없다면 None을 출력합니다.

**풀이** : 주어진 문자열의 알파멧 등장 횟수를 딕셔너리에 기록하고, 딕셔너리의 모든 key-value 값을 확인하여 정답을 구한다.

```python
word = input()
freq = {}

for alp in word: # 알파벳 등장 횟수를 딕셔너리 freq에 기록
    if alp in freq:
        freq[alp] += 1
    else:
        freq[alp] = 1
        
answer = 'None' # 1회 등장한 문자가 없을 경우 None이 출력되도록 'None'으로 초기화.

for x, y in freq.items(): # 딕셔너리에 저장된 값들 확인
    if y == 1:
        if answer == 'None': # 초기화된 문자가 없다면 x를 대입
          answer = x
        elif ord(x) < ord(answer): # 초기화된 문자보다 x가 사전순으로 더 빠르다면 갱신
            answer = x

print(answer)
```

