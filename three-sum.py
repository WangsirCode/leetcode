# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
import collections
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        used = collections.defaultdict(int)
        nums.sort()
        zero = -1 
        if not nums:
            return result
        for index,num in enumerate(nums):
            if num >= 0:
                zero = index
                break
        if nums[zero] == 0 and (zero + 2) < len(nums):
            if nums[zero+1] == 0 and nums[zero + 2] == 0:
                result.append([0,0,0])
        for num in nums[:zero]:
            if used[num] == 0:
                twosums = self.twoSum(nums[zero:],-num)
                used[num] = 1
                for twosum in twosums:
                    result.append(twosum + [num])
        for num in nums[zero:]:
            if used[num] == 0:
                twosums = self.twoSum(nums[:zero],-num)
                used[num] = 1
                for twosum in twosums:
                    result.append(twosum + [num])
                
        return result

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        anwser = collections.defaultdict(lambda: -1)
        aleady = collections.defaultdict(int)
        result = []
        for index, num in enumerate(nums):
            if anwser[num] != -1 and aleady[num] == 0:
                result.append([nums[anwser[num]], num])
                aleady[num] = 1
            else:
                anwser[target - num] = index
        return result
    
if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum([0,0,0]))
    print(Solution().threeSum([-2,0,1,1,2]))