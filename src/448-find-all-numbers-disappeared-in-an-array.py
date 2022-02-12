# @File : 448-find-all-numbers-disappeared-in-an-array.py
# @Author : Shane Shek
# @Date : 2022-02-12 22:08:48
# @Desc : 找到所有数组中消失的数字

# 给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数
# 字，并以数组的形式返回结果。 
#
#  示例 1： 
# 输入：nums = [4,3,2,7,8,2,3,1]
# 输出：[5,6]
#
#  示例 2： 
# 输入：nums = [1,1]
# 输出：[2]
# 
#  提示： 
#  n == nums.length
#  1 <= n <= 10⁵ 
#  1 <= nums[i] <= n
from typing import List


class Solution:
    def findDisappearedNumbers_1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        s = set()
        for num in nums:
            s.add(num)
        for i in range(1, n + 1):
            if i not in s:
                result.append(i)
        return result

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = []
        for num in nums:
            # 取模的目的是，所在位置的值可能已被增加过，取模后还原值
            nums[(num - 1) % n] += n
        for i in range(0, n):
            if nums[i] <= n:
                result.append(i + 1)
        return result