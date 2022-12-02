#include <iostream>
#include <memory>
#include <vector>

/*
unique_ptr
shared_ptr
weak_ptr
*/

void unique_ptr_demo()
{
    // create and initial
    std::unique_ptr<int> m(new int(5));
    std::cout << *m << std::endl;

    // create then assign
    std::unique_ptr<int> m_0(nullptr); 
    m_0.reset(new int(7));  
    std::cout << *m_0 << std::endl;

    // create arrray unique_ptr
    std::unique_ptr<int []> m_1(new int[5]{1, 3, 5, 7, 9});
    std::cout << m_1[0] << " |" << m_1[4] << std::endl;

    // move: unique_ptr don't soupport copy
    // explicit transfer ownership
    std::unique_ptr<int> m_2(std::move(m));
    assert(m==nullptr);
    std::cout << *m_2 << std::endl;  
    
    // make_unique
    // std::unique_ptr<int> v_1 = std::make_unique<int>(3);
    auto v_1 = std::make_unique<int>(3);
    std::cout << * v_1.get() << std::endl;

    // array
    auto v_2 = std::make_unique<int []>(5);
    std::cout << v_2.get()[0] << std::endl;  
    
    // vector-1d
    auto v_3 = std::make_unique<std::vector<int>>(5, 2);
    std::cout << v_3.get()->data()[0] << std::endl;

    // vector-2d
    auto v_4 = std::make_unique<std::vector<std::vector<int>>>(3, std::vector<int>(4, 3));
    std::cout << v_4.get()->data()[0][0] << std::endl;

    std::cout << "********************"<< std::endl;
}

void shared_ptr_demo()
{
    std::shared_ptr<int> v_0(new int(3));
    std::cout << "v_0: " << *v_0 << " reference count: " << v_0.use_count()<< std::endl;

    // copy
    std::shared_ptr<int> v_1 = v_0;
    std::cout << "v_1: " << *v_0 << " reference count: " << v_0.use_count() << std::endl;
    assert(v_0 == v_1);

    // release
    v_1.reset();
    std::cout << "v_1: " << " reference count: " << v_0.use_count() << std::endl;

    // reset
    v_0.reset();
    std::cout << "v_0: " << " reference count: " << v_0.use_count() << std::endl;
    
    std::cout << "********************"<< std::endl;

}

void weak_ptr_demo()
{
    auto v_0 = std::make_shared<int>(2);
    std::cout << "v_0: " << *v_0 << " reference count: " << v_0.use_count() << std::endl;

    // weak_ptr -> shared_ptr
    // don't affact the resource reference count
    auto v_1 = std::weak_ptr<int>();
    v_1 = v_0;
    std::cout << "v_1: " << " reference count: " << v_0.use_count() << std::endl;

    // in order to get object must convert to shared_ptr
    // with lock to get shred_ptr
    std::shared_ptr<int> v_2 = v_1.lock();
    std::cout << "v_2: " << *v_2 << " reference count: " << v_0.use_count() << std::endl;
    
    std::cout << "********************"<< std::endl;
}

void convert_smart_pointer_demo()
{
    // convert to smart pointer
    int v_0[5] = {0, 1, 2, 3, 4};
    std::unique_ptr<int> p_0(v_0);
    std::cout << "p_0: " << p_0.get()[0] << std::endl;

    std::unique_ptr<int> p_1(nullptr);
    p_1.reset(v_0);
    std::cout << "p_1: " << p_1.get()[1] << std::endl;

    auto p_2 = std::make_unique<int>(5);
    p_2.reset(v_0);
    std::cout << "p_1: " << p_1.get()[2] << std::endl;

    // convert from smart pointer
    int * v_2 = p_0.get();
    std::cout << "v_2: " << v_2[0] << std::endl;
    
    std::cout << "********************"<< std::endl;
}


int main()
{ 
    unique_ptr_demo();
    shared_ptr_demo();
    weak_ptr_demo();
    convert_smart_pointer_demo();
    
    return 0;
}