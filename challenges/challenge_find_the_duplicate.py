def find_duplicate(nums):
    if not nums or len(nums) == 1:
        return False

    duplicate_nums = set()
    for num in nums:
        if isinstance(num, str) or num < 1:
            return False
        if num in duplicate_nums:
            return num
        duplicate_nums.add(num)

    return False
