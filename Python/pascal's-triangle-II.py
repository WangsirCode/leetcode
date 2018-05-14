# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

# Note:
# Could you optimize your algorithm to use only O(k) extra space?

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        if rowIndex == 0:
            return [1]

        last = self.getRow(rowIndex - 1)
        result = [1]
        for i in range(rowIndex - 1):
            result.append(last[i] + last[i + 1])
        result.append(1)
        return result

if __name__ == "__main__":
    print(Solution().getRow(6))