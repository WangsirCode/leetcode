class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]
        i2,i3,i5 = 0
        while len(dp) < n:
            dp.append(min(dp[i2]*2,dp[i3]*3,dp[i5]*5))
            if(dp[-1] == dp[i2] * 2):
                i2 += 1
            if(dp[-1] == dp[i3] * 3):
                i3 += 1
            if(dp[-1] == dp[i5] * 5):
                i5 += 1

        return dp[-1]
            