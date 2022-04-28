#include <iostream>
#include "class_template.h"

using namespace std;
int main()
{
    Pair<string, int> alex("alex", 28);
    Pair<string, int> graham("graham", 26);
    
    std::cout << (alex < graham) << std::endl;
    
    return 0;
}
