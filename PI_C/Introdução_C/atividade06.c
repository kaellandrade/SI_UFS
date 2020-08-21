/*
6) Dados três números, imprimi-los em ordem crescente.
 */
#include<stdlib.h>
#include<stdio.h>

int a, b, c;

int main(void){
    printf("Digite A:\n");
    scanf("%d",&a);
    printf("Digite B:\n");
    scanf("%d",&b);
    printf("Digite C:\n");
    scanf("%d",&c);
    if( a <= c && c <= b){
        printf("%d %d %d\n",a,c,b);

    }else if (a<=b && b<=c){
        printf("%d %d %d\n",a,b,c);

    }else if(b <= a && a <= c){
        printf("%d %d %d\n",b,a,c);

    } else if(b <= c && c <= a){
        printf("%d %d %d\n",b,c,a);

    } else if(c <= a && a <= b){
        printf("%d %d %d\n",c,a,b);

    }else{
        printf("%d %d %d\n", c,b,a);
    }
}