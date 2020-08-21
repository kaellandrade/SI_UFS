#include<stdio.h>
#define LINHAS 4
#define COLUNAS 4
int MATRIZ[LINHAS][COLUNAS];
int RESULTANTE[LINHAS][COLUNAS];

int VETOR[LINHAS];
int soma;

/*
    04 - Crie um programa que preencha uma matriz 10 X 20 com números inteiros e some cada uma das linhas, armazenando
    o resultado das somas em um vetor. A seguir, o programa deverá multiplicar cada elemento da matriz pela soma da linha
    correspondente e mostrar a matriz resultante.
*/

int main(void){
    // Ler a matriz e soma as linhas armazenando no VETOR;
    for (int i = 0; i < LINHAS; i++)
    {
        soma = 0;
        for (int j = 0; j < COLUNAS; j++)
        {
            scanf("%d",&MATRIZ[i][j]);
            soma += MATRIZ[i][j];

        }
        VETOR[i]=soma;

        
    }

    // Multiplica a soma armazenada em VETOR por cada elemento de MATRIZ
    for (int i = 0; i < LINHAS; i++)
    {

        for (int j = 0; j < COLUNAS; j++)
        {
            RESULTANTE[i][j] = MATRIZ[i][j]*VETOR[i];
        }
        
    }

    printf("--------Matriz Principal---------\n");
    for (int i = 0; i < LINHAS; i++)
    {

        for (int j = 0; j < COLUNAS; j++)
        {
            printf("%.2d|",MATRIZ[i][j]);
        }
        printf("\n");
        
    }

    printf("\n--------Vetor soma---------\n");
    for (int i = 0; i < LINHAS; i++)
    {
        printf("%d|",VETOR[i]);
    }
    printf("\n");

    printf("\n--------Matriz resultante---------\n");
    for (int i = 0; i < LINHAS; i++)
    {

        for (int j = 0; j < COLUNAS; j++)
        {
            printf("%.3d|",RESULTANTE[i][j]);
        }
        printf("\n");
        
    }

    
}