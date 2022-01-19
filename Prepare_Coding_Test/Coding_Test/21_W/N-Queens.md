### 백준 9663 N-Queens

* 파이썬     
시간초과 (파이썬은 백트래킹 문제를 풀기에 시간복잡도상 불리하다고 함.)

``` python
import sys

def canGo(k, col):
    for i in range(1, k):
        if X[i] == col: return False
        if X[k - i] == col + i: return False
        if X[k - i] == col - i: return False
    return True


def nQueens(k):
    global cnt
    if k > n:
        cnt += 1
        return
    for col in range(n):
        if canGo(k, col):
            X[k] = col
            nQueens(k + 1)

n = int(sys.stdin.readline())
X = [0] * (n+1)
cnt = 0

nQueens(1)
print(cnt)
```

* C++     
파이썬에서와 같은 알고리즘 적용해 통과.

``` c++
#include <iostream>
using namespace std;

int cnt, X[15], n;

bool canGo(int k, int col);
void nQueens(int k);

int main(void) {
	cin >> n;
	nQueens(1);
	cout << cnt;
	return 0;
}

bool canGo(int k, int col) {
	for (int i = 1; i < k; i++) {
		if (X[i] == col or abs(X[k - i] - col) == i) {
			return false;
		}
	}
	return true;
}

void nQueens(int k) {
	if (k > n) {
		cnt += 1;
	}
	for (int col = 0; col < n; col++) {
		if (canGo(k, col)) {
			X[k] = col;
			nQueens(k + 1);
		}
	}

}
```
