# 백준 2309 일곱 난쟁이
import sys
input = sys.stdin.readline

def find_sevenDwarfs(nine_dwarfs):
  answer = []
  sum_of_dwarfs = sum(nine_dwarfs)
  for i in range(9):
    for j in range(i+1, 9):
      if sum_of_dwarfs - nine_dwarfs[i] - nine_dwarfs[j] == 100:
        return nine_dwarfs[:i] + nine_dwarfs[i+1:j] + nine_dwarfs[j+1:]

nine_dwarfs = []
for _ in range(9):
  nine_dwarfs.append(int(input()))

seven_dwarfs = sorted(find_sevenDwarfs(nine_dwarfs))
for dwarf in seven_dwarfs:
  print(dwarf)



