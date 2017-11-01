# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?

# Would this affect the run-time complexity? How and why?
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# The array may contain duplicates.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]

            mid = (start + end) // 2
            
            if nums[mid] > nums[start]:
                start = mid + 1
            elif nums[mid] == nums[start]:
                start = start + 1
            else:
                end = mid
        return nums[start]

if __name__ == "__main__":
    print(Solution().findMin([10,1,10,10,10]))
    print(Solution().findMin([3,3,1]))