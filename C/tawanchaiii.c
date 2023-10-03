// Simply method but don't have anyone do it.
#include <stdio.h>
#include <string.h>

void changeCoffeetoCode(char* str){
    str[2] = 'd';
    str[3] = 'e';
    str[4] = '\0'; 
    printf("%s\n", str); 
}


int main() {
    char str[] = "Coffee";
    changeCoffeetoCode(str);
    return 0;
}

