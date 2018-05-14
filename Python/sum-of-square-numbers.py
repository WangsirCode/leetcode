# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

# Example 1:
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:
# Input: 3
# Output: False
# Time:  o(logn)
# Space: o(1)
# 1. python ** //
# 2. any all
# 3. 列表生成器
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def is_square(N):
            return int(N**0.5)**2 == N
        return any(is_square(c - a**2) for a in range(int(c**0.5) + 1))

if __name__ == "__main__":
    print(Solution().judgeSquareSum(5))
    print(Solution().judgeSquareSum(4))
    print(Solution().judgeSquareSum(111111111111111111111111))