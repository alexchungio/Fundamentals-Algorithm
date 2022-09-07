# include <iostream>
# include <set>
# include <algorithm>

using namespace std;

int main()
{
    set<string> s_0 {"alex", "tim"};

    // insert
    s_0.insert("bili");
    
    set<string>::iterator iter;
    for(iter=s_0.begin(); iter != s_0.end(); iter++)
    {
        cout << * iter<< endl;
    }

    // travesal-2
    for(auto & s: s_0)
    {
        cout << s << endl;
    }
    
    // find
    set<string>::iterator iter_0 = s_0.find("tim");
    if(iter_0 != s_0.end())
    {
        cout << *iter_0 << endl;
    }

    // erase
    set<string>::iterator iter_1 = s_0.find("tim");
    if(iter_1 != s_0.end())
    {
        s_0.erase(iter_1);
        
    }

    return 0;
}