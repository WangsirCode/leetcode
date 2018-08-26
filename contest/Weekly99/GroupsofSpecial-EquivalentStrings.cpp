// You are given an array A of strings.

// Two strings S and T are special-equivalent if after any number of moves, S == T.

// A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping S[i] with S[j].

// Now, a group of special-equivalent strings from A is a non-empty subset of A such that any string not in A is not special-equivalent with any string in A.

// Return the number of groups of special-equivalent strings from A.

 

// Example 1:

// Input: ["a","b","c","a","c","c"]
// Output: 3
// Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]
// Example 2:

// Input: ["aa","bb","ab","ba"]
// Output: 4
// Explanation: 4 groups ["aa"], ["bb"], ["ab"], ["ba"]
// Example 3:

// Input: ["abc","acb","bac","bca","cab","cba"]
// Output: 3
// Explanation: 3 groups ["abc","cba"], ["acb","bca"], ["bac","cab"]
// Example 4:

// Input: ["abcd","cdab","adcb","cbad"]
// Output: 1
// Explanation: 1 group ["abcd","cdab","adcb","cbad"]
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

class Solution {
public:
    int numSpecialEquivGroups(vector<string>& A) {
        vector<int> isGrouped(A.size(),0);
        int result = 0;
        for(int i = 0; i < A.size(); i ++)
        {
            if(isGrouped[i])continue;
            else
            {
                result += 1;
                for (int j = i + 1; j < A.size(); j ++)
                {
                    if(isEquivalent(A[i],A[j])) isGrouped[j] = 1;
                }
            }
        }
        return result;
    }
    bool isEquivalent(string& rhs,string& lhs)
    {
        for(int i = 0; i < rhs.length(); i ++)
        {
            if(rhs[i] == lhs[i]) continue;
            else
            {
                for(int j = i + 2; j < rhs.length(); j += 2)
                {
                    if(lhs[j] == rhs[i])
                    {
                        char temp = lhs[j];
                        lhs[j] = lhs[i];
                        lhs[i] = temp;
                        break;
                    }
                }
                if(rhs[i] != lhs[i]) return false;
            }
        }
        return true;
    }
};

int main()
{
    vector<string > v = {"abc","cba"};
    Solution sol;
    cout<<sol.numSpecialEquivGroups(v)<<endl;
    
}