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
    printf("MAX_NUM_0 = %d \n", MAX_NUM_0);
    printf("MAX_NUM_1 = %d \n", MAX_NUM_1);

    // get size of int
    printf("int size: %lu byte \n", sizeof(int));

    // get float info
    printf("float size : %lu \n", sizeof(float));
    printf("float min value: %u\n", FLT_MIN );
    printf("float max value: %u\n", FLT_MAX );
    printf("precise value: %d\n", FLT_DIG );
    
    return 0;
}

