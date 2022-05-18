#include <iostream>
#include <string>

using namespace std;


struct Corporation
{
    string name = "meitu";
    string location = "xiamen";
    int    num_stuff = 2000;

    // initial member list
    Corporation() {};
    Corporation(string n, string l, int stuff):
                name(n),
                location(l),
                num_stuff(stuff) {};
};


int main()
{   
    Corporation meitu;
    std::cout << meitu.name << " | " << meitu.location << " | " << meitu.num_stuff << std::endl;
    Corporation baidu("baidu", "beijing", 50000);
    std::cout << baidu.name << " | " << baidu.location << " | " << baidu.num_stuff << std::endl;
    
    return 0;
}