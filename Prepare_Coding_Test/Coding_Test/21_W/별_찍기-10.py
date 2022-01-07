# 백준 2447 별 찍기 - 10

"""
["***", "* *", "***"] 3x3에서부터 시작해 MakeStar 함수를 호출할 때마다 9x9, 27x27, ... 으로 크기를 늘린다. MakeStar 함수는 log3 n 만큼 호출한다.
MakeStar 함수에서는 기존 격자를 매개변수로 받아 Temp 리스트에 새로운 격자를 저장해 리턴하는데, for문으로 기존 격자의 행의 개수(= len(L)) * 3 만큼 돌면서 새로운 격자의 행을 하나씩 채운다.
기존 격자의 i%len(L)번째 행으로 새로운 격자의 행을 채우는데 만약 행의 번호를 len(L)로 나눈 결과가 1이면 중간에 공백이 필요하고, 0이나 2이면 공백이 없이 채운다. 
"""

def MakeStar(L):
    Temp = []

    for i in range(3 * len(L)):
        if i // len(L) == 1:
            Temp.append(L[i % len(L)] + " " * len(L) + L[i % len(L)])
        else:
            Temp.append(L[i % len(L)] * 3)

    return Temp

n = int(input())
stars = ["***", "* *", "***"]

while n > 3:
    n /= 3
    stars = MakeStar(stars)

for star in stars:
    print(star)
    

"""
# + 재귀로 작성


def MakeStar(L, n):
    if n == 3:
        return L
    Temp = []

    for i in range(3 * len(L)):
        if i // len(L) == 1:
            Temp.append(L[i % len(L)] + " " * len(L) + L[i % len(L)])
        else:
            Temp.append(L[i % len(L)] * 3)

    return MakeStar(Temp, n/3)

n = int(input())
stars = []
stars = MakeStar(["***", "* *", "***"], n)

for star in stars:
    print(star)


"""
