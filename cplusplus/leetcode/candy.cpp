#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    // 前序遍历 + 后序遍历
    int candy(vector<int>& ratings) {
        if(ratings.size() == 1) return 1;
        int result = 0;
        vector<int> candy_val(ratings.size(), 1);
        // 前序遍历
        for(int i=1; i<ratings.size(); i++)
        {
            if(ratings[i] > ratings[i-1])
            {
                candy_val[i] = candy_val[i-1] + 1;
            }
        }
        // 后序遍历
        for(int j=ratings.size()-2; j>0; j--)
        {
            if(ratings[j] > ratings[j+1])
            {
                candy_val[j] = max(candy_val[j+1] + 1, candy_val[j]);
            }
        }
        // 累加个数
        for(int k=0; k<candy_val.size(); k++)
        {
            result += candy_val[k];
        }
        return result;
    }
    // brute force
    int candy_bf(vector<int>& ratings) {
        vector<int> candy_val(ratings.size(), 1);
        int sum_candy = 0; // 
        int cur_max = 0; // 记录当前最大评分对应的索引，保持 cur_max 到当前位置为非严格单调减，便于后值小于前值时，回退更新所有的前值
        for(int i=1; i<ratings.size(); i++)
        {
            // 前评分小于后评分
            if(ratings[i] > ratings[i-1])
            {
                candy_val[i] = candy_val[i-1] + 1; // 更新后值
                cur_max = i; // 更新当前最大值索引，保持单调减
                
            }
            // 前评分大于后评分
            else if(ratings[i] < ratings[i - 1])
            {   // 依次更新最大评分到当前索引的值，保持非严格单调减
                for(int j = i-1 ; j >= cur_max; j--)
                {   
                    // 只有 前值 小于等于 后值+1 才更新后值
                    if(candy_val[j] <= candy_val[j+1])
                    {
                        candy_val[j] += 1;
                    }
                }   
            }
            // 前平分等于后评分
            else
            {
                // 更新最大评分索引
                cur_max = i;
            }
        }

        for(int i=0; i<candy_val.size(); i++)
        {
            sum_candy += candy_val[i];
        }
        return sum_candy;
    }
};

int main()
{
    vector<int> ratings = {1, 0, 2}; // {2, 1, 2}
    Solution solution = Solution();
    int result = solution.candy(ratings);

    return 0;
}