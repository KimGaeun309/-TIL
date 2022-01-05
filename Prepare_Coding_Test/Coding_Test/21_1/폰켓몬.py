# 프로그래머스 1단계 폰켓몬

def solution(nums):
    a = len(nums) / 2
    newnums = set(nums)
    b = len(newnums)
    if b < a:
        return b
    else:
        return a
