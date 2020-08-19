/*****************************************************************
 * Name: malloc.cpp                                           *
 * Function:         *
 * Author: Alex Chung                                            *
 * Time: 2020/8/19 PM 19:10                                      *
 * **************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM 10
#define LEN 20
#define NUM_STRING 4

/*
malloc 分配内存块，不对内存块初始化
calloc 分配内存块， 并执行初始化（内存块清零）
realloc 调整之前分配的内存块大小
*/

int main(){
    char *p = NULL;
    if ((p = (char *) malloc(LEN + 1)) == NULL){
        printf("--No space Left---\n");
        exit(EXIT_FAILURE);
    }   
    strcpy(p, "hello world");
    printf("%s\n", p);
    free(p);

    // copy str array
    char * s_0[NUM_STRING] = {"hello", "good", "2020", "0819"};
    char * s_1[NUM_STRING];
    for(int i=0; i < NUM_STRING; i++){
        if ((s_1[i] = (char *)malloc(strlen(s_0[i])+1)) == NULL){
            printf("--No space left--\n");
        }
        strcpy(s_1[i], s_0[i]);
    }
    // traversal and free sape
    for(int i=0; i<NUM_STRING; i++){
        printf("%s \n", s_1[i]);
        free(s_1[i]);
    }

    int * i_0 = NULL;
    printf("%d", sizeof(i_0));
    if ((i_0 = (int *)malloc(NUM*sizeof(int))) == NULL){
            printf("--No space left--\n");
        }
    return 0;
    
}

