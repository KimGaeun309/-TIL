# 백준 1018 체스판 다시 칠하기

n, m = map(int, input().split())
U = [ input() for _ in range(n) ]
C = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]
def CountPaint(r, c):
    cnt = 0
    for i in range(r, r+8):
        for j in range(c, c+8):
            if U[i][j] != C[i-r][j-c]:
                cnt += 1
    if cnt <= 32:
        return cnt
    else:
        return 64-cnt

minimum = n * m

for i in range(n - 7):
    for j in range(m - 7):
        tmp = CountPaint(i, j)
        if minimum > tmp:
            minimum = tmp
print(minimum)
