/*****************************************************************
 * Name: array.cpp                                               *
 * Function:                                                     *
 * Author: Alex Chung                                            *
 * Time: 2020/7/21 PM 20:04                                      *
 * **************************************************************/

#include <stdio.h>

void show_one_pointer(int * a,  int size);

void show_one_array(int a [], int size);

void show_two_pointer(int * a,  int row_size, int col_size);


int main(void){
    
    // initial array
    int a_0[5] = {1, 2, 3, 4, 5};
    int a_1 [] = {5, 4, 3, 2, 1};
    int a_2 [5] = {1, 2, 3};
    // int a_3 [10] = {[1]=2, [3]=4, [4]=5}; C99
    // show a_0
    int size_0= sizeof(a_0) / sizeof(a_0[0]);
    show_one_pointer(a_0, size_0);
    int size_1 = sizeof(a_1) / sizeof(a_1[0]);
    show_one_array(a_1, size_1);

    // multi dimension array
    int b_0[2][3] = {1, 2, 3, 4, 5, 6};
    int b_1[][3] = {6, 5, 4, 3, 2, 1};
    
    //int raw_size_0 = sizeof(b_0) / sizeof(b_0[][0]);
    //int col_size_0 = sizeof(b_0) / sizeof(b_0[0][]);

    show_two_pointer(&b_0[0][0], 2, 3);
}


void show_one_pointer(int * a, int size){

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

    for (int i=0; i<row; i++ ){
        for (int j=0; j<col; j++){
            int * address = a + i*row + j;
            printf("%d ", * address);
        }
        printf("\n");   
    }
    
}

//void show_two_array(int a [], int row_size, int col_size){}