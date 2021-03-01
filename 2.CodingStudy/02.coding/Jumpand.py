# def solution(n):
#     ans = 0
#     while n > 0:
#         ans += n % 2
#         n = n // 2
#
#     return ans


# Using binary function

def solution(n):
    return bin(n).count('1')


solution(5000)
