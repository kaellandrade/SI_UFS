/*
Faça um programa que mostre o menu de opções a seguir, receba a opção do usuário e os dados neces-
sários para executar cada operação.
Menu de opções:
1. Somar dois números.
2. Raiz quadrada de um número.
Digite a opção desejada:


*/
#include<stdlib.h>
#include<stdio.h>
#include<math.h>

int main(void){
    
    float a,b ;
    int resposta;
    printf("Menu de opções:\n");
    printf("1. Somar dois números.\n");
    printf("2. Raiz quadrada de um número.\n");
    printf("Digite a opção desejada:\n");
    scanf("%d", &resposta);
    
    if (resposta == 1)
    {
        printf("Valor de A e B respectivamente: \n");
        scanf("%f %f", &a, &b);

        printf("%.2f + %.2f = %.2f\n", a,b, a+b );
    } else if(resposta == 2)
    {
        printf("Valor de A: \n");
        scanf("%f", &a);

        printf("Raiz de %.2f = %.2f\n", a, pow(a,0.5));

        
    }else
    {
        printf("Opção inválida!\n");
    }

    printf("\n");
    
        // printf("Raiz de %.2f = %f\n", a, pow(a,0.5));
    
    return 0;
}