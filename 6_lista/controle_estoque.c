/*
NÍVEL: Fácil
Tópicos: array, acumulador, repetição, busca, dicionário 
Descrição
---------
Em um estoque são dados os códigos das mercadorias e as respectivas quantidades existentes. A seguir, são fornecidos os pedidos dos clientes. O seu objetivo  é fazer um programa de controle do estoque que:

    Leia o estoque inicial (máximo de 100 mercadorias);
    Leia os pedidos dos clientes, constituído, cada um, de: número do cliente; código da mercadoria e quantidade desejada;
    Seja verificado, para cada pedido, se ele pode ser atendido integralmente. Caso possa ser atendido, imprima OK, caso contrário ESTOQUE INSUFICIENTE;
    Ao final da execução do programa, imprima o estoque final;

Formato de entrada
------------------
Uma lista de inteiros n e m, indicando o código da mercadoria e a quantidade dessa mercadoria disponível no estoque, respectivamente.
Essa lista se encerra quando n for igual a 9999.
Depois será dada uma lista de inteiros i, j e k, onde i corresponde ao número do cliente, j é o código da mercadoria sendo solicitada e k a quantidade pedida.
Os pedidos se encerram quando i for igual a 9999.

Formato de saída
----------------
Para cada pedido, a saída deve imprimir OK ou ESTOQUE INSUFICIENTE, seguida de um final de linha.
Ao final dos pedidos, deve ser impresso uma lista de inteiros x, y correspondendo ao código e ao estoque restante das mercadorias.
Cada par x, y dever ser impresso em uma linha.
*/
#include <stdio.h>
#include <stdlib.h>
#define SIZE 100

struct e
{
    int codigo;
    int quantidade;
    int index; // new
};

struct p
{
    int numeroCli;
    int codigo;
    int qtd;
};

typedef struct e estoque;
typedef struct p pedido;

void imprimeEstoque(estoque *v, int *tot);
void ordenarEstoque(estoque *v, int *tot);
int buscaBinaria(estoque *v, int *tot, int c);
void verificaEstoque(estoque *v, int p, int qt);
void ordenaEstoqueIndex(estoque *v, int *tot); // new

int main(void)
{
    int *p_codig, *p_quant, *p_total, codig, quant, total;

    pedido meu_pedido;
    int numCli, codigo, quantidade;
    int i = 0;
    p_codig = &codig;
    p_quant = &quant;
    p_total = &total;
    (*p_total) = 0;

    estoque *ve;
    ve = malloc(sizeof(estoque));

    while (scanf("%d", p_codig) != EOF && i < SIZE && *p_codig != 9999)
    {

        scanf("%d", p_quant);

        ve[i].codigo = *p_codig;
        ve[i].quantidade = *p_quant;
        ve[i].index = i; // armazena o index
        (*p_total)++;
        i++;
    }

    ordenarEstoque(ve, p_total);

    while (scanf("%d", &numCli) != EOF && numCli != 9999)
    {
        scanf("%d", &codigo);
        scanf("%d", &quantidade);

        int posi = buscaBinaria(ve, p_total, codigo);
        verificaEstoque(ve, posi, quantidade);
    }

    ordenaEstoqueIndex(ve, p_total); // new
    imprimeEstoque(ve, p_total);

    return EXIT_SUCCESS;
}

void imprimeEstoque(estoque *v, int *tot)
{
    for (int i = 0; i < (*tot); i++)
        printf("%d %d\n", v[i].codigo, v[i].quantidade);
}

void ordenarEstoque(estoque *v, int *tot)
{
    for (int j = 1; j < (*tot); ++j)
    {
        int c = v[j].codigo;
        int q = v[j].quantidade;
        int k = v[j].index; //new
        int i;
        for (i = j - 1; i >= 0 && v[i].codigo > c; --i)
        {
            v[i + 1].codigo = v[i].codigo;
            v[i + 1].quantidade = v[i].quantidade;
            v[i + 1].index = v[i].index; //new
        }
        v[i + 1].codigo = c;
        v[i + 1].quantidade = q;
        v[i + 1].index = k; //new
    }
}

void verificaEstoque(estoque *v, int p, int qt)
{
    if (v[p].quantidade >= qt)
    {
        printf("OK\n");
        v[p].quantidade -= qt;
    }
    else
    {
        printf("ESTOQUE INSUFICIENTE\n");
    }
}

int buscaBinaria(estoque *v, int *tot, int c)
{
    int baixo = 0;
    int alto = (*tot) - 1;
    while (baixo <= alto)
    {
        int meio = (baixo + alto) / 2;

        if (v[meio].codigo == c)
            return meio;

        if (v[meio].codigo > c)
            alto = meio - 1;
        else
            baixo = meio + 1;
    }

    return -1;
}

void ordenaEstoqueIndex(estoque *v, int *tot)
{ // new
    for (int j = 1; j < (*tot); ++j)
    {
        int c = v[j].codigo;
        int q = v[j].quantidade;
        int k = v[j].index; //new
        int i;
        for (i = j - 1; i >= 0 && v[i].index > k; --i)
        {
            v[i + 1].codigo = v[i].codigo;
            v[i + 1].quantidade = v[i].quantidade;
            v[i + 1].index = v[i].index; //new
        }
        v[i + 1].codigo = c;
        v[i + 1].quantidade = q;
        v[i + 1].index = k; //new
    }
}