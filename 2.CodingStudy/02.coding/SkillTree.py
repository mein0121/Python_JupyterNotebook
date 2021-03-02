def solution(skill, skill_trees):
    answer=0
    for i in skill_trees:
        skill_list = list(skill)
        for j in i:
            if j in skill_list:
                if j != skill_list.pop(0):
                    break
        else:
            answer +=1
    return answer

a = "CBDK"
b = ["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"]

print(solution(a,b))