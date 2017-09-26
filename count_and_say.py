# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if 1 == n:
            return "1"
        else:
            return self.count(self.countAndSay(n-1))

    def count(self,word):
        result = ''
        count = 1
        for index,value in enumerate(word):
            if index == len(word) - 1:
                result += str(count)
                result += value
                count = 1

            elif (value != word[index + 1]):
                result += str(count)
                result += value
                count = 1
            else:
                count += 1

        return result


if __name__ == "__main__":
    result = Solution().countAndSay(10)
    print result
