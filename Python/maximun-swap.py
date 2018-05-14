# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
# Note:
# The given number is in the range [0, 108]
import copy
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = list(str(num))
        sortedNums = sorted(nums,reverse=True)
        for i in range(len(nums)):
            if nums[i] != sortedNums[i]:
                # swap
                temp = copy.copy(nums)
                temp.reverse()
                index = len(nums) - temp.index(sortedNums[i]) - 1
                nums[index] = nums[i]
                nums[i] = sortedNums[i]
                break
        return reduce(lambda x,y:10*x + int(y), nums, 0 )

if __name__ == "__main__":
    print(Solution().maximumSwap(2736))
    print(Solution().maximumSwap(9973))
    print(Solution().maximumSwap(98368))
    print(Solution().maximumSwap(98368))
    print(Solution().maximumSwap(1993))
