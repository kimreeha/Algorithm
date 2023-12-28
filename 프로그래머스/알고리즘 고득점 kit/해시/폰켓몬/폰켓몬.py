def solution(nums):
    num = list(set(nums))
    return len(num[:len(nums)//2])