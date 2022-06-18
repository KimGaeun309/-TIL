## 백준 1074 Z

### 문제
* 한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
* N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
* N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

### 입력
* 첫째 줄에 정수 N, r, c가 주어진다.

### 출력
* r행 c열을 몇 번째로 방문했는지 출력한다.

### 코드
```python
import sys
N, r, c = tuple(map(int, sys.stdin.readline().split()))

def print_count(i, j, n):
    global count

    # n == 1 이면 정답 후보가 4칸 밖에 남지 않음
    if n == 1:
        if i == r and j == c:
            pass
        elif i == r and j+1 == c:
            count += 1
        elif i+1 == r and j == c:
            count += 2
        else:
            count += 3
        print(count)
        return

    n -= 1  # n 감소
    if (r < i + 2**n) and (c < j + 2 ** n):     # 2사분면 (i, j 그대로)
        print_count(i, j, n)
    elif (r < i + 2**n) and (c >= j + 2**n):    # 1사분면 (i 그대로, j += 2^n)
        count += 2**n * 2**n
        print_count(i, j + 2 ** n, n)
    elif (r >= i + 2**n) and (c < j + 2**n):    # 3사분면 (i += 2^n, j 그대로)
        count += 2 * 2**n * 2**n
        print_count(i + 2 ** n, j, n)
    else:                                       # 4사분면 (i += 2^n, j += 2^n)
        count += 3 * 2**n * 2**n
        print_count(i + 2 ** n, j + 2 ** n, n)

count = 0
print_count(0, 0, N)

```
