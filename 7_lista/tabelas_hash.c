/*
NÍVEL: Médio
Tópicos: estrutura de dados 

Descrição
---------

Implemente uma tabela hash utilizando a técnica do encadeamento para tratar colisões. Assim, cada posição da tabela T deve armazenar uma lista encadeada, que armazena os elementos inseridos (k) na referida posição ( T[h(k)] ), organizados de modo crescente. 
A função hash a ser utilizada deve ser o método da divisão (h(k) = k % m). 
O seu programa deve contemplar as seguintes operações:

1)inserir (elemento deve ser inserido em ordem crescente na lista da posição T[h(k)]). 
Inserções duplicadas são válidas;
2)remover;
3)imprimir, em que as listas encadeadas de cada posição da tabela devem ser impressas em ordem crescente, de T[0] à T[m-1];
4)procurar, que deve procurar um elemento na tabela e informar: (i) o 
número de elementos presentes na tabela, (ii) se o elemento em questão foi encontrado ou não, e (iii) quantos elementos da tabela foram acessados (inclusive ele próprio) até que o elemento fosse encontrado. Esses dados servem para refletir, por meio da comparação entre o número de elementos presentes na tabela e o número de elementos acessados, a eficiência da tabela hash para buscar elementos.

Formato de entrada
------------------

Primeira linha da entrada: valor de 'm'
a k: inserção do elemento "k"
r k: remoção do elemento "k"
i: imprimir tabela hash
f: finalizar programa 

Formato de saída
---------------

impressão do resultado da busca:
BUSCA POR ?
numero de elementos da tabela hash: ?
elemento ? encontrado!
numero de elementos acessados na tabela hash: ?
impressão da tabela hash: (exemplo com m = 29)
[0]:Lista vazia!
[1]:1=>30=>59=>
[2]:2=>2=>31=>31=>
[3]:3=>32=>61=>
[4]:4=>4=>4=>4=>33=>
[5]:5=>5=>
[6]:35=>
[7]:36=>
[8]:8=>8=>66=>
[9]:9=>67=>67=>
[10]:10=>39=>39=>
[11]:11=>11=>11=>69=>69=>69=>
[12]:12=>70=>
[13]:42=>71=>
[14]:14=>43=>43=>
[15]:15=>44=>73=>73=>73=>
[16]:16=>74=>
[17]:17=>46=>46=>
[18]:18=>47=>47=>47=>76=>76=>
[19]:48=>48=>48=>77=>
[20]:20=>49=>
[21]:21=>50=>
[22]:51=>51=>
[23]:52=>
[24]:24=>
[25]:25=>25=>25=>54=>54=>
[26]:Lista vazia!
[27]:Lista vazia!
[28]:28=>
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
void insere(int h, int ch, celula *p);
void imprimeEncontrado(celula *p, int x);

void buscaRemove(int x, celula **lista);
celula *busca(int x, celula *lista);

celula **tb;

int passos = 1;
int totalDeElementos = 0;
int M, valor, hashcode;

int main(void)
{
    celula *p_elemento;
    char letra;
    scanf("%d", &M);
    tb = malloc(M * sizeof(celula *));

    while (scanf("%c", &letra) != EOF && letra != 'f')
    {
        if (letra == 'a')
        {
            scanf("%d", &valor);
            contabiliza(valor);
        }

        if (letra == 'i')
            imprimehash();

        if (letra == 'r')
        {
            scanf("%d", &valor);
            hashcode = hash(valor, M);
            buscaRemove(valor, &tb[hashcode]);
        }
        if (letra == 'p')
        {
            scanf("%d", &valor);
            printf("BUSCA POR %d\n", valor);
            hashcode = hash(valor, M);
            p_elemento = busca(valor, tb[hashcode]);
            imprimeEncontrado(p_elemento, valor);
        }
    }

    return EXIT_SUCCESS;
}

void contabiliza(int ch)
{
    int h = hash(ch, M);
    celula *p = tb[h];
    insere(h, ch, p);
    totalDeElementos += 1;
}

int hash(int ch, int m) { return ch % m; }

void imprimehash()
{
    printf("imprimindo tabela hash:\n");
    for (int i = 0; i < M; i++)
    {
        printf("[%d]:", i);
        if (tb[i] != NULL)
        {
            imprimeList(tb[i]);
            printf("\n");
        }
        else
            printf("Lista vazia!\n");
    }
}

void imprimeList(celula *li)
{
    celula *p = li;
    while (p != NULL)
    {
        printf("%d=>", p->chave);
        p = p->prox;
    }
}

// insere em de forma ordenada um elemento na lista.
void insere(int h, int ch, celula *p)
{
    celula *nova;
    nova = malloc(sizeof(celula));

    nova->chave = ch;
    nova->ocorr = 1;

    celula *anterior, *atual;
    nova->prox = NULL;
    anterior = NULL;

    atual = tb[h];

    while (atual != NULL && ch > atual->chave)
    {
        anterior = atual;
        atual = atual->prox;
    }

    if (anterior == NULL)
    {
        nova->prox = tb[h];
        tb[h] = nova;
    }
    else
    {
        anterior->prox = nova;
        nova->prox = atual;
    }
}

celula *busca(int x, celula *lista)
{
    celula *p;
    p = lista;
    passos = 1;
    while (p != NULL && p->chave != x)
    {
        p = p->prox;
        passos++;
    }
    return p;
}

void buscaRemove(int x, celula **lista)
{
    celula *anterior, *atual;
    celula *lixo;
    if ((*lista) != NULL)
    {
        if (x == (*lista)->chave)
        {
            lixo = *lista;
            *lista = (*lista)->prox;
            free(lixo);
            totalDeElementos -= 1;
        }
        else
        {
            anterior = (*lista);
            atual = (*lista)->prox;
            while (atual != NULL && x != atual->chave)
            {
                anterior = atual;
                atual = atual->prox;
            }
            if (atual != NULL)
            {
                lixo = atual;
                anterior->prox = atual->prox;
                free(lixo);
                totalDeElementos -= 1;
            }
        }
    }
}

void imprimeEncontrado(celula *p, int x)
{
    printf("numero de elementos da tabela hash: %d\n", totalDeElementos);
    if (p != NULL)
    {
        printf("elemento %d encontrado!\n", x);
    }
    else
    {
        printf("elemento nao encontrado!\n");
        passos--;
    }
    printf("numero de elementos acessados na tabela hash: %d\n", passos);
}