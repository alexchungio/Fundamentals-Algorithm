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
node * add_to_head(node *, int);
node * add_to_tail(node *, int);
node * delete_from_head(node *);
node * delete_from_tail(node *);
node * add_node(node*, int, int);
node * delete_node(node*, int);
node * search_linked(node*, int);


int main(int argc, char*argv[]){
    
    node * head=NULL;
    
    // head = add_to_head(head, 1);
    head = add_to_head(head, 1);
    head = add_to_head(head, 2);
    
    head = add_to_tail(head, 3);
    head = add_to_tail(head, 4);
    
    head = delete_from_head(head);
    head = delete_from_head(head);
    head = delete_from_tail(head);
    head = delete_from_tail(head);
    
    return 0;
}

node * create_node(int v){
    node * new_node ;
    if ((new_node = (node *)malloc(sizeof(node)))==NULL){
        printf("--No space left--");
    }
    // method 1
    // (*new_node).value = v
    // method 2(recommand)
    new_node->value = v;
    // new_node->next = NULL; // note the struct pointer initial is invilid, need to reinitial 
    return new_node;
}

node * add_to_head(node * head, int v){
    node * new_head;
    if ((new_head = (node *)malloc(sizeof(node)))==NULL){
        printf("--Error: malloc failed to add_to_head--");
        exit(EXIT_FAILURE);
    }
    new_head->value = v;
    new_head->next = head;

    return new_head;
}

node * add_to_tail(node * head, int v){
    
    // traversal to tail
    node * prob = head ;
    while(prob->next != NULL){
        bool a = prob->next != NULL;
        prob = prob->next;
    }
    // crete node 
    node * new_node;
    if ((new_node = (node *)malloc(sizeof(node)))==NULL){
        printf("--Error: malloc failed to add_to_head--");
    }
    new_node->value = v;
    new_node->next = NULL;
    prob->next = new_node;

    return head;
}


node * delete_from_head(node * head){

    node * prob = head;
    if (prob == NULL){
        printf("Error: linked list is None");
    }else{
        head = head->next;
        free(prob);     
    }
    return head;
}
    

node * delete_from_tail(node * head){
    node * cur = NULL;
    node * prev = NULL;
    if (head == NULL){
        printf("Error: linked list is None");
    }else{
        for(cur=head, prev; cur->next != NULL;prev=cur,cur=cur->next);
        if(prev == NULL){  /*only one node*/
            head = NULL;
        }else{
            prev->next = NULL;
        }
        free(cur);
    }
    
    return head;
}

