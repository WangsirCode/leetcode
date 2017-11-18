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
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 1:
            return flowerbed[0] + n <= 1
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
        
        return n <= 0
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
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedArray = sorted(nums)
        l, r = 0, len(nums) - 1
        while sortedArray[l] == nums[l] and l < len(nums):
            l += 1
        while sortedArray[r] == nums[r] and r >  0:
            r -= 1
        
        return r - l + 1 if r >l else 0
    
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += r - l
                    l += 1
                else:
                    r -= 1
        
        return count
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