# Problem 1: Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def two_sum(nums, target):
  # Your solution here
  list = []
  for num1 in range(len(nums)):
      for num2 in range(len(nums)):
        if nums[num1]+nums[num2] == target and num1 != num2:
          list.append(num1)
          list.append(num2)
          return list
        else:
          pass


two_sum([6,4,2], 8)
