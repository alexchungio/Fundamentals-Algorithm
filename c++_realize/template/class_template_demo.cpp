#include <iostream>
#include "class_template.hpp"

using namespace std;

int main()
{
    Pair<string, int> graham("graham", 26);
    Pair<string, int> alex("alex", 28);
    std::cout << boolalpha << (graham < alex) << std::endl;
    
    return 0;
}
