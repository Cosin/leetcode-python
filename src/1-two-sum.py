from typing import List

"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,

return [0, 1].

"""


# 1. violence
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(0, len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# 2. hash table
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         dict = {}
#         for i in range(0, len(nums)):
#             dict[nums[i]] = i
#         for i in range(0, len(nums)):
#             find = target - nums[i]
#             if find in dict.keys() and i != dict[find]:
#                 return [dict[find], i]

# 3. hash table - improvement
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(0, len(nums)):
            find = target - nums[i]
            if find in dict.keys() and i != dict[find]:
                return [dict[find], i]
            else:
                dict[nums[i]] = i


if __name__ == "__main__":
    solution = Solution()
    # print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 3, 5], 6))
