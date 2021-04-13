def solution(nums):

    l = len(nums)//2
    n = len(set(nums))
    return min(l,n)


nums = [3, 3, 3, 2, 2, 2]
print(solution(nums))