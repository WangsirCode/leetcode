# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        result = [float('inf')] * (n + 1)
        result[0] = 0
        for i in range(1,n+1):
            j = 1
            while j * j <= i:
                result[i] = min(result[i],result[i - j*j] + 1)
                j += 1
        return result[n]
