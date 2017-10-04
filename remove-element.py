# Given an array and a value, remove all instances of that value in place and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Example:
# Given input array nums = [3,2,2,3], val = 3

# Your function should return length = 2, with the first two elements of nums being 2.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        last,length = 0,0
        for value in nums:
            if value != val:
                nums[last] = value
                length += 1
                last += 1
        print(nums[:length])
        return length

if __name__ == "__main__":
    print(Solution().removeElement([1, 2, 3, 4, 5, 2, 2], 2))