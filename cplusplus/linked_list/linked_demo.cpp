#include <iostream>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(nullptr) {}
};

int main()
{
    ListNode * head = new ListNode(1);
    cout << head -> val << endl;
    cout << head -> val << endl;
    
    return 0;
}