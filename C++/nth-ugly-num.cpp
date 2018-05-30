#include<vector>

class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> dp(1,1);
        int i2 = 0, i3 = 0, i5 = 0;
        while(dp.size() < n)
        {
            dp.push_back(min(dp[i2]*2,min(dp[i3]*3),dp[i5]*5));
            if(dp.back() == dp[i2] * 2)i2++;
            if(dp.back() == dp[i3] * 3)i3++;
            if(dp.back() == dp[i5] * 5)i5++;
        }
        return dp.back();
    }
};