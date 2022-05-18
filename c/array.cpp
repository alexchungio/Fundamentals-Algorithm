/*****************************************************************
 * Name: array.cpp                                               *
 * Function:                                                     *
 * Author: Alex Chung                                            *
 * Time: 2020/7/21 PM 20:04                                      *
 * **************************************************************/

#include <stdio.h>
#include <assert.h>

#define ROW_LEN 2
#define COL_LEN 3

//void show_one_pointer(int * a,  int size);
void show_one_pointer(int * ,  int );
//void show_one_array(int a [], int size);
void show_one_array(int [], int ); // omit parameter name in typeproto

//void show_two_pointer(int * a,  int row_size, int col_size);
void show_two_pointer(int * ,  int , int );//
//void show_tow_array(int a[][COL_LEN], int row);
void show_tow_array(int [][COL_LEN], int); // omit parameter name in typeproto


int main(void){
    
    // initial array
    int a_0[5] = {1, 2, 3, 4, 5};
    int a_1 [] = {5, 4, 3, 2, 1};
    int a_2 [5] = {1, 2, 3};
    // int a_3 [10] = {[1]=2, [3]=4, [4]=5}; C99
    // show a_0
     printf("a_0:\n");
    int size_0= sizeof(a_0) / sizeof(a_0[0]);
    show_one_pointer(a_0, size_0);
    // show a_1
     printf("a_1:\n");
    int size_1 = sizeof(a_1) / sizeof(a_1[0]);
    show_one_array(a_1, size_1);

    // multi dimension array
    int b_0[ROW_LEN][COL_LEN] = {1, 2, 3, 4, 5, 6};
    int b_1[][COL_LEN] = {6, 5, 4, 3, 2, 1};
    
    // show b_0
    printf("b_0:\n");
    int raw_size_0 = sizeof(b_0) / sizeof(b_0[0]);
    int col_size_0 = sizeof(b_0[0]) / sizeof(b_0[0][0]);
    show_two_pointer(&b_0[0][0], raw_size_0, col_size_0);
    // show b_1
    printf("b_1:\n");
    show_tow_array(b_1, ROW_LEN);

    return 0;
}


void show_one_pointer(int * a, int size){
    assert(NULL != a);
    for (int i=0; i<size; i++ ){
        printf("%d ", a[i]);
    }
    printf("\n");
}

void show_one_array(int a [], int size){

    for (int i=0; i<size; i++ ){
        printf("%d ", a[i]);
    }
    printf("\n");
}


void show_two_pointer(int * a,  int row, int col){
    assert(NULL != a)
    for (int i=0; i<row; i++ ){
        for (int j=0; j<col; j++){
            int * address = a + i*row + j;
            printf("%d ", * address);
        }
        printf("\n");   
    }

}

void show_tow_array(int a[][COL_LEN], int row){
    for (int i=0; i<row; i++){
        for (int j=0; j<COL_LEN; j++){
            printf("%d ", a[i][j]);
            }
    printf("\n"); 
    }
}

//void show_two_array(int a [], int row_size, int col_size){}