# Time:  O(n * glogg), g is the max size of groups.
# Space: O(n)
#
# Given an array of strings, return all groups of strings that are anagrams.
#
# Note: All inputs will be in lower-case.
#
# 1.python for 循环
# 2.iterable and iterator
# 3. sorted ,map , filter

import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        maps,result = collections.defaultdict(list),[]
        for str in strs:
            key = ("").join(sorted(str))
            maps[key].append(str)

        for value in maps.values():
            value.sort()
            result.append(value)

        return result


if __name__ == "__main__":
    result = Solution().groupAnagrams(["cat", "dog", "act", "mac"])
    print result