# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
import collections
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        appearedIndex = collections.defaultdict(lambda : -1)
        for index, num in enumerate(nums):
            if appearedIndex[num] != -1:
                if index - appearedIndex[num] <= k:
                    return True
            appearedIndex[num] = index
        
        return False