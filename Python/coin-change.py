
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)

# Example 2:
# coins = [2], amount = 3
# return -1.

# Note:
# You may assume that you have an infinite number of each kind of coin.
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        rt = [-1] * (amount + 1)
        rt[0] = 0
        for i in range(amount+1):
            for j in coins:
                if j > i:
                    continue
                if rt[i-j] != -1:
                    if rt[i] == -1:
                        rt[i] = rt[i-j] + 1
                    else:
                        rt[i] = min([rt[i], rt[i-j] + 1])

        return rt[-1]
        