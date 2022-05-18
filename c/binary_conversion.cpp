/*****************************************************************
 * Name: binary_conversion.cpp                                   *
 * Function:                                                     *
 * Author: Alex Chung                                            *
 * Time: 2020/08/07 AM 10:36                                     *
 * **************************************************************/

#include <stdio.h>
#include <stdlib.h>

# define LEN 20

int convert_char_to_digit(char); // only support '0'~'9'
char convert_digit_to_char(int); // only support 0~9
char digit_to_hex_char(int); // only support 0~15
int hex_char_to_digit(char); // only support '0'~'9' 'A'~'F'
 
void convert_int_to_str(int n, char *);
int convert_str_to_int(char *);

int decimal_num = 12;
int octal_num = 014;
int hex_num = 0xc;

int main(int argc, char* argv[]){
    // decimal
    printf("decimal value %d equal octal value = %o", decimal_num, decimal_num);  // octal
    printf("decimal value %d equal hexadecimal value = %x\n", decimal_num, decimal_num); //hexadecimal

    // octimal
    printf("octal value %o equal decimal value = %d\n", octal_num, octal_num);  // decimal
    printf("octal value %o octal equal hex value = %x\n", octal_num, octal_num);  // hex

    // hexadecimal
    printf("hex value %o equal octal value = %d\n", hex_num, hex_num);  // octal
    printf("hex value %o equal decimal value = %x\n", hex_num, hex_num);  // decimal

    // convert int to str
    // use stdlib.h
    char s_octal[LEN + 1];
    char s_decimal[LEN + 1];
    char s_hex[LEN + 1];
    itoa(decimal_num, s_octal, 8);
    printf("convert int to octal str: %s\n", s_octal);
    itoa(decimal_num, s_decimal, 10);
    printf("convert int to decimal str: %s\n", s_decimal);
    itoa(decimal_num, s_hex, 16);
    printf("convert int to hex str: %s\n", s_hex);

    
    // convert str to int
    // use stdlib.h
    // char const * str_decimal = "12";
    //char str_decimal [] = "12";

    char * str_decimal = (char *)"12";
    int str_decimal_num, c, n;
    str_decimal_num = atoi(str_decimal);
    printf("convert decimal str to decimal int: %d\n", str_decimal_num);

    // convert char to int
    c = '6';
    printf("convert char %c to digit = %d\n", c, convert_char_to_digit(c));
    // convert char to int
    n = 6;
    printf("convert int  %d to digit = %c\n", n, convert_digit_to_char(n));
    
    n = 10;
    printf("convert int  %d to hex = %c\n", n, digit_to_hex_char(n));
    c = 'A';
    printf("convert char %c to digit = %d\n", c, hex_char_to_digit(c));

    return 0;

}


int convert_char_to_digit(char c){

    int num = c - '0';

    return num;
}


char convert_digit_to_char(int n){

    char c = '0' + n;

    return c;
}

char digit_to_hex_char(int n){
    char const * hex_str = "0123156789ABCDEF"; 
    return hex_str[n];
}

int hex_char_to_digit(char c){
    
    int n;
    if (c >='0' && c<='9'){
        n = c - '0';
    }else if(c>='A' && c<='F'){
        n = c - 'A' + 10;
    }else{
        exit(EXIT_FAILURE);
    }
    return n;
} 