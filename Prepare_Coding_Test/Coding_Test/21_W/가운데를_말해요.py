# 백준 1655 가운데를 말해요

"""
입력받은 수를 중간값보다 작거나 같은 수들은 smaller 라는 max heap에 저장하고, 큰 수들은 bigger 라는 min heap에 저장하고, smaller 힙의 루트 노드에 해당하는 값을 출력하면 된다.
smaller를 max heap으로 만들기 위해 튜플 형태로 (-num, num) 원소를 넣어준다. 이때 항상 smaller의 원소 개수가 bigger의 원소 개수와 같거나 1 크도록 한다.
그리고 smaller의 모든 값들이 bigger의 모든 값들보다 항상 크지 않도록 하기 위해 smaller의 루트 노드 값이 bigger의 루트 노드 값보다 크다면 두 값을 뒤바꾸어준다.
"""

import heapq, sys

n = int(sys.stdin.readline())
smaller, bigger = [], []

for _ in range(n):
    new = int(sys.stdin.readline())
    if len(smaller) == len(bigger):
        heapq.heappush(smaller, (-new, new))
    else:
        heapq.heappush(bigger, (new, new))

    if bigger and smaller[0][1] > bigger[0][1]:
        big = heapq.heappop(smaller)[1]
        small = heapq.heappop(bigger)[1]
        heapq.heappush(smaller, (-small, small))
        heapq.heappush(bigger, (big, big))

    print(smaller[0][1])
