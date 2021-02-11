/**
NÍVEL: Médio
Tópicos: Árvore
Descrição
---------
Uma árvore binária é frequentemente usada para maximizar a eficiente de buscas. 
Mas quão eficiente essas buscas são?

Nessa questão você vai receber uma sequência de inteiros. 
Dessa sequência você vai construir uma árvore binária.

Depois você vai receber requisições, essas requisições são N inteiros, para cada inteiro você
vai ter que dizer quantas comparações são feitas até achar este na busca linear e quantas são necessárias na árvore binária.

Formato de entrada
------------------

Você receberá um inteiro N.
Depois N inteiros distintos a serem armazenados na árvore binária.
Depois receberá as requisições em que cada requisição é um inteiros X.

Formato de saída
----------------
Para cada requisição, você deve imprimir dois inteiros separados por espaços.

X Y
X = Número de comparações na busca linear, incluindo a comparação de igual.
Y = Número de comparações na busca em árvore binária, incluindo a comparação de igual.
Cada requisição deve ser separada por uma quebra de linha.
*/

#include <stdlib.h>
#include <stdio.h>
typedef struct reg2 celula;
typedef struct reg noh;
struct reg
{
    int conteudo;
    noh *esq;
    noh *dir;
};
struct reg2
{
    int conteudo;
    struct reg2 *prox;
};

typedef int boolean;

typedef noh *arvore;
typedef celula *fila;

arvore inserir(arvore raiz, int valor);
fila addFila(fila fi, int valor);

void buscaBIN(arvore arv, int valor);
void buscaLIN(fila fi, int valor);


int buscaB = 1;
int buscaL = 0;

arvore arvoreBUSC;
fila filaEnc;

int main(int argc, char const *argv[])
{
    int N, Ns, find;

    arvoreBUSC = NULL;

    filaEnc = malloc(sizeof(fila));
    filaEnc->prox = filaEnc;

    scanf("%d", &N);

    for (int i = 0; i < N; i++)
    {
        scanf("%d", &Ns);
        arvoreBUSC = inserir(arvoreBUSC, Ns);
        filaEnc = addFila(filaEnc, Ns);
    }
    while (scanf("%d", &find) != EOF)
    {
        buscaBIN(arvoreBUSC, find);
        buscaLIN(filaEnc, find);

        printf("%d %d\n", buscaL, buscaB);

    }

    return 0;
}

arvore inserir(arvore raiz, int valor)
{
    if (raiz == NULL)
    { // verifica arvore vazia
        arvore novo = malloc(sizeof(arvore));
        novo->conteudo = valor;
        novo->dir = NULL;
        novo->esq = NULL;
        return novo;
    }
    else
    {
        if (valor < raiz->conteudo)
            raiz->esq = inserir(raiz->esq, valor);
        if (valor > raiz->conteudo)
            raiz->dir = inserir(raiz->dir, valor);
    }
    return raiz;
}

void buscaBIN(arvore arv, int valor)
{
    buscaB = 1;
    while (arv != NULL && arv->conteudo != valor)
    {
        buscaB++;
        if (arv->conteudo > valor)
        {
            arv = arv->esq;
        }
        else
        {
            arv = arv->dir;
        }
    }
}

void buscaLIN(fila fi, int valor)
{
    buscaL = 0;
    fila p;
    p = fi->prox;
    while (p != fi)
    {
        ++buscaL;
        if(p->conteudo == valor)
            return;

        p = p->prox;

    }
}

fila addFila(fila fi, int valor)
{
    fila nova;
    nova = malloc(sizeof(celula));

    nova->prox = fi->prox;
    fi->prox = nova;
    fi->conteudo = valor;
    return nova;
}