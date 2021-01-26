/*
NÍVEL: Médio
Tópicos: estrutura de dados, array, alocação dinâmica

Descrição
---------
As tabelas Hash, também conhecidas como tabelas de dispersão, armazenam elementos com base no valor absoluto de suas chaves e em técnicas de tratamento de colisões. Para o cálculo do endereço onde deve ser armazenada uma determinada chave, utiliza-se uma função denominada função de dispersão, que transforma a chave em um dos endereços disponíveis na tabela.
Suponha que uma aplicação utilize uma tabela de dispersão com 13 endereços-base (índices de 0 a 12) e empregue a função de dispersão h(x) = x mod 13, em que x representa a chave do elemento cujo endereço-base deve ser calculado.
Se a chave x for igual a 49, a função de dispersão retornará o valor 10, indicando o local onde esta chave deverá ser armazenada. Se a mesma aplicação considerar a inserção da chave 88, o cálculo retornará o mesmo valor 10, ocorrendo neste caso uma colisão. O Tratamento de colisões serve para resolver os conflitos nos casos onde mais de uma chave é mapeada para um mesmo endereço-base da tabela. Este tratamento pode considerar, ou o recálculo do endereço da chave ou o encadeamento externo ou exterior.
O professor gostaria então que você o auxiliasse com um programa que calcula o endereço para inserções de diversas chaves em algumas tabelas, com funções de dispersão e tratamento de colisão por encadeamento exterior.

Formato de entrada
------------------
A entrada contém vários casos de teste. A primeira linha de entrada contém um inteiro N indicando a quantidade de casos de teste. Cada caso de teste é composto por duas linhas. A primeira linha contém um valor M (1 ≤ M ≤ 100) 
que indica a quantidade de endereços-base na tabela (normalmente um número primo) seguido por um espaço e um valor C (1 ≤ C ≤ 200) que indica a quantidade de chaves a serem armazenadas. A segunda linha contém cada uma das chaves (com valor entre 1 e 200), separadas por um espaço em branco.

É importante considerar que nessa tabela específica, uma mesma chave poderá ser inserida várias vezes. 
O elemento duplicado deve ser inserido no final da lista.

Formato de saída
----------------

A saída deverá ser impressa conforme os exemplos fornecidos abaixo, onde a quantidade de linhas de cada 
caso de teste é determinada pelo valor de M. Uma linha em branco deverá separar dois conjuntos de saída.
*/
#include <stdlib.h>
#include <stdio.h>
typedef struct reg celula;

struct reg
{
    int chave, ocorr;
    celula *prox;
};

void contabiliza(int ch);
int hash(int ch, int m);
void imprimehash();
void imprimeList();
celula *retornaNo();
celula *inserir(int ch, celula *p);
celula *busca(int x, celula *lista);

celula **tb;
int M, toatlChave, chave, valor, hashcode, testes;

int main(void)
{
    celula *p_elemento;

    scanf("%d", &testes);

    for (int i = 0; i < testes; i++)
    {
        scanf("%d %d", &M, &toatlChave);
        tb = malloc(M * sizeof(celula *));
        for (int j = 0; j < toatlChave; j++)
        {
            scanf("%d", &chave);
            contabiliza(chave);
        }
        imprimehash();
        printf("\n");
    }

    return EXIT_SUCCESS;
}

void contabiliza(int ch)
{
    int h = hash(ch, M);
    celula *p = tb[h];
    tb[h] = inserir(ch, p);
}

int hash(int ch, int m) { return ch % m; }

void imprimehash()
{
    for (int i = 0; i < M; i++)
    {
        printf("%d ->", i);
        if (tb[i] != NULL)
        {
            imprimeList(tb[i]);
            printf("\n");
        }
        else
            printf(" \\\n");
    }
}

void imprimeList(celula *li)
{
    celula *p = li;
    while (p != NULL)
    {
        printf(" %d ->", p->chave);
        p = p->prox;
    }
    printf(" \\");
}

celula *retornaNo()
{
    celula *nova = (celula *)malloc(sizeof(celula));
    return nova;
}

celula *busca(int x, celula *lista)
{
    celula *p;
    p = lista;
    while (p != NULL && p->chave != x)
    {
        p = p->prox;
    }
    return p;
}
celula *inserir(int ch, celula *p)
{
    celula *no = retornaNo();
    no->chave = ch;

    if (p == NULL)
    {
        no->prox = NULL;
        p = no;
    }
    else
    {
        celula *aux;
        aux = p;
        while (aux->prox != NULL)
        {
            aux = aux->prox;
        }
        no->prox = NULL;
        aux->prox = no;
    }

    return p;
}