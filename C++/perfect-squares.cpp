
// Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

// Example 1:

// Input: n = 12
// Output: 3 
// Explanation: 12 = 4 + 4 + 4.
// Example 2:

// Input: n = 13
// Output: 2
// Explanation: 13 = 4 + 9.
#include<vector>
#include<algorithm>
using namespace std;
class Solution 
{
    public:
        int numSquares(int n) 
        {
            if (n <= 0)
            {
                return 0;
            }
            
            // cntPerfectSquares[i] = the least number of perfect square numbers 
            // which sum to i. Note that cntPerfectSquares[0] is 0.
            vector<int> cntPerfectSquares(n + 1, INT_MAX);
            cntPerfectSquares[0] = 0;
            for (int i = 0; i <= n; i++)
            {
                for (int j = 1; j*j <= i; j ++)
                {
                    cntPerfectSquares[i] = min(cntPerfectSquares[i], cntPerfectSquares[i - j*j] + 1);
                }
            }
            return cntPerfectSquares.back();
            
        }
};