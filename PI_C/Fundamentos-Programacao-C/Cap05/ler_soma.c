/*
 Faça um programa que leia um número não determinado de pares de valores [m,n], todos inteiros e
positivos, um par de cada vez, e que calcule e mostre a soma de todos os números inteiros entre m e n
(inclusive). A digitação de pares terminará quando m for maior ou igual a n.
*/
#include<stdio.h>

int main(void){
    int soma,m,n;
    int flag = 1;

    while (flag){
        printf("Digite o valor Inicial:\n");
        scanf("%d",&m);
        printf("Digite o valor Final:\n");
        scanf("%d",&n);
        if (m<n){
            int soma = 0;
            for (int i = m; i <= n; i++){
                soma+=i;
            }
            printf("Soma de %d até %d = %d\n",m,n,soma);
            
        }else{
            flag = 0;
        }
    }
    
    
    

}