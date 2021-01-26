#include<stdio.h>
#include<math.h>
#include<stdlib.h>

int main(void){
    
    int i = 1234;
    printf(" i = %d\n", i); // valor variável
    printf("&i = %ld\n", (long int)&i); // posição long int
    printf("&i = %p\n", (void *)&i); // posição hex
    return EXIT_SUCCESS;
}