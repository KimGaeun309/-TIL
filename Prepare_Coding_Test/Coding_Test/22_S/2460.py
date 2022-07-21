# 백준 2460 지능형 열차 2
import sys
input = sys.stdin.readline
max_people = 0
curr_people = 0
for _ in range(10):
  get_off, get_on = tuple(map(int, input().split()))
  curr_people -= get_off
  curr_people += get_on
  if curr_people > max_people:
    max_people = curr_people

print(max_people)
