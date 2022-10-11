#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>

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
            result.push_back(path);
        }
        unordered_set<int> uset;
        for(int i=start_index; i<nums.size(); i++)
        {   
            
            if(uset.find(nums[i]) != uset.end()  || // 按层去重（包含重复元素）
            (!path.empty() && nums[i] < path.back())) // 移除非递增元素
            {
                continue;
            }
            uset.insert(nums[i]);
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