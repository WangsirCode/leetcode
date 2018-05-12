# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:

# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        longest = [0] * len(s)
        curMax = 0
        for i in range(1,len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    longest[i] = longest[i-2] + 2 if (i - 2) > 0 else 2
                    curMax = max(curMax,longest[i])
                else:
                    if i-longest[i-1]-1 >= 0 and s[i-longest[i-1]-1] == '(':
                        longest[i] = longest[i-1] + 2 + (longest[i-longest[i-1]-2] if (i-longest[i-1]-2 >= 0) else 0) 
                        curMax = max(longest[i],curMax) 
        return curMax


if __name__ == "__main__":
    print(Solution().longestValidParentheses(")(())))(())())"))
    
        