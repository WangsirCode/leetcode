# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# You may assume no duplicate exists in the array.

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
            
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid
        return nums[start]

if __name__ == "__main__":
    print(Solution().findMin([3,4,5,1,2]))