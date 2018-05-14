# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        result = []
        if nums[0] != 1:
            result += [i + 1 for i in range(nums[0] - 1)]
        for index, value in enumerate(nums):
            if index < len(nums) - 1:
                num = value
                if value == nums[index+1]:
                    continue 
                while num + 1 != nums[index + 1]:
                    result.append(num + 1)
                    num += 1
            else:
                num = value
                while num != len(nums):
                    num += 1
                    result.append(num)
        return result

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

if __name__ == "__main__":
    print(Solution().findDisappearedNumbers([2,2]))