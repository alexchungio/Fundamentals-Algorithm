#include <iostream>
#include <string>



int main()
{
    int i_0 = 123;
    std::string s_0 = std::to_string(i_0);
    int i_1 = std::stoi(s_0);
    std::cout << typeid(i_0).name() << i_0 << std::endl;
    std::cout << typeid(s_0).name() << s_0 << std::endl;
    std::cout << typeid(i_1).name() << i_1 << std::endl;
    return 0;
}