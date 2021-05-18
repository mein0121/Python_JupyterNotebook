
# 문제 설명
# 의사가 당신의 다이어트 식단을 지정했다. 이 식단은 Diet로 나타낸다.
# 식단에 포함된 각 음식은 하나의 문자로 치환되며, breakfast와 lunch는 각각 아침과 점심에 먹은 음식을 낸다. 당신이 아침과 점심에 먹지 않은 음식은 전부 저녁에 먹게 된다. 당신이 저녁에 먹을 음식을 알파벳 순서로 배열하여 리턴하시오.
#
# 만약 식단에 없는 음식을 아침과 점심때 먹었거나, 혹은 식단에는 있지만 식단에 포함 된 횟수보다 더 많이 먹었을 경우 CHEATER라는 문자열을 출력하시오.
#
# 참고 / 제약 사항
# Diet, breakfast, lunch의 길이는 0이상 26이하다.
# Diet, breakfast, lunch의 각 음식은 대문자 알파벳이다.
# Diet, breakfast, lunch에는 중복된 문자가 없다.
# Breakfast와 lunch에 동시에 등장하는 음식은 없다.

class Solution:
    def solution(self, diet, breakfast, lunch):
        diet = sorted(diet)
        eat = breakfast + lunch
        eat = sorted(eat)
        answer = [x for x in diet if x not in eat]
        if ["CHEATER" for x in eat if x not in diet]:
            answer = "CHEATER"
        return "".join(answer)


p = Solution()
print(p.solution("","",""))