## 오티 숙제
- 코딩 문제만 따로 저장

### 

**1. 단어 출력**
```python
print("Hello")
```

**2. 문장 출력**
```python
print("Hello World!")
```

**3. 따옴표 출력**
```python
print("He says \"It's a really simple sentence\".")
```

**4. 2줄 출력**
```python
print("Hello")
print("World")
```

**5. 숫자 2개 출력**
```python
print("3 5");
```

**6. 세 정수형 변수 선언**
```python
num1 = 7
num2 = 23
num3 = 30

print("{0} + {1} = {2}".format(num1, num2, num3))
```

**7. 달에서 무게 구하기**
```python
a = 13
b = 0.165

print("%d * %6lf = %6lf" %(a, b, a*b))
```

**8. 입력받아 계산**
```python
a = int(input())
print(f"{a + 2}")
```

**9. 실수 받아 그대로 출력**
```python
n = input()
n = float(n)
print(f"{n:.2f}")
```

**10. 문자 받아 출력**
```python
a = input()
print(a)
```

**11. 문자열 받아 출력**
```python
s = input()
print(s)
```

**12. 입력받아 계산 2**
```python
a, b = map(int, input().split())
print(f"{a * b}")
```

**13.입력받아 계산 3**
```python
a = int(input())
b = int(input())
print(f"{a*b}")
```

**14. 1시간 뒤 시간 출력**
```python
h, m = map(int, input().split(":"))

print(f"{h+1}:{m}")
```

**15. 날짜 변경하여 출력**
```python
y, m, d = map(int, input().split('.'))

print(f"{m}-{d}-{y}")
```

**16. 원소 10개의 합**
```python
arr = list(map(int, input().split()))

arr_sum = 0

for num in arr:
    arr_sum += num

print(arr_sum)
```

**17. 학점 계산기**
```python
n = int(input())
scores = list(map(float, input().split()))

avg = 0

for score in scores:
    avg += score

avg /= n

print(f"{avg:.1f}")

if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
else:
    print("Poor")
```

**18. 제곱하여 출력하기**
```python
n = int(input())
arr = list(map(int, input().split()))

new_arr = [elem ** 2 for elem in arr]

for num in new_arr:
    print(num, end=" ")
```

**19. 1-9 개수 세기**
```python
n = int(input())
nums = list(map(int, input().split()))
count_nums = [0 for _ in range(10)]

for num in nums:
    count_nums[num] += 1

for i in range(1, 10):
    print(count_nums[i])
```

**20. 가장 큰 수 구하기**
```python
import sys

nums = list(map(int, input().split()))

max_num = -sys.maxsize

for num in nums:
    if num > max_num:
        max_num = num
print(max_num)
```

**21. n개의 숫자 중 최소**
```python
import sys

n = int(input())
arr = list(map(int, input().split()))
min_num = sys.maxsize
min_cnt = 0

for num in arr:
    if num < min_num:
        min_num = num
        min_cnt = 1
    elif num == min_num:
        min_cnt += 1

print(min_num, min_cnt)
```

**22. 배열의 합**
```python
arr = [
    list(map(int, input().split()))
    for _ in range(4)
]

for line in arr:
    print(sum(line))
```

**23. 숫자 직사각형**
```python
n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

num = 1

for i in range(n):
    for j in range(m):
        arr[i][j] = num
        num += 1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()
```

**24. 아스키코드의 합과 차**
```python
c1, c2 = map(str, input().split())

print(f"{ord(c1) + ord(c2)}", end=" ")

if ord(c1) > ord(c2):
    print(f"{ord(c1) - ord(c2)}")
else:
    print(f"{ord(c2) - ord(c1)}")
```

**25. 아스키코드표 맞추기**
```python
nums = list(map(int, input().split()))
chars = [
    chr(num)
    for num in nums
]

for char in chars:
    print(char, end=" ")
```

**26. 대문자로 출력하기**
```python
string = input()

for s in string:
    if 'A'<=s and s<='Z':
        print(s, end='')
    elif  'a'<=s and s<='z':
        print(chr(ord(s) - ord('a') + ord('A')), end='')
```

**27. 붙여서 합하기**
```python
a, b = input().split()

print(f"{int(a + b) + int(b + a)}")
```

