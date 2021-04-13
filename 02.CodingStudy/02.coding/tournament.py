def solution(n, a, b):
    answer = 0
    a, b = a - 1, b - 1 # 0부터 시작
    while a != b:
        a = a // 2
        b = b // 2
        answer += 1
    return answer
