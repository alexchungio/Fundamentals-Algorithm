/*****************************************************************
 * Name: str_test.cpp                                            *
 * Function:                                                     *
 * Author: Alex Chung                                            *
 * Time: 2020/08/07 AM 10:24                                     *
 * **************************************************************/

#include <stdio.h>
#include <string.h>

#define CONTENT_LEN 20

int count_spaces(const char * s);
size_t get_strlen(const char *);
char * concat_str(char *, const char *);
void traversal_str_array(char**, int);

int main(int argc, char *argv[]){

    /* for (int i=0; i< argc; i++){
        printf("%s\n", argv[i]);
    } */
    
    char const * s_1 = "are you ok";
    char s_2[] = "i'm fine thank you";
    
    // print
    printf("%s\n", s_1);
    printf("%s\n", s_2);
    puts(s_1);
    puts(s_2);

    // read
    char contents[CONTENT_LEN + 1];
    printf("Enter you contents: \n");
    // scanf("%s", contents); // that is a question
    // puts(contents); // that

  /*   gets(contents); // that is a question
    puts(contents); // that is a question */

    int num_space;
    num_space = count_spaces(s_1);
    printf("The number space of %s is %\n", s_2, num_space);


    // use string.h lib
    
    const char* s_3 =  "AWSL";
    char s_4[20+1];
    // copy 
    // strcpy(s_4, s_3);  // normal
    strncpy(s_4, s_3, sizeof(s_4)-1); //security
    s_4[sizeof(s_4)-1] = '/0';
    printf("%s size is: %d\n", s_4, strlen(s_4));

    // concat two str
    // strcat(s_4, s_3); //normal
    strncat(s_4, s_3, sizeof(s_4)-sizeof(s_3) - 1); // security
    s_4[sizeof(s_4)] = '\0';
    printf("%s size is: %d\n", s_4, strlen(s_4));
    
    // compare two str
    const char * s_5 = "XSWL";
    // strcmp(const char * str1, const char * str2)
    // str1 < str2 -> -1
    // str1 > str2 -> 1
    // str1 = str2 -> 0
    printf("compare %s and %s: %d\n", s_3, s_5, strcmp(s_3, s_5));
    printf("compare %s and %s: %d\n", s_3, s_4, strcmp(s_3, s_4));
    printf("compare the front %d of %s and %s : %d\n", 3, s_3, s_4, strncmp(s_3, s_4, 3));
    printf("compare the front %d of %s and %s : %d\n", 6, s_3, s_4, strncmp(s_3, s_4, 6));

    // get str length
    printf("lenght of %s is %d\n", s_4, get_strlen(s_4));
    
    printf("concat result of %s and %s is ", s_4, s_5);
    printf("%s\n", concat_str(s_4, s_5));

    // str array
    char * menu[] = {"alex", "graham", "tomas", "kobe"};
    traversal_str_array(menu, 4);
    
    return 0;
}

int count_spaces(const char *s){
    
    int num_space = 0;
    for (; *s != '\0'; s++){
        if (*s == ' '){
            num_space += 1;
        }
    }
    return num_space;
}

size_t get_strlen(const char *s){
    const char * p =  s;
    while(*s){
        s++;
    }
    return s - p;
}


char * concat_str(char* s1, const char* s2){
    char * p = s1; // handle head of s1
    // move to end of s1
    while(*p){
        p++;
    }
    while(*p++ = *s2++);

    return s1;
}


void traversal_str_array(char ** s, int capacity){
    
    for (int i=0; i<capacity; i++){
        printf("%s\n", *(s+i));
    }
}






