# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>


using namespace std;

s
int main()
{   
    // 1-dimension array
    vector<int> v_0(2, 3);

    // add
    v_0.push_back(5);
    v_0.push_back(9);
    // delete
    v_0.erase(v_0.begin() + 1);
    // traverse
    for(auto v: v_0)
    {
        cout << v << endl;
    }
    // get min|max value positon
    vector<int>::iterator min_pos = min_element(v_0.begin(), v_0.end());
    vector<int>::iterator max_pos = max_element(v_0.begin(), v_0.end());
    cout << *min_pos << " " << *max_pos << endl;

    // 2-dimension array
    vector<vector<int>> v_1(2, vector<int>(3, 1));
    // traverse-1
    for(int i=0; i<v_1.size(); i++)
    {
        for(int j=0; j<v_1[i].size(); j++)
        cout << v_1[i][j] << endl;
    }
    // traverse-2
    for(auto i: v_1)
    {
        for(auto j: i)
        {
            cout << j << endl;
        }
    }
    return 0;
}