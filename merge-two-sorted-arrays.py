# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

# Time:  o(n)
# Sapce: o(1)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        for i in range(n):
            nums1[m + i] = nums2[i]
        
        nums1.sort()
        print(nums1)

if __name__ == "__main__":
    nums1 = [2,0]
    print(Solution().merge(nums1,1,[1],1))
    print(nums1)