/*****************************************************************
 * Name: test.cpp                                               *
 * Function:                                                     *
 * Author: Alex Chung                                            *
 * Time: 2020/7/10 PM 20:04                                      *
 * **************************************************************/
#include <stdio.h>

void pretty_print(int *start, int row, int col){
    for (int i = 0; i < row; ++i) {
    for (int j = 0; j < col; ++j) {
        int *address = start + i * col + j; //手动计算地址
        printf("%d ", *address);
   }
   printf("\n");
}
return;
}

int main(int argc, const char **argv){
    int a[3][2] = {{1, 2}, {3, 4}, {5, 6}};
    pretty_print((&a[0][0]), 3, 2);

    return 0;
}