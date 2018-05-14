# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# For example,
# Given nums = [0, 1, 3] return 2.

# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return ValueError
        
        i = 0
        nums.sort()
        while i < len(nums):
            if nums[i] != i:
                return i
            i += 1
        return i


if __name__ == "__main__":
    print(Solution().missingNumber([0,1,2,4]))
    print(Solution().missingNumber([1,2]))
    print(Solution().missingNumber([0]))
