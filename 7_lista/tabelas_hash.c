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
typedef celula **tabelaHash;
typedef celula *listaEnc;
struct reg
{
    int chave, ocorr;
    celula *prox;
};

void contabiliza(int ch);
int hash(int ch, int m);
void imprimehash();
void imprimeList();
listaEnc insere(int h, int ch);
void imprimeEncontrado(listaEnc lista, int x);

listaEnc buscaRemove(int x, listaEnc lista);
celula *busca(int x, listaEnc lista);

tabelaHash tb;

int passos = 1;
int totalDeElementos = 0;
int M, valor, hashcode;

int main(void)
{
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
            listaEnc r_elemento = tb[hashcode]; // o elmento para remover está nesta lista;
            tb[hashcode] = buscaRemove(valor, r_elemento);
        }
        if (letra == 'p')
        {
            scanf("%d", &valor);
            printf("BUSCA POR %d\n", valor);
            hashcode = hash(valor, M);
            listaEnc p_elemento = tb[hashcode]; // referencia a lista encadeada onde o elemento será procuado

            p_elemento = busca(valor, p_elemento);
            imprimeEncontrado(p_elemento, valor);
        }
    }

    return EXIT_SUCCESS;
}

void contabiliza(int ch)
{
    int h = hash(ch, M);
    tb[h] = insere(h, ch); // atualiza a tabela com anova lista modificada;
    totalDeElementos += 1; // apois inserir o elemento atualiza o total de elementos
}

int hash(int ch, int m)
{
    return ch % m;
}

void imprimehash()
{
    printf("imprimindo tabela hash:\n");
    for (int i = 0; i < M; i++)
    {
        listaEnc listaAtual;
        listaAtual = tb[i]; // Referencia a lista na posição da tabela
        printf("[%d]:", i);
        if (listaAtual != NULL)
        {
            imprimeList(listaAtual); //imprima essa lista;
            printf("\n");
        }
        else
            printf("Lista vazia!\n");
    }
}

void imprimeList(listaEnc lista)
{
    listaEnc cabeca_lista = lista;
    while (cabeca_lista != NULL)
    {
        printf("%d=>", cabeca_lista->chave);
        cabeca_lista = cabeca_lista->prox;
    }
}

// insere em de forma ordenada um elemento na lista.
listaEnc insere(int h, int ch)
{
    listaEnc lista = tb[h]; // captura a lista encadeada aqual devemos trabalhar
    celula *nova;
    nova = malloc(sizeof(celula));

    nova->chave = ch;
    nova->ocorr = 1;

    celula *anterior, *atual;
    nova->prox = NULL;
    anterior = NULL;

    atual = lista;

    while (atual != NULL && ch > atual->chave)
    {
        anterior = atual;
        atual = atual->prox;
    }

    if (anterior == NULL)
    {
        nova->prox = lista;
        lista = nova;
    }
    else
    {
        anterior->prox = nova;
        nova->prox = atual;
    }
    return lista;
}

listaEnc busca(int x, listaEnc lista)
{
    listaEnc cabecaLista;
    cabecaLista = lista;
    passos = 1; // contabiliza os passos até encontrar o elemento
    while (cabecaLista != NULL && cabecaLista->chave != x)
    {
        cabecaLista = cabecaLista->prox;
        passos++;
    }
    return cabecaLista;
}

listaEnc buscaRemove(int x, listaEnc lista)
{
    celula *anterior, *atual;
    celula *lixo;
    if (lista != NULL){
        if (x == lista->chave){
            lixo = lista;
            lista = lista->prox;
            free(lixo);
            totalDeElementos -= 1;
        }
        else{
            anterior = lista;
            atual = lista->prox;
            while (atual != NULL && x != atual->chave){
                anterior = atual;
                atual = atual->prox;
            }
            if (atual != NULL){
                lixo = atual;
                anterior->prox = atual->prox;
                free(lixo);
                totalDeElementos -= 1;
            }
        }
    }
    return lista; // retornar a lista atualizada
}

void imprimeEncontrado(listaEnc lista, int x)
{
    printf("numero de elementos da tabela hash: %d\n", totalDeElementos);
    if (lista != NULL)
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