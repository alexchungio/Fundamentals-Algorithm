# include<iostream>
# include<vector>


using namespace std;

int maxValue(vector<int>&, vector<int>&, int);

int maxValue(vector<int>& weight, vector<int>& value, int bag_weight)
{
    vector<vector<int>> dp(weight.size(), vector<int>(bag_weight + 1, 0));
    for(int j=weight[0]; j<=bag_weight; j++) dp[0][j] = value[0];
    for(int i=1; i<weight.size(); i++)
    {
        for(int j=0; j<= bag_weight; j++)
        {
            if(j < weight[i]) 
            {
                dp[i][j] = dp[i-1][j];
            }
            else 
            {
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i]);
            }   
        }
    }

    return dp[weight.size()-1][bag_weight];
}

int main()
{
    vector<int> weight = {1, 3, 4};
    vector<int> value = {15, 20, 30}; 
    int bag_weight = 4;
    int max_value = maxValue(weight, value, bag_weight);
    cout << max_value << endl;
    return 0;
}