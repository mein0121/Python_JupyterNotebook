class Solution:
    def solution(self, goldValues):
        g = sorted(goldValues)
        answer = 0
        while g:
            answer += g.pop()
            g.pop()
        return answer

goldValues = [5,2,1,4,3,1]

a = Solution()
print(a.solution(goldValues))