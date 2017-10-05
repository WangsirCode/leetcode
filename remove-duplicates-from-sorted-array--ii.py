# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array nums = [1,1,1,2,2,3],

# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
# Time:  O(n)
# Space: O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        last = 0
        duplicate = float("inf")
        for num in nums[1:]:
            if nums[last] != num:
                last += 1
                nums[last] = num
            elif num != duplicate:
                last += 1
                nums[last] = num
                duplicate = num

        print(nums[:last + 1])
        return last + 1

if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 2,4,5,6]))
    print(Solution().removeDuplicates([1, 1, 1, 2]))
    print(Solution().removeDuplicates([1, 1, 2,2,2,4,5,5,5,5,66,77,77,77]))