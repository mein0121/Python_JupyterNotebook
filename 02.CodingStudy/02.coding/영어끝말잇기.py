import math


def solution(n, words):
    answer = []
    index=0
    num=0
    # for idx, i in enumerate(words):
    #     if i in words:
    #         index = idx
    for idx, i in enumerate(words):
        if i not in answer:
            answer.append(i)
        else:
            index = idx
            break
    for j in range(1,len(words)):
        if words[j][0] != words[j-1][-1]:
            num = j
            break
    if index!=0 or num != 0:
        if index < num:
            index = num
    elif index == 0 and num ==0:
        return [0,0]
    else:
        if index > num:
            index = num

    return [index%n+1, math.ceil((index+1)/n)]


w = ['qwe', 'eqwe', 'eqwe']
n = 2
print(solution(n,w))


def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]:
            return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]


def solution(n, words):

    for j in range(1, len(words)):
        if words[j][0] != words[j - 1][-1] or words[j] in words[:j]:
            return [j % n + 1, (j // n) + 1]
    else:
        return [0, 0]