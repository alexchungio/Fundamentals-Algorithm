/*****************************************************************
 * Name: linked_list.cpp                                         *
 * Function:                                                     *
 * Author: Alex Chung                                            *
 * Time: 2020/8/19 PM 19:10                                      *
 * **************************************************************/

#include <stdio.h>
#include <stdlib.h>

struct node {
    int value;
    struct node * next;
};

node * create_node(int v);

int main(int argc, char*argv[]){
    
    node * head = create_node(1);
    head->next = create_node(2);
    return 0;
    
    
}

node * create_node(int v){
    node * new_node = NULL;
    if ((new_node = (node *)malloc(sizeof(node)))==NULL){
        printf("--No space left--");
    }
    // method 1
    // (*new_node).value = v
    // method 2(recommand)
    new_node->value = v;
    return new_node;
}