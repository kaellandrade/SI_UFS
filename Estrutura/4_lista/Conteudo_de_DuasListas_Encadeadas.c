/*
Descrição
---------
Dada duas listas encadeadas A e B, escreva uma função para verificar se B é um subconjunto de A.


Formato de entrada
------------------
A primeira linha de entrada será o tamanho da primeira lista (número inteiro). 
Em seguida, uma lista com n números inteiros. 
A terceira linha de entrada é o tamanho da segunda lista (número inteiro). 
Por fim, uma lista com m números inteiros. Nesse caso, m e n podem assumir valores iguais ou diferentes.


Formato de saída
----------------
0 caso não seja subconjunto; 1 caso contrário.
*/
#include <stdio.h>
#include <stdlib.h>

typedef struct reg celula;
struct reg
{
    int conteudo;
    celula *proximo;
};

void insereElemento(int *valor, celula *p);
int estaContido(int x, celula *p);
int isSubset(celula *a, celula *b);

int main(void)
{
    celula *lista1, *lista2;
    int totalElementos, valor;

    lista1 = malloc(sizeof(celula));
    lista2 = malloc(sizeof(celula));

    // Inicializando a cabe�a das duas listas
    lista1->proximo = NULL;
    lista2->proximo = NULL;

    // Preenche a primeira lista;
    scanf("%d", &totalElementos);
    for (int i = 0; i < totalElementos; i++)
    {
        scanf("%d", &valor);
        insereElemento(&valor, lista1);
    }

    // Preenche a segunda lista
    scanf("%d", &totalElementos);
    for (int i = 0; i < totalElementos; i++)
    {
        scanf("%d", &valor);
        insereElemento(&valor, lista2);
    }

    printf("%d\n", isSubset(lista1, lista2)); // Mostra se � lista2 � subconjunto de lista1
    return EXIT_SUCCESS;
}

// dadoDado um ponteiro para um valor, o conteudo desse valor ser�
// adcionado no vetor apontado por p
void insereElemento(int *valor, celula *p)
{
    celula *nova;

    // Aloca mem�ria para o novo elemento
    nova = malloc(sizeof(celula));

    nova->conteudo = *valor;
    nova->proximo = p->proximo;
    p->proximo = nova;
}

// Dado os vetores A e B, verifica se B � subconjunto de A
int isSubset(celula *a, celula *b)
{

    for (celula *j = b->proximo; j != NULL; j = j->proximo)
    {
        if (!estaContido(j->conteudo, a)) // Se o valor n�o estiver contido ser� retornado false
        {
            return 0;
        }
    }
    return 1;
}

// Dado uma valor x e um vetor p, verifica se x est� em p;
int estaContido(int x, celula *p)
{
    for (celula *i = p->proximo; i != NULL; i = i->proximo)
    {
        if (x == i->conteudo)
        {
            return 1;
        }
    }
    return 0;
}
