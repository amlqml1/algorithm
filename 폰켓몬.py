from collections import Counter
def solution(nums):
    answer = len(Counter(nums))
    if len(nums)//2 < answer:
        return len(Counter(nums))-1
    return len(Counter(nums))

print(solution([3,1,2,3]))