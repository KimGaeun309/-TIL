# 백준 3460 이진수
T = int(input()) 
for _ in range(T):
  test_case = int(input())
  binary = bin(test_case)[2:]
  cnt = 0
  for i in range(len(binary)-1, -1, -1):
    if (binary[i] == '1'):  print(cnt, end=' ')
    cnt += 1
  print()



