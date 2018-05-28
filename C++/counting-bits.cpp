#include<vector>
#include <iostream>

using namespace std;
// An easy recurrence for this problem is f[i] = f[i / 2] + i % 2.
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> dp(num + 1, 0);
        for (int i = 1; i < num + 1; i ++)
        {
            dp[i] = dp[i >> 1] + i % 2;
        }
        return dp;
    }
};

int main()
{
    Solution s;
    vector<int> result = s.countBits(10);

    for(int i = 0; i < 11; i ++)
    {
        cout << result[i] << ",";
    }
    cout << endl;
    
    return 0;
}
