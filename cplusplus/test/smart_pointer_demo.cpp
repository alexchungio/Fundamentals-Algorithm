#include <iostream>
#include <memory>

/*
unique_ptr
shared_ptr
*/

int main()
{

    // create and initial
    std::unique_ptr<float> m(new float(5));
    std::cout << *m << std::endl;

    
    std::unique_ptr<float> m_0(nullptr); //create
    m_0.reset(new float(7));  // assign
    std::cout << *m_0 << std::endl;

    // create arrray unique_ptr
    std::unique_ptr<float[]> m_1(new float[]{1, 3, 5, 7, 9});
    std::cout << m_1[0] << "|" << m_1[4] << std::endl;

    // unique_ptr don't soupport copy
    // move: m will been release
    std::unique_ptr<float> n(std::move(m));
    assert(m==nullptr);
    std::cout << *n << std::endl;
    
    return 0;
}