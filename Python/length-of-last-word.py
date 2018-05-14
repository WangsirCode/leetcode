# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# For example, 
# Given s = "Hello World",
# return 5.
# 1,python 字符串处理
# Time:  O(n)
# Space: O(1)
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = s.rfind(' ')
        if index == -1:
            return len(s)
        elif index == len(s) - 1:
            return self.lengthOfLastWord(s[:len(s) - 1])
        else:
            return len(s) - index - 1

class Solution2:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])

           
if __name__ == "__main__":
    print(Solution().lengthOfLastWord("sadf asdfasf asdfa aaf"))
    print(Solution().lengthOfLastWord("sadf "))
    print(Solution().lengthOfLastWord(""))
    print(Solution().lengthOfLastWord("sadf"))
