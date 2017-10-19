# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        self.substring = ""
        self.maxlen = 0
        if len(s) < 2:
            return len(s)

        for index, ch in enumerate(s[:-1]):
            self.substring = ch
            j = index
            while -1 == self.substring.find(s[j+1]):
                self.substring += s[j + 1]
                j += 1
                if j == len(s) - 1:
                    break
            if self.maxlen < len(self.substring):
                self.maxlen = len(self.substring)
        
        return self.maxlen

class Solution2:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
            

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("b"))