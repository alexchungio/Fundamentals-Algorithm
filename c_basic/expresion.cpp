/*****************************************************************
 * Name: exprision.cpp                                           *
 * Function: convert a Fahrenheit temperature to Celsius         *
 * Author: Alex Chung                                            *
 * Time: 2020/7/12 AM 10:16                                      *
 * **************************************************************/

#include <stdio.h>


int main(){
    
   
    //----------------------- ++ -- ----------------------------------
    // instance 1
    int i = 2, j = 2;
    printf("i++=%d, i=%d\n", i++, i);
    printf("i--=%d, i=%d\n", i--, i);
    
    printf("j++=%d, j=%d\n", ++j, j);
    printf("--=%d, j=%d\n", --j, j);

    // instance 2
    int m=1, n=2,
    k = m++ + ++n;
    // calculation step
    // step 1: n = n + 1 = 2 + 1 = 3
    // step 2: k = m + n = 1 + 3 = 4
    // step 3: m = m + 1 = 1 + 1 = 2
    printf("k=%d, m=%d, n=%d\n", k, m, n);


    //-----------------------compound assignment-----------------------
    // instance 1
    int a=2, b = 2, c = 3, d=4, e=5, f=-2;  
    a *= b += c *= d += e;
    // calculation step
    // step 0: e = 5
    // step 1: d = d + e = 4 + 5 = 9
    // step 2: c = c * d = c * (d + e) = 3 * (4 + 5) = 27
    // step 3: b = b + c = b + c * (d + e) = 2 + 3 * (4 + 5) = 29
    // step 4: a = a * b = a * (b + c * (d + e)) = 2 * (2 + 3 * (4 + 5)) = 58
    printf("a = %d, b = %d, c = %d, d = %d, e = %d\n", a, b, c, d, e); 

     // instance 2
    b = 1, c = 2, d=3, e=5;  
    a = b += c++ - d + --e / -f;
    // calculation step
    // step 0: a = b += (c++) - d + (--e) / (-f)
    // step 1: a = b += (c++) -d + ((--e) / (-f))
    // step 2: a = b + ((c++) -d + ((--e) / (-f))) = 1 + (3 - (5 / 2)) = 5
    printf("a = %d, b = %d, c = %d, d = %d, e = %d, f=%d\n", a, b, c, d, e, f); 

    



    

    return 0;
}
