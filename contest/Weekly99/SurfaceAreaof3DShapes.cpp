// On a N * N grid, we place some 1 * 1 * 1 cubes.

// Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

// Return the total surface area of the resulting shapes.

 

// Example 1:

// Input: [[2]]
// Output: 10
// Example 2:

// Input: [[1,2],[3,4]]
// Output: 34
// Example 3:

// Input: [[1,0],[0,2]]
// Output: 16
// Example 4:

// Input: [[1,1,1],[1,0,1],[1,1,1]]
// Output: 32
// Example 5:

// Input: [[2,2,2],[2,1,2],[2,2,2]]
// Output: 46
 

// Note:

// 1 <= N <= 50
// 0 <= grid[i][j] <= 50

#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

class Solution {
public:
    int surfaceArea(vector<vector<int>>& grid) {
        int total = 0;
        int overlap = 0;
        int row_size = grid.size();
        int col_size = grid[0].size();
        // 2. find the overlap
        for (int i = 0; i < grid.size(); i ++){
            for(int j = 0; j < grid[i].size(); j ++)
            {
                if(grid[i][j] > 0)
                {
                    int lap = (grid[i][j] - 1) * 2;
                    total += grid[i][j];
                    if(i + 1 < row_size){
                        lap += min(grid[i][j],grid[i+1][j]);
                    }
                    if (i - 1 >= 0)
                    {
                        lap += min(grid[i][j],grid[i-1][j]);
                    }
                    if (j - 1 >= 0)
                    {
                        lap += min(grid[i][j],grid[i][j - 1]);
                    }
                    if (j + 1 < col_size)
                    {
                        lap += min(grid[i][j],grid[i][j + 1]);
                    }
                    overlap += lap;
                }
                
            }
        }
        return total*6 - overlap;
    }
};

int main()
{
    vector< vector<int> > v = {{1,2},{3,4}};
    Solution sol;
    cout<<sol.surfaceArea(v)<<endl;
}
