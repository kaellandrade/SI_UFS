/*
NÍVEL: Fácil
Tópicos: array, repetição, busca

Descrição
---------
Faça um programa em linguagem C que leia uma sequência de 101 números reais, verifique se o último número está presente nos 100 primeiros números e imprima as posições do array em que ele está presente. 
O programa deve mostrar as mensagens “Digite a sequencia de numero:” e “Indice no qual o numero desejado aparece:”.

Formato de entrada
------------------
O usuário deve digitar uma sequência de 101 números reais

Formato de saída
----------------
O programa deve exibir uma sequência de inteiros separados por um final de linha, onde cada inteiro representa o índice do array em que foi encontrado o último número lido. 
Se o último número não for encontrado nos 100 números anteriores não imprima nada. Na tela, devem ser impressos:


Digite a sequencia de numero:
Indice no qual o numero desejado aparece:
n
n
n
n
*/
#include <stdio.h>
#include <stdlib.h>
#define SIZE 101
struct reg
{
    float valor;
    int indx;
};
typedef struct reg tupla;

void ordenar(tupla *v, int tamanho);
int buscaBinaria(float x, int n, tupla *v);
void imprimeOcorrencias(tupla *v, int index, int tamanho);

int main(void)
{

    float valor, ultimo;
    float *p_valor, *p_ultimo;

    tupla *vector;

    vector = malloc(sizeof(tupla) * SIZE);

    p_valor = &valor;
    p_ultimo = &ultimo;

    printf("Digite a sequencia de numero:\n");
    for (int i = 0; i < SIZE; i++)
    {
        scanf("%f", p_valor);
        vector[i].valor = (*p_valor);
        vector[i].indx = i;
    }

    // Armazena o �ltimo valor digitado
    *p_ultimo = vector[SIZE - 1].valor;

    // ordena meu vetor;
    ordenar(vector, SIZE);

    int index = buscaBinaria(*p_ultimo, SIZE, vector);
    imprimeOcorrencias(vector, index, SIZE);
}

void ordenar(tupla *v, int tamanho)
{
    for (int j = 1; j < tamanho; ++j)
    {
        float x = v[j].valor;
        int y = v[j].indx;
        int i;
        for (i = j - 1; i >= 0 && v[i].valor > x; --i)
        {
            v[i + 1].valor = v[i].valor;
            v[i + 1].indx = v[i].indx;
        }
        v[i + 1].valor = x;
        v[i + 1].indx = y;
    }
}

int buscaBinaria(float x, int n, tupla *v)
{
    int e = -1,
        d = n;
    while (e < d - 1)
    {
        int m = (e + d) / 2;
        if (v[m].valor < x)
            e = m;
        else
            d = m;
    }
    return d;
}

void imprimeOcorrencias(tupla *v, int index, int tamanho)
{
    printf("Indice no qual o numero desejado aparece:\n");
    for (int i = index; v[i].valor == v[i + 1].valor; i++)
    {
        printf("%d\n", v[i].indx);
    }
}