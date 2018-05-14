# Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return ValueError
        index = 0
        nums.sort()
        while index < len(nums):
            if index + 1 == len(nums):
                return nums[index]
            elif nums[index] != nums[index + 1]:
                return nums[index]
            else:
                index += 3
        return ValueError

if __name__ == "__main__":
    print(Solution().singleNumber([1,1,1,2]))
    print(Solution().singleNumber([2]))