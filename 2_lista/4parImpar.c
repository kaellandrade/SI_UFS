#include <stdio.h>
#include <stdlib.h>

#define LENGTH 15
#define VETLENGTH 5
/*DESCRIÇÃO
-----------
Neste problema você deverá ler 15 valores colocá-los em 2 arrays conforme estes valores forem pares ou ímpares. 
Só que o tamanho de cada um dos dois arrays é de 5 posições. 
Então, cada vez que um dos dois arrays encher, você deverá imprimir todo o array e utilizá-lo novamente para os próximos números que forem lidos. 
Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois arrays, imprimindo primeiro os valores do array ímpar. 
Cada array pode ser preenchido tantas vezes quantas for necessário.

Formato de entrada:
A entrada contém 15 números inteiros.
EX: 1 ,3, 4, -4, 2, 3, 8, 2, 5, -7, 54, 76, 789, 23, 98

Formato de saída:
par[0] = 4
par[1] = -4
par[2] = 2
par[3] = 8
par[4] = 2
impar[0] = 1
impar[1] = 3
impar[2] = 3
impar[3] = 5
impar[4] = -7
impar[0] = 789
impar[1] = 23
par[0] = 54
par[1] = 76
par[2] = 98


*/
void adicionaElemento(int *vetor, int *posicao, int *valor);
void imprimePar(int *vetor, int *tamanho);
void imprimeImpar(int *vetor, int *tamanho);
int verificaPar(int *x);

int main()
{
    int impares[VETLENGTH];
    int pares[VETLENGTH];
    int valor;
    int total_impares = 0;
    int total_pares = 0;
    for (int i = 0; i < LENGTH; i++)
    {
        scanf("%d", &valor);
        // Verifica o valor digitado e armazena no respectivo vetor
        if (verificaPar(&valor))
        {
            adicionaElemento(&pares[0], &total_pares, &valor);
        }
        else
        {
            adicionaElemento(&impares[0], &total_impares, &valor);
        }

        // Verifica se o vetor impar e o vetor par encheu
        if (total_impares == 5)
        {
            imprimeImpar(&impares[0], &total_impares);
            total_impares = 0; // Zera o contador do vetor impares
        }

        if (total_pares == 5)
        {
            imprimePar(&pares[0], &total_pares);
            total_pares = 0; // Zera o contador do vetor pares
        }
    }
    imprimeImpar(&impares[0], &total_impares);
    imprimePar(&pares[0], &total_pares);

    return EXIT_SUCCESS;
}
// Dado um valor x, verifica se x é par
int verificaPar(int *x)
{
    if ((*x) % 2 == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
// dado um vetor v uma posicao p e um valor x
// v[p]=x
void adicionaElemento(int *vetor, int *posicao, int *valor)
{
    vetor[*posicao] = *valor;
    (*posicao)++;
}
void imprimeImpar(int *vetor, int *tamanho)
{
    for (int i = 0; i < *tamanho; i++)
    {
        printf("impar[%d] = %d\n", i, vetor[i]);
    }
}
void imprimePar(int *vetor, int *tamanho)
{
    for (int i = 0; i < *tamanho; i++)
    {
        printf("par[%d] = %d\n", i, vetor[i]);
    }
}