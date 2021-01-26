/*
NÍVEL: Iniciante
Tópicos: array, busca

Descrição
---------
A aluna de Programação 1 Sofia estava com muita dificuldade para verificar o maior número e o menor número dada uma sequência de inteiros. 
A sua tarefa é criar um programa que mostre o maior e o menor número dessa sequência e a quantidade de vezes que eles aparecem nessa sequência.
Formato de entrada
Um inteiro n e logo em seguida uma sequência de n inteiros positivos menores ou iguais a 1000.

Formato de saída
----------------
A saída deverá conter o maior e o menor número dessa sequência, seguidos da quantidade de vezes que eles repetem.
*/
#include <stdio.h>
#include <stdlib.h>

void ordenar(int *v, int *p_tamanho);
int buscaBinaria(int x, int n, int *v);
int oMaior(int *x, int *n);
int oMenor(int *n, int *v);

int main(void)
{
    int tamanho, valor, menor, maior, index_maior;
    int *p_tamanho, *p_valor, *p_menor, *p_maior, *p_index_maior;
    p_tamanho = &tamanho;
    p_valor = &valor;
    p_menor = &menor;
    p_maior = &maior;
    p_index_maior = &index_maior;

    int *vector;
    scanf("%d", p_tamanho);
    vector = malloc(sizeof(int) * (*p_tamanho));

    for (int i = 0; i < (*p_tamanho); i++)
    {
        scanf("%d", p_valor);
        vector[i] = (*p_valor);
    }

    ordenar(vector, p_tamanho);
    (*p_menor) = vector[0];
    (*p_maior) = vector[tamanho - 1];

    (*p_index_maior) = buscaBinaria(*p_maior, *p_tamanho, vector);
    int indexMenor = buscaBinaria(*p_menor, *p_tamanho, vector);

    printf("Maior: %d apareceu %d vezes\n",
           maior, oMaior(p_index_maior, p_tamanho));

    printf("Menor: %d apareceu %d vezes\n",
           menor, oMenor(p_tamanho, vector));
}

void ordenar(int *v, int *p_tamanho)
{
    for (int j = 1; j < (*p_tamanho); ++j)
    {
        int x = v[j];
        int i;
        for (i = j - 1; i >= 0 && v[i] > x; --i)
            v[i + 1] = v[i];
        v[i + 1] = x;
    }
}

int buscaBinaria(int x, int n, int *v)
{
    int e = -1,
        d = n;
    while (e < d - 1)
    {
        int m = (e + d) / 2;
        if (v[m] < x)
            e = m;
        else
            d = m;
    }
    return d;
}

int oMaior(int *index, int *n)
{
    int vezes = 0;
    for (int i = (*index); i < (*n); i++)
        vezes++;
    return vezes;
}

int oMenor(int *n, int *v)
{
    int vezes = 1, i = 0;

    while (v[i] == v[i + 1] && i < (*n))
    {
        vezes++;
        i++;
    }
    return vezes;
}