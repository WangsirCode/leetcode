class Solution(object):
    def countBinarySubstrings(self, s):
        s = map(len, s.replace('01', '0 1').replace('10', '1 0').split())
        return sum(min(a, b) for a, b in zip(s, s[1:]))

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
    
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        isLoewr = word.lower() == word
        isuppper = word.upper() == word
        firstCapital = (word.lower()[1:] == word[1:] and word.upper()[0] == word[0])
        return isLoewr or isuppper or firstCapital