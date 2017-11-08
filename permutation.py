# Given a collection of distinct numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution(object):
    # def permute(self, nums):
        # """
        # :type nums: List[int]
        # :rtype: List[List[int]]
        # """
        # return [[n] + p
        #     for i, n in enumerate(nums)
        #     for p in self.permute(nums[:i] + nums[i+1:])] or [[]]
    
    def permute(self, nums):
        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]
                
        ans = []
        backtrack(0, len(nums))
        return ans

if __name__ == "__main__":
    print(Solution().permute([1,2,3]))

        