/*****************************************************************
 * Name: exprision.cpp                                           *
 * Function: convert a Fahrenheit temperature to Celsius         *
 * Author: Alex Chung                                            *
 * Time: 2020/7/28 PM 14:46                                      *
 * **************************************************************/

#include <stdio.h>

enum demo_type {RECTANGULAR = 1, POLAR=2};

struct demo_struct{
    int x = 0;
    int y = 0;
} m, n;

struct enum_struct{
    int type=RECTANGULAR;
    int x = 0;
    int y = 0;
} s, t;

demo_struct add_struct(demo_struct, demo_struct);


int main(){
   
    m.x = 1;
    m.y = 2;
    n.x = 3;
    n.y = 4;
    printf("x=%d y=%d\n", m.x, m.y);
    printf("x=%d y=%d\n", n.x, n.y);
    demo_struct z;
    z = add_struct(m, n);
    printf("x=%d y=%d\n", z.x, z.y);
      
}

demo_struct add_struct(demo_struct a, demo_struct b){
    struct demo_struct z;
    z.x = a.x + b.x;
    z.y = a.y + b.y;
    
    return z; 
}
