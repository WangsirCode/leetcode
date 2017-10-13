# Given two strings s and t which consist of only lowercase letters.

# String t is generated by random shuffling string s and then add one more letter at a random position.

# Find the letter that was added in t.

# Example:

# Input:
# s = "abcd"
# t = "abcde"

# Output:
# e

# Explanation:
# 'e' is the letter that was added.

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        list_s = sorted(s)
        list_t = sorted(t)

        index = 0
        while index < len(list_s):
            if list_s[index] != list_t[index]:
                return list_t[index]
            index += 1

        return list_t[-1]

if __name__ == "__main__":
    print(Solution().findTheDifference("asdfff","asffdff"))