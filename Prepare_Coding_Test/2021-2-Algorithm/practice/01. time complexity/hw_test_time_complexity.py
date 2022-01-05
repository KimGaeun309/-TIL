import time, random

# code for O(n^2)-time function
def evaluate_n2(A, x):
    answer = 0
    for i in range(n):
        axn = A[i]
        for j in range(i):
            axn *= x
        answer += axn
    return answer


# code for O(n)-time function
def evaluate_n(A, x):
    answer = 0
    tmp = 1  # x 의 제곱 값을 저장할 변수
    for i in range(n):
        answer += (tmp * A[i])
        tmp *= x
    return answer


random.seed()  # random 함수 초기화
# n 입력받음
n = int(input())
A = []
# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
for i in range(n):
    A.append(random.randint(-1000, 1000))

x = random.randint(-1000, 1000)

# evaluate_n2 호출
n2_s = time.process_time()
evaluate_n2(A, x)
n2_e = time.process_time()

# evaluate_n 호출
n_s = time.process_time()
evaluate_n(A, x)
n_e = time.process_time()

# 두 함수의 수행시간 출력
print(f"evaluate_n2 time = {n2_e - n2_s}")
print(f"evaluate_n  time = {n_e - n_s}")
