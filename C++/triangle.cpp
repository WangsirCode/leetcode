// Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

// For example, given the following triangle

// [
//      [2],
//     [3,4],
//    [6,5,7],
//   [4,1,8,3]
// ]
// The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

// Note:

// Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
class Solution {
public:
    int minimumTotal(vector< vector<int> >& triangle) {
        if(triangle.empty() or triangle[0].empty())
        {
            return 0;
        }
        vector<int> mini;
        mini.push_back(triangle[0][0]);
        for(int i = 1; i < triangle.size(); i ++)
        {
            vector<int> row = triangle[i];
            mini.push_back(mini.back() + row.back());
            for (int j = i - 1; j > 0; --j)
            {
                mini[j] = row[j] + min(mini[j], mini[j-1]);
            }
            mini[0] = row[0] + mini[0];
        }
        vector<int>::iterator min = min_element(mini.begin(), mini.end());
        return *min;

    }
};
int main()
{
     vector< vector<int> > v;
     vector<int> i;
     i.push_back(-1);
     v.push_back(i);
    
     i.clear();
     i.push_back(2);
     i.push_back(3);
     v.push_back(i);

     i.clear();
     i.push_back(1);
     i.push_back(-1);
     i.push_back(-3);
     v.push_back(i);

     Solution s;
     cout << s.minimumTotal(v) << endl;;
    
     v.clear();
     i.clear();
     i.push_back(-1);
     v.push_back(i);
    
     i.clear();
     i.push_back(3);
     i.push_back(2);
     v.push_back(i);

     i.clear();
     i.push_back(-3);
     i.push_back(1);
     i.push_back(-1);
     v.push_back(i);
     cout << s.minimumTotal(v) << endl;;
    return 0;
}
