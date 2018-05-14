# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]
        before = self.generate(numRows - 1)
        last = before[-1]
        result = [1]
        for i in range(numRows - 2):
            result.append(last[i] + last[i + 1])
        result.append(1)
        before.append(result)
        return before

if __name__ == "__main__":
    print(Solution().generate(4))