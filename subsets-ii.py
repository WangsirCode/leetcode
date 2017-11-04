# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsetsWithDup(self, nums):
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
                    candidate1.sort()
                    candidate2.sort()
                    if candidate1 not in next:
                        next.append(candidate1)
                    if candidate2 not in next:
                        next.append(candidate2)
                
            solutions = next 
            
        return solutions

if __name__ == "__main__":
    print(Solution().subsetsWithDup([1,2,3]))
    print(Solution().subsetsWithDup([1,2,2]))