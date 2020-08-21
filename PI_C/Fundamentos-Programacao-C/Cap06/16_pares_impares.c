#include<stdio.h>
#define LENGTH1 10
#define LENGTH2 5

int VET1[LENGTH1], VET2[LENGTH2];
int SUMPAR[LENGTH1], SUMIMPAR[LENGTH1];
int posicao1 = 0;
int posicao2 = 0;
int soma;

/*
    Faça um programa que preencha um vetor com dez números inteiros e um segundo
    vetor com cinco número inteiro. Calcule e mostre dois vetores resultantes.
    O primeiro vetor resultante será  composto pelos números pares, gerados pelo
    elemento do primeiro vetor somado a todos elementos do segundo vetor; o segundo
    será composto pelos números ímpares gerados pelo elemento do primeiro vetor somado
    a todos os elementos do segundo vetor.
*/

int main(void){
    printf("**Primeiro vetor**\n");
    for (int i = 0; i < LENGTH1; i++)
    {
        scanf("%d",&VET1[i]);
    }

    printf("\n**Segundo vetor**\n");
    for (int i = 0; i < LENGTH2; i++)
    {
        scanf("%d",&VET2[i]);
    }

    // Armazena os pares somados com todos os elementos do segundo vetor.
    for (int i = 0; i < LENGTH1; i++){
        soma = VET1[i];
        for (int j = 0; j < LENGTH2; j++){
            soma += VET2[j];
        }

        if (VET1[i]%2 == 0){ // Se for par;
            SUMPAR[posicao1]=soma;
            posicao1++;
        }else{
            SUMIMPAR[posicao2]=soma;
            posicao2++;
        }
    }

    printf("\n\n**Vetor SUMPAR**\n");
    for (int i = 0; i < posicao1; i++){
        printf("%d|",SUMPAR[i]);
    }

    printf("\nVetor ÍMPAR**\n");
    for (int i = 0; i < posicao2; i++){
        printf("%d|",SUMIMPAR[i]);
    }
    printf("\n");
        
}