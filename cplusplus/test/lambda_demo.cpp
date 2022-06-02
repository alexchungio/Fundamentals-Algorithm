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
    std::vector<int> v = {3, 1, 4, 5, 2, 0};
    print_vector(v);
    return 0;
}