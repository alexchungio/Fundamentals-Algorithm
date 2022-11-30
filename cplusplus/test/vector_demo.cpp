# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
#include <functional>
#include <numeric>


using namespace std;

template<typename T>
void print(const std::string & prefix, std::vector<T> value)
{
    std::cout << prefix << ": ";
    for(auto v: value)
    {
        std::cout << v << " ";
    }
    std::cout << std::endl;  
}

template<typename T>
std::vector<size_t> argmax_idx(std::vector<T> v)
{
    std::vector<size_t> idx(v.size());
    std::iota(idx.begin(), idx.end(), 0);
    std::sort(idx.begin(), idx.end(), [&v](size_t i, size_t j){return v[i] > v[j];});
    return idx;
}


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

    // sort
    std::vector<int> v_2 = {5, 7, 4, 2, 8, 6, 1, 9, 0, 3};
    print("v_2", v_2);

    // std::sort(v_2.begin(), v_2.end(), [](int a, int b){return a > b;});
    // print("v_2 sorted from high to low", v_2);

    std::vector<size_t> v_3 = argmax_idx(v_2);
    print("sorted idx", v_3);

    

    return 0;
}