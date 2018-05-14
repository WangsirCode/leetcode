# Given an array of integers, every element appears twice except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Time:  o(n)
# Space: o(1)
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
        while index < len(nums):
            if index + 1 == len(nums):
                return nums[index]
            elif nums[index] != nums[index + 1]:
                return nums[index]
            else:
                index += 1
            index += 1
        return ValueError

    def singleNumberXor(self, nums):
        # known that A XOR A = 0 and the XOR operator is commutative, the solution will be very straightforward.
        result = 0
        for i in nums:
            result ^= i
        return result

if __name__ == "__main__":
    print(Solution().singleNumber([1,1,2]))
    print(Solution().singleNumber([2]))
    print(Solution().singleNumberXor([1,1,2]))
    print(Solution().singleNumberXor([2]))

