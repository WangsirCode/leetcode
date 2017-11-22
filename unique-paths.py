# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.facotor(m + n - 2)/ (self.facotor(m - 1) * self.facotor(n - 1))
        
    def facotor(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * self.facotor(n - 1)
    
