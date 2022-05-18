/*****************************************************************
 * Name: pointer.cpp                                       *
 * Function:                                                     *
 * Author: Alex Chung                                            *
 * Time: 2020/7/23 PM 17:04                                      *
 * **************************************************************/
#include <stdio.h>
#include <assert.h>

// #define

// declaration of external variable

// prototype
void pointer_start();
int find_max_min_a(int *, int, int*, int*);
int find_largest(int *, int);
// int find_max_min_b(int *, int, int*, int*);
int find_row_largest_a(const int * ,  int , int );
int find_row_largest_b(int * ,  int , int );
int find_col_largest_a(const int * ,  int , int );

int max(int, int);

int main(int argc, char *argv[]){

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

    /*tow demension array*/
    int b [2][3] = {2, 4, 3, 6, 1, 7};
    int num_row = sizeof(b) / sizeof(b[0]);
    int num_col = sizeof(b[0]) / sizeof(b[0][0]);
    //get largest of row 
    int dst_row = 0; 
    printf("lagest value of %d row is %d\n", dst_row, find_row_largest_a(b[0], num_col, dst_row));
    printf("lagest value of %d row is %d\n", dst_row, find_row_largest_b(b[0], num_col, dst_row));
    //get largest of col
    int dst_col = 1;
    printf("lagest value of %d col is %d\n", dst_col, find_col_largest_a(b[0], num_row, dst_col));
    //printf("lagest value of %d col is %d\n", dst_col, find_col_largest_b(b[0], num_row, num_col, dst_col));


    /*二维数组指针(数组的数组)*/
    int c [2][3] = {1, 2, 3, 4, 5, 6};
    
    int (*p_1)[3] = c; 
    printf("p[][] equal to (*p)[]:\n");
    for(int i=0; i<2; i++){
        for(int j=0; j<3; j++){
            printf("%d ", *(*(p_1+i)+j));
        }
        printf("\n");
    }

    /*指针的指针与指针数组*/
    printf("*p[] equal to **p\n");
    int p[3] = {1, 2, 3};
    int q[3] = {4, 5, 6};
    int * d[2] = {p, q};
    int **p_2 = d;
    for(int i=0; i<2; i++){
        for(int j=0; j<3; j++){
            printf("%d ", *(*(p_2+i)+j));
        }
        printf("\n");
    }


    /*指向函数的指针*/
    int (*p_max)(int, int) = max;
    printf("max value of %d and %d is %d\n", 8, 20, (*p_max)(8, 20));
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
    assert(NULL != min);
    assert(NULL != max);

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

    assert(NULL != a);
    int * largest = a;
    for (int i=0; i<n; i++){
        if (*(a+i)> * largest){
            largest = a + i;
        }
    }
    return *largest;
}


int find_row_largest_a(const int * a ,  int num_col , int dst_row ){
    assert(NULL != a);
    int v_largest = *(a+ dst_row);
    for (int i=0; i<num_col; i++){
        if (*((a+dst_row)+i)>v_largest){
            v_largest = *((a+dst_row)+i);
        }
    }
    return v_largest;
}

int find_row_largest_b(int* a  ,  int num_col , int dst_row ){

    assert(NULL != a);
    int v_largest = *(a + dst_row);
    int * p=NULL;
    for ( p=a+dst_row*num_col; p<a+(dst_row+1)*num_col; p++){
        if (*p > v_largest){
            v_largest = *p;
        }
    }
    return v_largest;
}


int find_col_largest_a(const int * a ,  int num_row , int dst_col){
    
    assert(NULL != a);
    int v_largest = *(a+ dst_col);
    
    for(int i=0; i<num_row; i++){
        if(*(a+num_row*i+dst_col+1)>v_largest){
            v_largest = *(a+num_row*i+dst_col+1);
        }
    }
    return v_largest;

}


int max(int a, int b){
    
    return a > b ? a : b;
}

