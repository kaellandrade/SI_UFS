#include<stdio.h>
#define LENGTH 3

/*
Faça um programa que preencha um vetor com dez números inteiros, 
calcule e mostre o vetor resultante de uma ordenação decrescente.
*/
int vet[LENGTH];
int auxiliar;

int main(void){
    //Ler os valores
    for (int i = 0; i < LENGTH; i++)
    {
        printf("%dº valor: \n",i+1);
        scanf("%d",&vet[i]);
    }

    // Ordena
    for (int i = 0; i < LENGTH; i++){
        for (int j = 0; j < LENGTH; j++){
            if(vet[j] < vet[j+1]){
                auxiliar = vet[j];
                vet[j] = vet[j+1];
                vet[j+1] = auxiliar;
            }
        }
        
    }
    
    for (int i = 0; i < LENGTH; i++)
        {
            printf("%d| ",vet[i]);
        }
    printf("\n");
}