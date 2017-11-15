class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, sum(nums[1:])
        for index, value in enumerate(nums):
            if left == right:
                return index
            if index == len(nums) - 1:
                break
            left += value
            right -= nums[index + 1]
        return -1