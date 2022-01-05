def find_median_five(A):
    D = {}
    maximum, minimum = max(A), min(A)
    T = []
    for a in A:
        try:
            D[a] += 1
        except:
            D[a] = 1
        if a != maximum and a != minimum:
            T.append(a)

    if len(T) == 0:
        if D[maximum] > D[minimum]:
            return maximum
        else:
            return minimum
    elif len(T) < 2:
        return A[0]
    else:
        return find_median_five(T)


    # L의 다섯 개 이하의 값 중에서 중간값을 찾아 리턴하는 코드
    # 파이썬의 max, min 함수 사용 가능. sort 함수 사용 불가능(정렬하면 안됨)

def MoM(A, k):  # L의 값 중에서 k번째로 작은 수 리턴
    if len(A) == 1:  # no more recursion
        return A[0]
    i = 0
    S, M, L, medians = [], [], [], []
    while i + 4 < len(A):
        medians.append(find_median_five(A[i: i + 5]))
        i += 5

    if i < len(A) and i + 4 >= len(A):  # 마지막 그룹으로 5개 미만의 값으로 구성
        medians.append(find_median_five(A[i:]))

    mom = MoM(medians, len(medians)//2) 

    # S, M, L 그룹 나누기
    for v in A:
        if v < mom:
            S.append(v) 
        elif v > mom:
            L.append(v) 
        else:
            M.append(v) 

    if len(S) >= k: 
        return MoM(S, k) 
    elif len(S) + len(M) < k: 
        return MoM(L, k - len(S) - len(M)) 
    else:
        return mom


# n과 k를 입력의 첫 줄에서 읽어들인다
n, k = map(int, input().split());
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
A = list(map(int, input().split()));
print(MoM(A, k))
