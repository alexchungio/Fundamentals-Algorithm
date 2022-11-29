#include <iostream>
#include <memory>

/*
unique_ptr
shared_ptr
*/

int main()
{

    // create and initial
    std::unique_ptr<int> m(new int(5));
    std::cout << *m << std::endl;

    
    std::unique_ptr<int> m_0(nullptr); //create
    m_0.reset(new int(7));  // assign
    std::cout << *m_0 << std::endl;

    // create arrray unique_ptr
    std::unique_ptr<int []> m_1(new int[5]{1, 3, 5, 7, 9});
    std::cout << m_1[0] << " |" << m_1[4] << std::endl;

    // make unique (c++ 14)
    std::unique_ptr<int> m_2 = std::make_unique<int>(0);

    // unique_ptr don't soupport copy
    // move: m will been release
    std::unique_ptr<int> n(std::move(m));
    assert(m==nullptr);
    std::cout << *n << std::endl;

    
    return 0;
}