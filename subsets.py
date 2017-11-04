# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutions = [[]]
        
        for num in nums:
            next = []
            for solution in solutions:
                    candidate1 = solution + []
                    candidate2 = solution + [num]
                    next.append(candidate1)
                    next.append(candidate2)
                
            solutions = next 
            
        return solutions

if __name__ == "__main__":
    print(Solution().subsets([1,2,3]))