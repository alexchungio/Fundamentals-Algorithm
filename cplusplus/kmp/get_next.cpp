#include <iostream>
#include <string>

using namespace std;

void get_next(int * next, const string s)
{
    // i 表示后缀末尾
    // j 表示前缀末尾
    int j = 0;
    next[0] = j;
    for(int i=1; i<s.size(); i++)
    {
        //前后缀不相同的情况
        while(j > 0 && s[i] != s[j])
        {
            j = next[j-1]; // 向前回退
        }
        if(s[i] == s[j])
        {
            j++;
        }

        //前后缀相同的情况
        next[i] = j;
    }
}


int main()
    
{
    // index: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    // m:     [a, b, a, b, a, a, a, b, a, b,  a, a]
    // next:  [0, 0, 1, 2, 3, 1, 1, 2, 3, 4,  5, 6]
    const string m = "ababaaababaa";
    int next[m.size()];
    get_next(next, m);

    for(int i=0; i<m.size(); i++)
    {
        cout << next[i] << endl;
    }
    
    return 0;
}