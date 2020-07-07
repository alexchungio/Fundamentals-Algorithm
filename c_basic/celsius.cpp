/*****************************************************************
 * Name: celsius.cpp                                             *
 * Function: convert a Fahrenheit temperature to Celsius         *
 * Author: Alexchung                                             *
 * Time: 2020/7/7 AM 08:42                                       *
 * **************************************************************/

# include <stdio.h>

#define FREEZING_PT 32.0f
#define SCALE_FACTOR (5.0f / 9.0f)

int main(void){
    float fahrenheit, celsius;
    printf("Please enter Fahrenheit temperature: ");
    scanf("%f", &fahrenheit);
    
    printf("%d", sizeof(FREEZING_PT));
    celsius = (fahrenheit - FREEZING_PT) * SCALE_FACTOR;
    printf("The celsius temparatuer equivalent: %.1f\n", celsius);
    return 0;
}