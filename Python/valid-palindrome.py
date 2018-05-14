# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.

# For the purpose of this problem, we define empty string as valid palindrome.
# Time:  o(n)
# Space: o(1)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            # find the left alphanumeric character
            while  left < right and not s[left].isalnum():
                left += 1

            # find the right alphanumeric character
            while  left < right and not s[right].isalnum():
                right -= 1
            
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("race a car"))  
    print(Solution().isPalindrome(""))  