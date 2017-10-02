# Write a function to find the longest common prefix string amongst an array of strings.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        strs = sorted(strs, key=len)
        print(strs)
        lens = len(strs[0])
        for i in range(lens):
            prefix = strs[0][:lens - i]
            num = 1
            for value in strs[1:]:
                if value.startswith(prefix):
                    num = num + 1
                else:
                    break
            if num == len(strs):
                return prefix
        return ""

if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["heao", "heaven", "heavy","hea"]))