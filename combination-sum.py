# Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7, 
# A solution set is: 
# [
#   [7],
#   [2, 2, 3]
# ]
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        subsets = self.subsets(candidates)
        def func(acc, candidate):
            if (sum(candidate) == target):
                acc.append(candidate)
            return acc
        return reduce(func, subsets, [])
    

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
    print(Solution().combinationSum([2, 3, 6, 7] , 7))