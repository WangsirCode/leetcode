# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

# For example:

# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

# Note:
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

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
        singles = []
        while index < len(nums):
            if index + 1 == len(nums):
                singles.append(nums[index])
            elif nums[index] != nums[index + 1]:
                singles.append(nums[index])
            else:
                index += 1
            index += 1
        return singles

if __name__ == "__main__":
    print(Solution().singleNumber([1,1,2,3]))
    print(Solution().singleNumber([2,1]))