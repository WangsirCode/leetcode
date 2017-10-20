
# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r, l = len(nums) - 1, 0
        index = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                index = mid
                break
        
        if index == -1:
            return [-1,-1]
        l ,r = mid, mid
        try:
            while nums[l] == target:
                l -= 1
        except:
            l = 0
        else:
            l += 1
        
        try:
            while nums[r] == target:
                r += 1
        except:
            r = len(nums) - 1
        else:
            r -= 1

        return [l,r]
if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10],8))
    print(Solution().searchRange([8, 8, 8],8))

        