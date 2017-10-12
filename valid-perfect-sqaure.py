# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Returns: True
# Example 2:

# Input: 14
# Returns: False
# Time : o(logn)
# Space: o(1)

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return self.mySqrt(num)*self.mySqrt(num) == num

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return ValueError
        elif x < 2:
            return x
        
        left, right = 1, int(x/2)
        while left <= right:
            mid = (left + right) // 2
            if mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1
        return right