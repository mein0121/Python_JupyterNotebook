# 문제 설명
# 나라마다 통용되는 화폐의 단위와 갯수는 다르다.
#
# 화폐 단위의 예)
# 대한민국: 10원, 50원, 100원, 500원, 1000원, 5000원, 10000원, 50000원
# 영국: 1페니, 2펜스, 5펜스, 10펜스, 20펜스, 50펜스, 1파운드(100펜스), 2파운트(200펜스)
#
# currencies의 각 요소는 이 나라에서 사용되는 화폐의 단위를 나타낸다.
# 이 나라의 화폐를 이용하여, wantMoney만큼의 돈을 거슬러주는 모든 방법의 수를 리턴하시오.
#
# 참고 / 제약 사항
# currencies에 포함되어 있는 요소의 갯수는 1개이상이며 100개이하 이다.
# currencies의 각 요소의 값은 1이상이며 1000이하 이다.
# wantMoney의 값은 1이상이며 1000이하 이다.
# 테스트 케이스
# currencies = [1,5,10]
# wantMoney = 10리턴(정답): 4
# 10을 만드는 방법을 나열하면, 1x10 = 10, 1x5 + 5x1 = 10, 5x2 = 10, 10x1 = 10 이므로 4개이다.
#
# currencies = [4,25,40]
# wantMoney = 80리턴(정답): 3
# 80을 만드는 방법을 나열하면, 4x20 = 80, 4x10 + 40x1 = 80, 40x2 = 80 이므로 3개이다.
#
# currencies = [1,21,24,31,35,37,47]
# wantMoney = 57리턴(정답): 13
# currencies = [10,11,38]
# wantMoney = 90리턴(정답): 2
# currencies = [10,11,38,39,40,41,48]
# wantMoney = 55리턴(정답): 1

class Solution:
    def solution(self, currencies, wantMoney):
        # [x for x in goldValues if goldValues.index(x) < mypick or goldValues.index(x) > oppick]
        count=0

        # m = [x for x in currencies if wantMoney]
        for x in range(len(currencies)):
            if wantMoney%currencies[x]==0:
                count+=1



    return 0