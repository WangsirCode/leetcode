# Given a sorted integer array without duplicates, return the summary of its ranges.

# Example 1:
# Input: [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Example 2:
# Input: [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        start, end = nums[0], nums[0]
        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i] + 1:
                end += 1
            else:
                ranges = "%d" % start if start == end else "%d->%d" % (start,end)
                result.append(ranges)
                start, end = nums[i + 1], nums[i + 1]
        
        ranges = "%d" % start if start == end else "%d->%d" % (start,end)
        result.append(ranges)
        return result

if __name__ == "__main__":
    print(Solution().summaryRanges([0,1,2,4,5,7]))