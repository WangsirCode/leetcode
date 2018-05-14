# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note:

# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
class Solution:
    def minimumTotal(self, triangle):
        if not triangle or not triangle[0]:
            return 0
        m = [triangle[0][0]]
        for i in range(1, len(triangle)):
            row = triangle[i]
            m.append(row[-1] + m[-1])
            for j in range(1, i):
                m[j] = row[j] + min(m[j], m[j-1])
            m[0] = row[0] + m[0]
        return min(m)

if __name__ == "__main__":
    print(Solution().minimumTotal1([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))