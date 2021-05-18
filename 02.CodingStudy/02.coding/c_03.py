# 문제 설명
# 이 문제에서 A0, X, Y, M, n 이 주어진다.
# 당신은 아래의 규칙에 따라 리스트 A를 만들어야 한다.
#
# A[0] = A0
# A[i] = (A[i - 1] * X + Y) MOD M (단, 0 < i < n)
#
# 리스트 A에서 절대값의 차가 가장 작은 두 요소의 절대값의 차를 리턴하시오. ( 자세한 내용은 예제 참고 )
#
# 참고 / 제약 사항
# 1 <= A0, X, Y, M <= 10000
# 2 <= n <= 10000


class Solution:
    def solution(self, A0, X, Y, M, n):
        A = []
        min = 0xFFFFFFFF
        A.append(A0)
        for i in range(1,n):
            A.append((A[i-1]*X+Y)%M)
        A.sort()
        for i in range(len(A)-1):
            minus = A[i+1] - A[i]
            if min > minus:
                min = minus
        return min

b = Solution()
# print(b.solution(3,7,1,101,5))
# print(b.solution(3,9,8,32,8))
print(b.solution(67,13,17,4003,23))
print(b.solution(1,1221,3553,9889,11))
print(b.solution(1,1,1,2,10000))