/*****************************************************************
 *
 * Name: linked_list.cpp                                         *
 * Function:                                                     *
 * Description:
 * Version:
 * Modify:   
 * Author: Alex Chung                                            *
 * Time: 2020/8/19 PM 19:10                                  *
 * **************************************************************/

#include <stdio.h>
#include <stdlib.h>


typedef int TYPE;

struct node 
{
    TYPE value;
    struct node * next;
};


node * create_node(TYPE v);  
node * add_to_head(node *, TYPE);
node * add_to_tail(node *, TYPE);
node * delete_from_head(node *);
node * delete_from_tail(node *);
node * search_linked(node*, TYPE);
node * insert_node(node*, int, TYPE);
node * delete_node(node*, int);
void traversal_linked(node *);


int main(int argc, char*argv[])
{
    
    node * head=NULL;
    
    // head = add_to_head(head, 1);
    head = add_to_head(head, 1); 
    traversal_linked(head); // 1
    head = add_to_head(head, 2);
    traversal_linked(head);  // 2 1
    head = insert_node(head, 0, 3);
    traversal_linked(head); // 3 2 1
    head = insert_node(head, 1, 4);
    traversal_linked(head); // 3 4 2 1
    head = insert_node(head, 4, 5);
    traversal_linked(head); // 3 4 2 1 5
    head = delete_node(head, 4);
    traversal_linked(head); // 3 4 2 1 
    head = delete_node(head, 1);
    traversal_linked(head); // 3 2 1
    head = add_to_tail(head, 6);
    traversal_linked(head); // 3 2 1 6
    head = add_to_tail(head, 7);
    traversal_linked(head); // 3 2 1 6 7
    
    node * node_3 = search_linked(head, 3); 
    node * node_5 = search_linked(head, 5); // not fund 5 in linked list

    head = delete_from_head(head); 
    traversal_linked(head); // 2 1 6 7
    head = delete_from_head(head);
    traversal_linked(head); // 1 6 7
    head = delete_from_tail(head);
    traversal_linked(head); // 1 6
    head = delete_from_tail(head);
    traversal_linked(head); // 1
    
    return 0;
}


/***************************************************************
title：create_node
function：
format：node * create_node(TYPE v)
input：v
output：NULL
return：node *
***************************************************************/
node * create_node(TYPE v)
{
    node * new_node ;
    if ((new_node = (node *)malloc(sizeof(node)))==NULL)
    {
        printf("--No space left--");
    }
    // method 1
    // (*new_node).value = v
    // method 2(recommand)
    new_node->value = v;
    new_node->next = NULL; // note the struct pointer initial is invilid, need to reinitial 
    return new_node;
}


/***************************************************************
title：add_to_head
function：add node to linked head
format：node * add_to_head(node * head, TYPE v)
input：linked list head, v
output：NULL
return：node *
***************************************************************/
node * add_to_head(node * head, TYPE v)
{
    node * new_head;
    if ((new_head = (node *)malloc(sizeof(node)))==NULL)
    {
        printf("--Error: malloc failed to add_to_head--");
        exit(EXIT_FAILURE);
    }
    new_head->value = v;
    new_head->next = head;

    return new_head;
}


/***************************************************************
title：add_to_tail
function：add node to linked tail
format：node * add_to_tail(node * head, TYPE v)
input：linked list head, v
output：NULL
return：node *
***************************************************************/
node * add_to_tail(node * head, TYPE v)
{
    
    // traversal to tail
    node * prob = head ;
    while(prob->next != NULL)
    {
        bool a = prob->next != NULL;
        prob = prob->next;
    }
    // crete node 
    node * new_node;
    if ((new_node = (node *)malloc(sizeof(node)))==NULL)
    {
        printf("--Error: malloc failed to add_to_head--");
    }
    new_node->value = v;
    new_node->next = NULL;
    prob->next = new_node;

    return head;
}


/***************************************************************
title：delete_from_head
function：delete node from head
format：node * delete_from_head(node * head)
input：linked list head
output：NULL
return：node *
***************************************************************/
node * delete_from_head(node * head)
{

    node * prob = head;
    if (prob == NULL)
    {
        printf("Error: linked list is None");
    }
    else
    {
        head = head->next;
        free(prob);     
    }
    return head;
}


/***************************************************************
title：delete_from_tail
function：delete node from linked tail
format：node * delete_from_tail(node * head)
input：linked list head
output：NULL
return：node *
***************************************************************/
node * delete_from_tail(node * head)
{
    node * cur = NULL;
    node * prev = NULL;
    if (head == NULL)
    {
        printf("Error: linked list is None");
    }
    else
    {
        for(cur=head, prev; cur->next != NULL;prev=cur,cur=cur->next);
        if(prev == NULL) /*only one node*/
        {  
            head = NULL;
        }
        else
        {
            prev->next = NULL;
        }
        free(cur);
    }
    
    return head;
}


/***************************************************************
title：search_linked
function：search value in linked list
format：node * search_linked(node* head, int v)
input：linked list head, v
output：NULL
return：node *
***************************************************************/
node * search_linked(node* head, int v){
    node * prob = head;
    while( prob != NULL && prob->value !=v)
    {
        prob = prob->next;
    }
    if (prob == NULL)
    {
        printf("not fund %d in linked list\n", v);
        return NULL;
    }
    else
    {
        return prob;
    }
}


/***************************************************************
title：insert_node
function：insert node to linked list 
format：node * insert_node(node* head, int n, TYPE v)
input：linked list head, index n, value v
output：NULL
return：node *
***************************************************************/
node * insert_node(node* head, int n, TYPE v){
    node * cur = head;
    node * prev = NULL;
    /*插入到头节点*/
    node * new_node = NULL;
    if ((new_node = (node *)malloc(sizeof(node)))==NULL)
    {
        printf("--Error: malloc failed to insert_node--");
    }
    
    if (n==0)
    { 
        new_node->value = v;
        new_node->next = head;
        head = new_node;
    }
    else
    {
        while((n-- > 0) && (cur!= NULL))
        {
            prev = cur;
            cur = cur->next;
        }
        if (n>0)
        {
            printf("the index %d out of range", n);
            free(new_node);
            exit(EXIT_FAILURE);
        /*insert tail*/
        }
        else if(cur==NULL)
        {

            new_node->value = v;
            new_node->next = NULL;
            prev->next = new_node;
        /*insert internal*/
        }
        else
        {
           new_node->value = v;
           new_node->next= cur;
           prev->next = new_node; 
        } 
    }

    return head;
}


/***************************************************************
title：delete_node
function：delete node from linked list 
format：node * delete_node(node* head, int n)
input：linked list head, index n
output：NULL
return：node *
***************************************************************/
node * delete_node(node* head, int n)
{
    
    node * cur = head;
    node * prev = NULL;
    if (n==0)
    {
        head = head->next;
        free(cur);
    }
    else
    {
        while((n-->0) && (cur->next!=NULL))
        {
            prev = cur;
            cur = cur->next;
        }
        if(n>0)
        {
            printf("the index %d out of range", n);
            exit(EXIT_FAILURE);
        }
        else
        {
            prev->next = cur->next;
            free(cur);
        }
        
    }
    return head;
}


/***************************************************************
title：traversal_linked
function：traversal and print linked list 
format：void traversal_linked(node * head)
input：linked list head
output：node value
return：NULL
***************************************************************/
void traversal_linked(node * head)
{
    
    node * prob = head;
    while(prob != NULL)
    {
        printf("%d ", prob->value);
        prob = prob->next;
    }
    printf("\n");  
}
