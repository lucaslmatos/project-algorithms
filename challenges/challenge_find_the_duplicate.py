def find_duplicate(nums):
    if len(nums) <= 1 or type(nums) == str:
        return False
    num_count = {}
    for num in nums:
        if type(num) == str or num < 0:
            return False
        if num in num_count:
            return num
        num_count[num] = 1
    return False
