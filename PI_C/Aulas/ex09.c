#include<stdlib.h>
#include<stdio.h>
/*
Faça um programa que preencha um vetor com nove números inteiro, calcule e mostre os números primos e suas respectivas posições.
*/
#define LENGTH 9

// Conta quantos divisores o número n tem;
int eprimo(int n){
    int contadiv = 0;
    for ( int i = 1; i <= n; i++)
    {
        // Caso tenha mais de dois divisores não é primo, logo não faz sentido continuar o laço.
        if (contadiv > 2){
            break;
        }        

        if(n%i == 0){
            contadiv ++;
        }
    }
    if(contadiv == 2){
        return 1;
    } else{
        return 0;
    }
}

int main(void){
    int lidos [LENGTH];
    // Add valores digitados ao vetor lidos
    for (int i = 0; i < LENGTH; i++)
    {
        printf("%d Nº: ",i+1);
        scanf("%d", &lidos[i]);
    }

    // Varre o vetor lidos;
    for (int j = 0; j < LENGTH; j++)
    {
        if(eprimo(lidos[j])){
            printf("%d é primo está na posição %d.\n",lidos[j], j);
        }
        
    }
    return 0;
    
}