/*
NÍVEL: Fácil
Tópicos: array, decisão, busca 

Descrição
---------
Suponha dois vetores de 15 elementos cada, contendo: código de área e telefone. 
Faça um programa em linguagem C que permita buscar um código e imprimir todos os números de telefone que começam com aquele código de área. Caso não haja nenhum telefone com aquele código, deve ser mostrada a mensagem "Nao ha nenhum telefone com o codigo n".

Formato de entrada
-----------------
A entrada consiste de 15 pares de números, 
contendo respectivamente o código de área e o numero do telefone, e o código de área desejado.
Formato de saída
----------------
O programa deve exibir os números de telefone que tem o código de área desejado após a mensagem "Telefones com o codigo de area n:" ou ""Nao ha nenhum telefone com o codigo n", imprimindo na tela:

Digite o codigo de area e o telefone:
Digite o codigo de area e o telefone:
Digite o codigo de area e o telefone:
Digite o codigo de area e o telefone:
Digite o codigo de area e o telefone:
Digite o codigo de area e o telefone:
Digite o codigo de area e o telefone:
Digite o codigo de area e o telefone:
Digite o codigo de area e o telefone:
Digite o codigo de area e o telefone:
Digite o codigo de area e o telefone:
Digite o codigo de area e o telefone:
Digite o codigo de area e o telefone:
Digite o codigo de area e o telefone:
Digite o codigo de area e o telefone:
Digite o codigo de area:
Telefones com o codigo de area n:
n
n
n
*/
#include <stdio.h>
#include <stdlib.h>
#define SIZE 15
struct reg
{
    int codigo;
    int numero;
};
typedef struct reg listaPhone;

int buscaBinaria(int x, int n, listaPhone *v);
void imprimeLista(listaPhone *v, int *index, int *codigo);
void ordenar(listaPhone *v, int tamanho);
void imprime(listaPhone *v, int tamanho);

int main(void)
{

    int area, numero, buscar, posicao;
    int *p_area, *p_numero, *p_buscar, *p_posicao;

    listaPhone *vector;

    vector = malloc(sizeof(listaPhone) * SIZE);

    p_area = &area;
    p_numero = &numero;
    p_buscar = &buscar;
    p_posicao = &posicao;

    for (int i = 0; i < SIZE; i++)
    {
        printf("Digite o codigo de area e o telefone:\n");
        scanf("%d", p_area);
        scanf("%d", p_numero);
        vector[i].codigo = (*p_area);
        vector[i].numero = (*p_numero);
    }

    printf("Digite o codigo de area desejado:\n");
    scanf("%d", p_buscar);

    ordenar(vector, SIZE); /// ordena meu vetor;

    (*p_posicao) = buscaBinaria(buscar, SIZE, vector);

    if (*p_posicao == -1)
        printf("Nao ha nenhum telefone com o codigo %d\n", *p_buscar);
    else
        imprimeLista(vector, p_posicao, p_buscar);
}

void ordenar(listaPhone *v, int tamanho)
{
    for (int j = 1; j < tamanho; ++j)
    {
        int x = v[j].codigo;
        int y = v[j].numero;
        int i;
        for (i = j - 1; i >= 0 && v[i].codigo > x; --i)
        {
            v[i + 1].codigo = v[i].codigo;
            v[i + 1].numero = v[i].numero;
        }
        v[i + 1].codigo = x;
        v[i + 1].numero = y;
    }
}

int buscaBinaria(int x, int n, listaPhone *v)
{
    int baixo = 0;
    int alto = n - 1;
    while (baixo <= alto)
    {
        int meio = (baixo + alto) / 2;

        if (v[meio].codigo == x)
            return meio - 1;

        if (v[meio].codigo > x)
            alto = meio - 1;
        else
            baixo = meio + 1;
    }

    return -1;
}

void imprimeLista(listaPhone *v, int *index, int *codigo)
{
    printf("Telefones com o codigo de area %d:\n", *codigo);
    int i = *index;
    while (v[i].codigo == (*codigo))
    {
        printf("%d %d\n", v[i].codigo, v[i].numero);
        i++;
    }
}

void imprime(listaPhone *v, int tamanho)
{
    for (int i = 0; i < tamanho; i++)
    {
        printf("%d-%d\n", v[i].codigo, v[i].numero);
    }
}