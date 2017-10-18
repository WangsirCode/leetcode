# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example:

# Input: "babad"

# Output: "bab"

# Note: "aba" is also a valid answer.
# Example:

# Input: "cbbd"

# Output: "bb"

class Solution(object):
    def __init__(self):
        self.maxLen = 0
        self.lo = 0

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        for index,value in enumerate(s):
            self.extendPalindrome(s,index,index)
            self.extendPalindrome(s,index,index + 1)
        
        return s[self.lo:self.lo + self.maxLen]

    def extendPalindrome(self,s,i,j):
        while i>=0 and j < len(s) and s[i] == s[j]:
            i -=1
            j +=1
        
        if self.maxLen < j - i - 1:
            self.maxLen = j - i - 1
            self.lo = i + 1



if __name__ == '__main__':
    print(Solution().longestPalindrome("abccba"))