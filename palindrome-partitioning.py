# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# For example, given s = "aab",
# Return

# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

class Solution(object):
    def partition(self, s):
        def backtrack(start, end, tmp):
            if start == end:
                ans.append(tmp[:])
            for i in range(start, end):
                cur = s[start:i+1]
                if cur == cur[::-1]:
                    tmp.append(cur)
                    backtrack(i+1, end, tmp)
                    tmp.pop()
        ans = []
        backtrack(0, len(s), [])
        return ans

if __name__ == "__main__":
    print(Solution().partition("aab"))
        