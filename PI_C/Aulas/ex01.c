#include<stdio.h>
/*
1. Faça um programa que receba quatro números inteiros calcule mostre a soma desses números.
*/

int main()
{
    int n1, n2, n3, n4, soma;
    printf("Digite o primeiro valor\n");
    scanf("%d",&n1);
    printf("Digite o segundo valor\n");
    scanf("%d", &n2);
    printf("Digite o terceiro valor\n");
    scanf("%d",&n3);
    printf("Digite o quarto valor\n");
    scanf("%d",&n4);
    soma = n1 + n2 + n3 + n4;
    printf("A soma de %d + %d + %d + %d = %d\n", n1, n2, n3, n4, soma);
    return 0;
}
