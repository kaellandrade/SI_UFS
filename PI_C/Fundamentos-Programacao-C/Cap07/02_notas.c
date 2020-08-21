#include<stdio.h>
#define LINHAS 3
#define COLUNAS 3
/*
Faça um programa que preencha uma matriz 10 X 3 com as notas de dez alunos em três provas.
O programa deverá mostrar um relatório com o número dos alunos (número da linha) e a prova em que
cada aluno obteve menor nota. Ao final do relatório, deverá mostrar quantos alunos tiveram  menor
nota em cada uma das provas: na prova 1, na prova 2 e na prova 3.
*/

int NOTAS[LINHAS][COLUNAS];
int menor_nota, indice_da_prova, conta_aluno;
int quant1 = 0;
int quant2 = 0;
int quant3 = 0;


int main(void){

    //Preenche minha matriz;
    for (int i = 0; i < LINHAS; i++){
        printf("-----%dº Aluno----\n",i+1);
        for (int j = 0; j < COLUNAS; j++){
            printf("%dº nota:\n",j+1);
            scanf("%d",&NOTAS[i][j]);
        }
    }
    // Menor nota de cada aluno
    for (int i = 0; i < LINHAS; i++){
        menor_nota = NOTAS[i][0];
        indice_da_prova = 0;
        for (int j = 0; j < COLUNAS; j++){
            if(NOTAS[i][j] < menor_nota){
                menor_nota = NOTAS[i][j];
                indice_da_prova = j;
            }

            
        }
        if (indice_da_prova == 0){
            quant1++;  
        }else if(indice_da_prova == 1){
            quant2++;
        }else{
            quant3++;
        }
        printf("Aluno %dº obteve a menor nota na %dº prova.\n",i+1, indice_da_prova+1);
    }
        printf("Prova1: %d\nProva2: %d\nProva3: %d\n",quant1, quant2, quant3);
}