# 문제 설명
# 제인은 몸매를 유지하기위해 최선의 노력을 다한다. 그녀의 여동생이 이것을 알고 제인에게 장난을 치기로 한다:
# 제인의 오래된 체중계가 고장난 이후 제인의 여동생은 실제 몸무게가 아니라 몸무게의 제곱을 보여주는 체중계를 제인에게 줬다.
#
# 이 사실을 모른채 제인은 몸무게를 얼마간 사용해왔다. 어느 날 아침 그녀는 " apparentGain 만큼 살이 쪘어!"라고 소리지른다.
# 주어진 apparentGain (제인 현재 몸무게의 제곱과 예전 몸무게의 제곱의 차이)을 이용해서 가장 최근의 측정 이후
# 가능한 제인의 실제 몸무게를 오름차순으로 정렬한 정수값의 배열을 리턴하시오.
#
# 모든 무게(체중계에 표시된 몸무게와 실제 몸무게, 예전 몸무게와 현재 몸무게)는 양의 정수이다.
#
# 참고 / 제약 사항
# apparentGain은 최소값 1, 최대값 100000의 범위를 가진다.
# 테스트 케이스
# apparentGain = 233리턴(정답): [117]
# 만약 Jane의 예전몸무게가 116 파운드였다면 체중계는 116^2 = 13456을 보여줬을 것이다.
# 제인의 체중이 1 파운드 증가했다면 체중계는 117^2 = 13689를 보여줬을 것이다.
# 이 때, apparentGain은 13689 - 13456 = 233이 된다.
#
# apparentGain = 15리턴(정답): [4,8]
# 이번 예제에서 제인을 작은 동물이라 가정한다면, 그녀는 1에서 4, 혹은 7에서 8로 몸무게가 증가하였을 것이다.
#
# apparentGain = 1440리턴(정답): [38,39,42,46,49,53,66,77,94,123,182,361]
import math


class Solution:
    def solution(self, apparentGain):
        start = math.floor(math.sqrt(apparentGain))
        print(start, "start")
        x = math.ceil(apparentGain / 2)
        print(x, "x")
        # for i in range(start, x + 1):
        #     for j in range(x):
        #         if i ** 2 - j ** 2 == apparentGain:
        #             answer.append(i)
        #             break
        #         if j >= i:
        #             break
        answer = []
        i = start
        while i <= x:
            for j in range(i-1,0,-1):
                 if i ** 2 - j ** 2 == apparentGain:
                    answer.append(i)
                    break
            i += 1
        # answer = [i for a in range(x) for i in range(start, x + 1) if (i ** 2 - a ** 2) == apparentGain and i > a]
        return answer


p = Solution()
print(p.solution(1440))
# import math
# print(math.sqrt(1440))
# print(117**2)
#
# x = (1440)/2
# print(x)
#
# for i in range(10,0, -1):
#     print(i)
