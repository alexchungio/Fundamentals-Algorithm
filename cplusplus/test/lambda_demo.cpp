#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
/*
lambda:
[capture](parameter) specifiers exception attr -> return type
{
    definition of method
}
[capture]: 代表捕获列表， 捕获 lambda 所在函数的局部变量。 捕获类型可以分为值捕获，引用捕获，隐式捕获。
(parameter): 代表参数列表， 其中括号内为形参
specifiers exception attr: 代表附加说明符， 一般为 mutable, noexcept 等。
return type： 代表 lambda 的返回类型
{}: d代表函数主体
*/
using namespace std;

void print_vector(std::vector<int> v)
{
    std::for_each(v.begin(), v.end(), [](int i)
    {
        std::cout << i << " ";
        
    });
    std::cout << std::endl;
}

int main()
{
    std::vector<int> v = {3, 1, 4, 5, 2, 0, 1, 2, 3};
    print_vector(v);

    // non-increasing sort
    sort(v.begin(), v.end(), [](const int &a, const int &b) -> bool
    {
        return a > b;
    });
    print_vector(v);
    
    // remove duplicate element
    std::vector<int>::iterator p;
    p = unique(v.begin(), v.end(), [](int a, int b)
    {
        return a == b;
    });
    // resize the vector so as to remove the undefined terms
    v.resize(distance(v.begin(), p));
    print_vector(v);

    /*
    [&] : capture all external variable by reference 
    [=] : capture all external variable by value 
    [a, &b] : capture a by value and b by reference
    */

    std::vector<int> v_1 = {3, 1, 5};
    std::vector<int> v_2 = {7, 9, 12, 4};
    
    auto push_into = [&](int m)
    {
        v_1.push_back(m);
        v_2.push_back(m);
    };
    push_into(6);
    print_vector(v_1);
    print_vector(v_2);

    const int N = 4;
    int count_greater_n = count_if(v_2.begin(), v_2.end(), [=](int a)
    {
        return a>N;
    });
    std::cout << count_greater_n << std::endl;



    return 0;
}