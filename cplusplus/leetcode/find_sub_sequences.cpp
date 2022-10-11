#include <iostream>
#include <vector>

using namespace std;

class Solution {
private:
    vector<vector<int>> result;
    vector<int> path;
    void backtracking(vector<int>& nums, int start_index)
    {
        // 终止条件
        if(path.size() >= 2)
        {
            if(path[-1] < path[-2])
            {
                return;
            }
            else
            {
                result.push_back(path);
            }
        }
        
        for(int i=start_index; i<nums.size(); i++)
        {   
            // 按层去重（包含重复元素）
            if(i != start_index && nums[i-1] == nums[i])
            {
                continue;
            }
            path.push_back(nums[i]);
            backtracking(nums, i+1);
            path.pop_back();
        }
    }
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        backtracking(nums, 0);
        return result;
    }
};


int main()
{
    vector<int> nums = {4, 6, 7, 7};
    Solution solution = Solution();
    vector<vector<int>> result = solution.findSubsequences(nums);
    return 0;
}