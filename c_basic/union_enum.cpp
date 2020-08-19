/*****************************************************************
 * Name: union_enum.cpp                                               *
 * Function:                                                     *
 * Author: Alex Chung                                            *
 * Time: 2020/7/23 PM 17:04                                      *
 * **************************************************************/

#include <stdio.h>
#include <string.h>

#define TITLE_LEN 20
#define AUTHOR_LEN 20
#define LOGO_LEN 20

union menu {
    int book;
    int fruit;
    int vegetables;
};

union items {
    struct {
        char title[TITLE_LEN + 1];
        char anthor[AUTHOR_LEN + 1];
        int num_page;
    }book;

    struct {
        char logo[LOGO_LEN + 1];
        float price;  
    }mug;
    
    struct{
        char logo[LOGO_LEN + 1];
        char size;
    }shirt;
    
};


typedef enum {ANNIMAL, HUMAN, FRUITS, PLANTS} KINDS;

menu fruit = {.fruit=10};
menu book = {.book=5};

items mugs;


int main(void){

    printf("number fruit = %d\n", fruit.fruit);
    printf("number book = %d\n", book.book);
    printf("book num_page=%d\n", mugs.mug.price);
    
    // printf("%f", 2.0f);
    // enum
    printf("FRUIT = %d", FRUITS);
}
