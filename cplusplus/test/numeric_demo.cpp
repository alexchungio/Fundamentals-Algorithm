#include <iostream>
#include <vector>
#include <numeric>
#include <string>


void accumulate_demo()
{
    std::vector<int> v{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // multiplies tow value => template class
    int multi_0 =  std::multiplies<int>()(2, 4);
    
    // accumulate
    int sum_0 = std::accumulate(v.begin(), v.end(), 0);
    // multiply all value
    int multi_1 = std::accumulate(v.begin(), v.end(), 1, std::multiplies<int>());

    std::cout << "multi_0 value: " <<  multi_0 << std::endl;
    std::cout << "sum value: " <<  sum_0 << std::endl;
    std::cout << "multi_1 value: " <<  multi_1 << std::endl;
    
}

void transform_demo()
{
    std::string s = "alex";
    std::transform(s.begin(), s.end(), 
                   s.begin(), // d_first	-> the beginning of the destination range
                   [](char c){return std::toupper(c);});
    
    std::vector<int> v_1 = {1, 2, 3, 4, 5};
    std::vector<int> v_2 = {2, 2, 6, 8, 10};
    std::vector<int> multi_2(5);
    std::transform(v_1.begin(), v_1.end(), 
                   v_2.begin(), multi_2.begin(), // d_first	-> the beginning of the destination range
                   std::multiplies<int>());    std::cout << "upper string: " <<  s << std::endl;
    for(auto i: multi_2)
    {
        std::cout << " " << i << std::endl;
    }
}

int main()
{
    accumulate_demo();
    transform_demo();
    

    

    return 0;
}