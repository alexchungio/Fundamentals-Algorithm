# include <iostream>
# include <map>
# include <algorithm>


using namespace std;

int main()
{
    map<int, string> m_0;
    m_0.insert(pair<int, string>(0, "alex"));
    m_0.insert(pair<int, string>(1, "tim"));
    
    // travesal-1
    map<int, string>::iterator iter;
    for(iter=m_0.begin(); iter != m_0.end(); iter++)
    {
        cout << iter -> first << ":" <<iter->second << endl;
    }

    // travesal-2
    for(auto & m: m_0)
    {
        cout << m.first << ":" << m.second << endl;
    }

    // find key
    map<int, string>::iterator iter_0 = m_0.find(1);
    if (iter_0 != m_0.end())
    {
        cout << iter -> first << ":" <<iter->second << endl;
    }

    // erase
    map<int, string>::iterator iter_1 = m_0.find(0);
    if (iter_1 != m_0.end())
    {
        m_0.erase(iter_1);
    }
    
    // std::tie <=> std::map
    bool is_inserted;
    tie(ignore, is_inserted) = m_0.insert(pair<int, string>(2, "mark"));
    if(is_inserted)
    {
        cout << "Value was inserted successfully" << endl;
    }
    
    return 0;
}