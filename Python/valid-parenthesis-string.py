# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
# Example 1:
# Input: "()"
# Output: True
# Example 2:
# Input: "(*)"
# Output: True
# Example 3:
# Input: "(*))"
# Output: True

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = []
        star = []
        if not s:
            return True
        for index, value in enumerate(s):
            if value == '(':
                left.append(index)
            elif value == '*':
                star.append(index)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        if not left:
            return True
        elif len(left) > len(star):
            return False
        else:
            index = -1
            for i in left:
                index +=1
                if index == len(star):
                    return False
                while(star[index] < i) :
                    index += 1
                    if index == len(star):
                        return False
                
            return True


if __name__ == "__main__":
    print(Solution().checkValidString("()*()**()(())(()()(())*)()((()**))()()()(((*(((*)))(**(())))*()*))()(()()(()))()((())(*()())())()(*"))