**28. 두 수의 합과 1**
```python
a, b = map(int, input().split())

string = str(a + b)
cnt = 0

for s in string:
    if s == '1':
        cnt += 1
        
print(cnt)
```

**29. 일치하는 문자열의 수**
```python
n, A = input().split()
n = int(n)

cnt = 0

for _ in range(n):
    B = input()
    if B == A:
        cnt += 1
        
print(cnt)
```

### Novice Mid

**30. 007**
```python
class Secret:
    def __init__(self, secret_code, meeting_point, time):
        self.s = secret_code
        self.m = meeting_point
        self.t = time

s1, m1, t1 = input().split()
t1 = int(t1)


secret = Secret(s1, m1, t1)

print(f"secret code : {secret.s}")
print(f"meeting point : {secret.m}")
print(f"time : {secret.t}")
```

**31. NEXT LEVEL**
```python
class NextLevel:
    def __init__(self, ID="", Level=0):
        self.ID = ID
        self.Level = Level

user1 = NextLevel()

user1.ID = 'codetree'
user1.Level = 10

id2, level2 = input().split()

user2 = NextLevel(id2, int(level2))

print(f"user {user1.ID} lv {user1.Level}")
print(f"user {user2.ID} lv {user2.Level}")
```

**32. 코드네임**
```python
class Agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score
arr = []
for _ in range(5):
    c, s = input().split()
    new_agent = Agent(c, int(s))
    arr.append(new_agent)

min_agent = arr[0]

for i in range(1, 5):
    if min_agent.score > arr[i].score:
        min_agent = arr[i]

print(f"{min_agent.codename} {min_agent.score}")
```

### Intermediate Mid

**50. HashMap 기본**
```python
n = int(input())
H = dict()

for _ in range(n):
    string = list(map(str, input().split()))
    
    if string[0] == 'add':
        H[int(string[1])] = int(string[2])
    elif string[0] == 'remove':
        H.pop(int(string[1]))
    else:
        if int(string[1]) in H:
            print(H[int(string[1])])
        else:
            print("None")
```

**51. TreeMap 기본**
```python
from sortedcontainers import SortedDict

T = SortedDict()

n = int(input())
for _ in range(n):
    command = list(map(str, input().split()))
    if command[0] == 'add':
        T[int(command[1])] = int(command[2])
    elif command[0] == 'remove':
        T.pop(int(command[1]))
    elif command[0] == 'find':
        if int(command[1]) in T:
            print(int(T[int(command[1])]))
        else:
            print("None")
    else:
        if not T:
            print('None')
        else:
            for v in T.values():
                print(v, end=' ')
            print()
```

**52. HashSet 기본**
```python
n = int(input())

S = set()

for _ in range(n):
    command = list(map(str, input().split()))

    if command[0] == 'add':
        S.add(int(command[1]))
    elif command[0] == 'remove':
        S.remove(int(command[1]))
    else:
        if int(command[1]) in S:
            print('true')
        else:
            print('false')
```

**53. TreeSet 기본**
```python
from sortedcontainers import SortedSet

S = SortedSet()

n = int(input())

for _ in range(n):
    command = list(map(str, input().split()))
    
    if command[0] == 'add':
        S.add(int(command[1]))
    elif command[0] == 'remove':
        S.remove(int(command[1]))
    elif command[0] == 'find':
        print('true') if int(command[1]) in S  else print('false')
    elif command[0] == 'lower_bound':
        try:
            print(S[S.bisect_left(int(command[1]))])
        except:
            print('None')
    elif command[0] == 'upper_bound':
        try:
            print(S[S.bisect_right(int(command[1]))])
        except:
            print('None')
    elif command[0] == 'largest':
        print(S[-1]) if S else print('None')
    else:
        print(S[0]) if S else print('None')
```

**54. 정수 명령 처리 6 (Priority Queue)**
```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        heapq.heappush(self.items, -item)

    def empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def pop(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        return -heapq.heappop(self.items)

    def top(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        return -self.items[0]

n = int(input())
pq = PriorityQueue()

for _ in range(n):
    command = list(map(str, input().split()))

    if command[0] == 'push':
        pq.push(int(command[1]))
    elif command[0] == 'pop':
        print(pq.pop())
    elif command[0] == 'size':
        print(pq.size())
    elif command[0] == 'empty':
        print(1) if pq.empty() else print(0)
    elif command[0] == 'top':
        print(pq.top())
```
