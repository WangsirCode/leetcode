# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

# Example 1:
# Input: "abab"

# Output: True

# Explanation: It's the substring "ab" twice.
# Example 2:
# Input: "aba"

# Output: False
# Example 3:
# Input: "abcabcabcabc"

# Output: True

# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_len = len(s)
        for i in range(int(str_len / 2)):
            substring_len = i - 0 + 1
            
            if 0 == str_len % substring_len:
                substring = s[0:i + 1]
                sb = substring
                times = int(str_len / substring_len) - 1
                for i in range(times):
                    sb += substring
                if sb == s:
                    return True
        return False

if __name__ == "__main__":
    print(Solution().repeatedSubstringPattern("abab"))
                    