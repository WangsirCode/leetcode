# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

# For example, with A = "abcd" and B = "cdabcdab".

# Note:
# The length of A and B will be between 1 and 10000.

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        C = A
        result = 1
        while 1:
            if B in C:
                return result
            else:
                if len(C) > 2 * len(B):
                    break
                C += A
                result += 1
        
        return -1

if __name__ == "__main__":
    print(Solution().repeatedStringMatch("abababaaba","aabaaba"))