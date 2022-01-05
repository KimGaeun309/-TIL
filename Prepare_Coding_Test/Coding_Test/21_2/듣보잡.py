# 백준 1764 듣보잡

n, m = map(int, input().split())

NS = {}

for i in range(n):
    name = input()
    NS[name] = 1

Answer = []
cnt = 0

for i in range(m):
    name = input()
    try:
        isNSH = NS[name]
    except:
        isNSH = 0
    if isNSH:
        Answer.append(name)
        cnt += 1

Answer.sort()
print(cnt)
for i in range(cnt):
    print(Answer[i])
