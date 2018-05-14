# Implement int sqrt(int x).

# Compute and return the square root of x.
# Time : o(logn)
# Space: o(1)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return ValueError
        elif x < 2:
            return x
        
        left, right = 1, int(x/2)
        while left <= right:
            mid = (left + right) // 2
            if mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1
        return right

if __name__ == "__main__":
    print(Solution().mySqrt(10))
    print(Solution().mySqrt(20))
