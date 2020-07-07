#include <stdio.h>
#include <limits.h>
#include <float.h>

// define constant method 1
# ifndef MAX_NUM_0
  # define MAX_NUM_0 10
# endif

int main(){
    // define constant method 2
    const int MAX_NUM_1 = 20;
    printf("MAX_NUM_0 = %d \n", MAX_NUM_0); // MAX_NUM_0 = 10
    printf("MAX_NUM_1 = %d \n", MAX_NUM_1); // MAX_NUM_1 = 20

    // get size of int
    printf("int size: %lu byte \n", sizeof(int)); // int size: 4 byte

    // get float info
    printf("float size : %lu \n", sizeof(float)); // float size : 4
    printf("float min value: %u\n", FLT_MIN ); // float min value: 0
    printf("float max value: %u\n", FLT_MAX ); // float max value: 3758096384
    printf("precise value: %d\n", FLT_DIG ); // precise value: 6

    // compare float or double
    printf("Add f after decimal means to float: %d\n", sizeof(32.0f)); // Add f after decimal means to float: 4
    printf("Only decimal means to double: %d\n", sizeof(32.0)); // Only decimal means to double: 8
    
    return 0;
}

