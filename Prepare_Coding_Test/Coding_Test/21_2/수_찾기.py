#  백준 1920 수 찾기

def binary_search(A, k, n):
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid-1
        elif A[mid] < k:
            left = mid+1
        else:
            return mid

    return None



n = int(input())
A = sorted(list(map(int, input().split())))
m = int(input())
B = list(map(int, input().split()))


for k in B:
    if binary_search(A, k, n) != None:
        print(1, end=' ')
    else:
        print(0, end=' ')

