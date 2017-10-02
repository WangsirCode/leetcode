# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
# 1. list 方法 pop append
# 2. 考虑到 '[' ']'这样的情况
# 3. Python 逻辑操作 为 not or and 
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        lookupTable = {"{":"}","[":"]","(":")"}
        for ch in s:
            if ch == '{' or ch == '[' or ch == '(':
                stack.append(ch)
            else:
                if not stack:
                    return False
                else:                    
                    first = stack.pop()
                    if ch != lookupTable[first]:
                        return False
        return (not stack)

if __name__ == "__main__":
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("()[{]}"))
    print(Solution().isValid("]"))
    print(Solution().isValid("["))
