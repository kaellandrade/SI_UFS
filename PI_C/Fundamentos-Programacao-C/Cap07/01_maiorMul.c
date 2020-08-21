#include<stdio.h>
#define LINHAS 4
#define COLUNAS 4
/*
Faça um programa que preencha uma matriz M (2X2), calcule e mostre a matriz R, resultante da multiplicação
dos elementos de M pelo seu maior elemento.
*/
int M[LINHAS][COLUNAS];
int R[LINHAS][COLUNAS];
int maior_elemento;

int main(void){
    //Preenche minha matriz;
    for (int i = 0; i < LINHAS; i++)
    {
        for (int j = 0; j < COLUNAS; j++)
        {
            printf("Digite o valor da %d linha %d coluna:\n", i+1, j+1);
            scanf("%d",&M[i][j]);
            if(i==0 && j==0){ // Verifica se é o primeiro valor lido.
                maior_elemento = M[i][j];
            }else{
                if(M[i][j]>maior_elemento){
                    maior_elemento = M[i][j];
                }
            }
            
        }
        
    }

    // Multiplica os valores de M ao maior e atribui a R
    for (int i = 0; i < LINHAS; i++)
    {
        for (int j = 0; j < COLUNAS; j++)
        {
            R[i][j] = M[i][j]*maior_elemento;
            printf("%.2d | ",R[i][j]);
        }
        printf("\n");
        
    }
    

}