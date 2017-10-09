# Determine whether an integer is a palindrome. Do this without extra space.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reversed = self.reverse(x)
        return reversed == x
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)

        result = 0
        while x:
            result = result * 10 + x % 10
            x /= 10
        return result if result <= 0x7fffffff else 0  # Handle overflow.

if __name__ == "__main__":
    print(Solution().isPalindrome(12321))
    print(Solution().isPalindrome(1231))
    print(Solution().isPalindrome(1221))
