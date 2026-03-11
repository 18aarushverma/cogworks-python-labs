# Problem 4: Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
def max_subarray(nums):
    max_sum = nums[0]
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum


# Test cases for Maximum Subarray
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert max_subarray([1]) == 1
assert max_subarray([5,4,-1,7,8]) == 23
