# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Here are few examples.
# [1,3,5,6], 5  2
# [1,3,5,6], 2  1
# [1,3,5,6], 7  4
# [1,3,5,6], 0  0
# Time:  O(n)
# Space: O(1)
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        order = 0
        for i in nums:
            if i == target:
                return index
            index += 1
            if target > i:
                order += 1
        
        return order

if __name__ == "__main__":
    print(Solution().searchInsert([1,2,3,4],3))
    print(Solution().searchInsert([1,2,3,4],6))
    print(Solution().searchInsert([1,2,5,6],3))