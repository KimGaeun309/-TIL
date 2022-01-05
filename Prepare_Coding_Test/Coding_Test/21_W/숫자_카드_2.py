# 백준 10816 숫자 카드 2

"""
문제를 풀 때 시간 초과가 많이 발생했으나 dictionary(hash table)를 이용해
수행시간을 줄여 문제를 해결함.
"""

n = int(input())
cards = list(map(int, input().split()))


m = int(input())
questions = list(map(int, input().split()))

dict_cards = {}
for i in range(n):
    try:
        dict_cards[cards[i]] += 1
    except:
        dict_cards[cards[i]] = 1

for i in range(m):
    try:
        print(dict_cards[questions[i]], end=' ')
    except:
        print(0, end=' ')


