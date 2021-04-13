import math


def solution(progresses, speeds):
    work = [] # 남는 작업기간
    answer = []
    # 작업 남은 기간 저장
    for i, j in zip(progresses, speeds):
        work.append(math.ceil((100 - i) / j))
    curr = work[0] # 기준작업기간
    count = 0
    # 기준작업기간보다 i의 작업기간이 길면 그전 작업들은 배포.
    # 기준작업기간은 i 작업기간으로 변경
    for i in work:
        if curr < i:
            curr = i
            answer.append(count)
            count = 0
        count += 1
    answer.append(count)
    return answer
