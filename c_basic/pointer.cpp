/*****************************************************************
 * Name: pointter.cpp                                       *
 * Function:                                                     *
 * Author: Alex Chung                                            *
 * Time: 2020/7/23 PM 17:04                                      *
 * **************************************************************/
#include <stdio.h>

// #define

// declaration of external variable

// prototype
void pointer_start();
int find_max_min_a(int *, int, int*, int*);
int find_largest(int *, int);
// int find_max_min_b(int *, int, int*, int*);

int main(){

    pointer_start();
    
    int a[] = {9, 4, 3, 7, 10, 5};
    int n, min_a, max_a;
    n = sizeof(a) / sizeof(a[0]);

    min_a = max_a = a[0];
    find_max_min_a(a, n, &min_a, &max_a);
    printf("min=%d, max=%d\n", min_a, max_a);

    // int * min_b, * max_b;
    // min_b = max_b = a;
    // find_max_min_b(a, n, min_b, max_b);
    // printf("min=%d, max=%d", *min_b, *max_b);
    // get largest value
    printf("largest value=%d\n", find_largest(a, n));
    
    return 0;
}

void pointer_start(){

    int i, j,  *p, *q;

    p = &i;
    *p = 4;
    printf("i=%d, p=%d, *p=%d\n", i, p, *p);
    /// q and p point save variable
    q = p;
    printf("i=%d, p=%d, *p=%d, q=%d, *q=%d\n", i, p, *p, q, *q);
    *p = 5;
    printf("i=%d, p=%d, *p=%d, q=%d, *q=%d\n", i, p, *p, q, *q);

    q = &j;
    *q = 6;
    // point different variable
    printf("i=%d, p=%d, *p=%d, q=%d, *q=%d\n", i, p, *p, q, *q);
    // change the variable value of q pointer with p pointer
    *q = *p;
    printf("i=%d, p=%d, *p=%d, q=%d, *q=%d\n", i, p, *p, q, *q);
    
}


int find_max_min_a(int* a, int n,  int* min, int* max){

    for(int i=0; i<n; i++){
        if (*(a+i) < * min){   
            * min = *(a+i);
        }
        else if (*(a+i) > * max){
            * max = *(a+i);
        }
        
    }   
}

// int find_max_min_b(int* a, int n,  int* min, int* max){

//     for(int i=0; i<n; i++){
//         if (*(a+i) < * min){
//             min = a+i;
//         }
//         else if (*(a+i) > * max){
//             max = a+i;
//         }
        
//     }   
// }

int find_largest(int* a, int n){
    int * largest = a;
    for (int i=0; i<n; i++){
        if (*(a+i)> * largest){
            largest = a + i;
        }
    }
    return *largest;
}