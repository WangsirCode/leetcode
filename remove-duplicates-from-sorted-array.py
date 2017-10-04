# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example,
# Given input array nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        last = 0 
        for num in nums[1:]:
            if nums[last] != num:
                last += 1
                nums[last] = num
        print(nums[:last + 1])
        return last + 1

if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 2,4,5,6]))
    print(Solution().removeDuplicates([1, 1, 1, 2]))
    print(Solution().removeDuplicates([1, 1, 2,2,4,5,66,77,77]))


# wrong solution 
# remove 的复杂度是o(n)
# 整体的复杂度为o(n^2)
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         length, current = 1, nums[0]
#         for num in nums[1:]:
#             if current != num:
#                 length = length + 1
#                 current = num
#             else:
#                 nums.remove(num)
#         return length