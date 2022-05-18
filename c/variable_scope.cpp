/*****************************************************************
 * Name: variable_scope.cpp                                             *
 * Function: global varriable and local variable test            *
 * Author: Alexchung                                             *
 * Time: 2020/7/7 AM 10:12                                       *
 * **************************************************************/
#include <stdio.h>

// global variable
int hour=10, minite=13;

void show_time(void){
    printf("Now time: 2020-07-07 %d:%d\n", hour, minite);   
}

int add_range_non_initialize(int a, int b){
    int i, sum;
    // if do not initialize, the local variable will will random initialize
    for(i=a; i<b; i++){
        sum += i;
    }
    return sum;
}

int add_range(int a, int b){
    // initialize local variable 
    int i, sum=0;
    
    for(i=a; i<b; i++){
        sum += i;
    }
    return sum;
}

int main(){
    //local variable
    int hour=10, minite=20;

    show_time(); // Now time: 2020-07-07 10:13
    printf("Now time: 2020-07-07 %d:%d\n", hour, minite); //Now time: 2020-07-07 10:20

    printf("The number of sum range %d and %d is %d\n", 1, 5, add_range_non_initialize(1, 5)); // The number of sum range 1 and 5 is 72

    printf("The number of sum range %d and %d is %d\n", 1, 5, add_range(1, 5)); // The number of sum range 1 and 5 is 10
    return 0;
}