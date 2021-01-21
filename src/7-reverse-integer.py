# @File : 7-reverse-integer.py
# @Author : Shane Shek
# @Date : 2021-01-21 16:52:19
# @Desc : 整数反转

# 给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。
#
#  如果反转后整数超过 32 位的有符号整数的范围 [−231, 231 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
#
#  示例 1：
#
# 输入：x = 123
# 输出：321
#
#  示例 2：
#
# 输入：x = -123
# 输出：-321
#
#  示例 3：
#
# 输入：x = 120
# 输出：21
#
#  示例 4：
#
# 输入：x = 0
# 输出：0
#
#  提示：
#
#  -231 <= x <= 231 - 1

# class Solution:
#     def reverse(self, x: int) -> int:
#         if x <= pow(-2, 31) or x >= pow(2, 31) - 1:
#             return 0
#         minus = False
#         if x < 0:
#             x = -x
#             minus = True
#         s = str(x)
#         t = pow(10, len(s) - 1)
#         sum = 0
#         for i in range(0, len(s)):
#             sum = sum + (x % 10) * t
#             x = int(x / 10)
#             t = t / 10
#         if sum <= pow(-2, 31) or sum >= pow(2, 31) - 1:
#             return 0
#         if minus:
#             return int(-sum)
#         return int(sum)
class Solution:
    def reverse(self, x: int) -> int:
        if x <= pow(-2, 31) or x >= pow(2, 31) - 1:
            return 0
        minus = False
        if x < 0:
            x = -x
            minus = True
        re = int(str(x)[::-1])
        if re <= pow(-2, 31) or re >= pow(2, 31) - 1:
            return 0
        if minus:
            return -re
        return re
