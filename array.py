class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, sum(nums[1:])
        for index, value in enumerate(nums):
            if left == right:
                return index
            if index == len(nums) - 1:
                break
            left += value
            right -= nums[index + 1]
        return -1
    
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

    
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        product = 1
        left = 0
        for index,value in enumerate(nums):
            product *= value
            while left <= index and product >= k:
                product /= nums[left]
                left += 1
            count += index - left + 1
        return count

    def findShortestSubArray(self, nums):
        c = collections.Counter(nums)
        first, last = {}, {}
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            last[v] = i
        degree = max(c.values())
        return min(last[v] - first[v] + 1 for v in c if c[v] == degree)