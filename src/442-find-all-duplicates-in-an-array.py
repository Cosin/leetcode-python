# @File : 442-find-all-duplicates-in-an-array.py
# @Author : Shane Shek
# @Date : 2021-07-24 14:51:46
# @Desc : 数组中重复的数据

# 给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。 
# 
#  找到所有出现两次的元素。 
# 
#  你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？ 
# 
#  示例： 
# 
#  
# 输入:
# [4,3,2,7,8,2,3,1]
# 
# 输出:
# [2,3]

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        result = []
        n = len(nums)
        for i in range(n):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                result.append(num)
            else:
                nums[num - 1] = -nums[num - 1]
        return result
