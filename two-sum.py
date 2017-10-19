
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
import collections
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        reslut = collections.defaultdict(lambda: -1)
        for index, num in enumerate(nums):
            if reslut[num] != -1:
                return [reslut[num], index]
            else:
                reslut[target - num] = index

if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15],26))