#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

template <typename T>
void swap_two(T & x, T & y)
{
    T tmp = x;
    x = y;
    y = tmp;
}

// overload template
template<typename T>
void swap_tow(T *x, T *y)
{
    T tmp = *x;
    *x = *y;
    *y = tmp;
}

int main()
{
    int a = 1, b = 2;
    float c = 3, d = 4;
    swap_two(a, b);
    swap_two(c, d);
    std::cout << "a = " << a << " b = "<< b << std::endl;
    std::cout << "c = " << c << " d = "<< d << std::endl;

    int *a_p = &a, *b_p = &b;
    float *c_p = &c, *d_p = &d;
    swap_tow(a_p, b_p);
    swap_tow(c_p, d_p);
    std::cout << "a = " << a << " b = "<< b << std::endl;
    std::cout << "c = " << c << " d = "<< d << std::endl;
    
}