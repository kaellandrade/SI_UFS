#include <stdio.h>
/* DESCRIÇÃO
-------------

Faça um programa que leia n números inteiros dados em um array e os imprime:
a) na ordem inversa dos números dados
b) com um deslocamento para a esquerda
c) ordenado em ordem decrescente

Formato de entrada:
Consiste de um número n indicando a quantidade de números a serem passados na entrada, seguido de n números separados por um espaço em branco.
Suponha que o maior n dado é 10000.

Formato de saída:
Consiste de 3 sequências de números, separados por um espaço em branco. Após cada sequência, existe um final de linha. 
A primeira sequência contém os números na ordem inversa, a segunda com o deslocamento para a esquerda e a terceira contém os números ordenados em ordem decrescente. 
Lembre-se que depois do último número de cada sequência não existe espaço.

Exem:
6
9 3 1 6 8 5

5 8 6 1 3 9
3 1 6 8 5 9
9 8 6 5 3 1

*/

void deslocaLeft(int *vet, int *length);
void ordenaDecres(int *vet, int *length);
void imprimeArray(int *vet, int *length, int inverter);
void troca(int *x, int *y);

void main(void)
{
    int tamanho, valor, *p_tamanho, *p_valor;
    p_tamanho = &tamanho;
    p_valor = &valor;
    // Ler o tamanho do array
    scanf("%d", p_tamanho);
    int vetor[*p_tamanho];
    // Ler e armazena os valores do vetor
    for (int i = 0; i < (*p_tamanho); i++)
    {
        scanf("%d", p_valor);
        vetor[i] = *p_valor;
    }

    // dado um vetor v e seu tamanho, v será impresso na orde inversa.
    imprimeArray(vetor, p_tamanho, 1);

    // dado um vetor v e seu tamanho, v será deslocado para esquerda.
    deslocaLeft(vetor, p_tamanho);

    // imprime o vetor novamente
    imprimeArray(vetor, p_tamanho, 0);

    // dado um vetor v e seu tamanho, v será ordenado em ordem decrescente.
    ordenaDecres(vetor, p_tamanho);

    // imprime o vetor novamente
    imprimeArray(vetor, p_tamanho, 0);
}

// dada a primeira posição de mémoria de uma vetor e seu respectivo tamanho,
// imprimeArray irá mostrar os valores do vetor.
// Se for passado true == 1 para o parâmetro int invert, o vetor será impresso na forma reversa.
void imprimeArray(int *vet, int *length, int inverter)
{
    if (inverter) // é para imverter ?
    {
        for (int i = (*length - 1); i >= 0; i--)
        {
            printf("%d", vet[i]);
        }
    }
    else
    {
        for (int i = 0; i < (*length); i++)
        {
            printf("%d", vet[i]);
        }
    }

    printf("\n");
}

// dada a primeira posição de mémoria de uma vetor e seu respectivo tamanho,
// deslocaLeft irá deslocar o vetor para esquerda.
void deslocaLeft(int *vet, int *length)
{
    int primeiro_elemento, *p_primeiro;
    p_primeiro = &primeiro_elemento;
    *p_primeiro = vet[0];
    for (int i = 0; i < (*length); i++)
    {
        vet[i] = vet[i + 1];
    }
    vet[*length - 1] = *p_primeiro; // O primeiro elemento agora fica na última posição
}

// dado um valor x e y, se x < y, então x=y e y=x
void troca(int *x, int *y)
{
    int auxiliar;
    if (*x < *y)
    {
        auxiliar = *x;
        *x = *y;
        *y = auxiliar;
    }
}

// dada a primeira posição de memória de uma vetor e seu respectivo tamanho,
// ordenaDecres ordena o vetor de forma decrescente
void ordenaDecres(int *vet, int *length)
{
    for (int i = 0; i < (*length); i++)
    {
        for (int j = 0; j < (*length - 1); j++)
        {
            troca(&vet[j], &vet[j + 1]);
        }
    }
}
