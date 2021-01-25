/*
NÍVEL: Iniciante
Descrição
---------

Pilha é uma estrutura de dados linear capaz de armazenar uma coleção de elementos que somente 
são acessados a partir do seu lado superior, denominado topo. Assim, os elementos da pilha são manipulados, 
sempre, pelo topo da pilha.
Considerando uma estrutura de dados do tipo Pilha, então, implemente as seguintes operações:

Empilhar: essa operação adiciona um novo elemento da pilha, ela receberá o valor do novo elemento como parâmetro.

Desempilhar: essa operação remove o elemento que está no topo da pilha.

Imprimir: essa operação imprime o valor de todos os elementos presentes na pilha, a impressão deve começar a partir do topo.

A última linha da entrada contém o seguinte texto Finalizar

Formato de entrada
------------------
A entrada será composta por várias linhas, sendo que em cada linha haverá um comando.
Os comandos possíveis são:

1. Empilhar
    Esse comando será seguido pelo valor do novo elemento que está sendo adicionado na pilha.

2. Desempilhar
    Esse comando remove o elemento que está no topo da pilha. 

3. Imprimir
    Esse comando imprime o valor de todos elementos presentes na pilha, a impressão deve ser feita em uma mesma linha, 
    separando os valores por espaço.

4. Finalizar
    Esse indica a última linha da entrada



Formato de saída
----------------
Cada linha da saída terá o resultado de um comando Imprimir.
Considerando a seguinte entrada:

Empilhar 4
Empilhar 5
Imprimir
Empilhar 2
Imprimir
Desempilhar
Imprimir
Empilhar 8
Empilhar 12
Imprimir
Finalizar

A Saída seria:
5 4
2 5 4
5 4
12 8 5 4

Observe que, na entrada, o comando Imprimir apareceu quatro vezes, e por isso a saída tem quatro linhas.

*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct reg celula;

struct reg
{
    int conteudo;
    celula *proximo;
};

void empilhar(int *p_valor);
void desempilhar(void);
void imprimir(celula *p);

celula *pilha;

int main(void)
{
    char string[11]; // Apenas para armazenar os comando Empilhar, Desempilhar, Imprimir e Finalizar
    int valor;
    // Inicializa a cabeca da pilha;
    pilha = malloc(sizeof(celula));
    pilha->proximo = NULL;

    do
    {
        scanf("%s", string);

        if (strcmp(string, "Empilhar") == 0)
        {
            scanf("%d", &valor);
            empilhar(&valor);
        }

        if (strcmp(string, "Desempilhar") == 0)
            desempilhar();

        if (strcmp(string, "Imprimir") == 0)
        {
            imprimir(pilha->proximo);
            printf("\n");
        }

    } while (!(strcmp(string, "Finalizar") == 0));

    return EXIT_SUCCESS;
}

void empilhar(int *p_valor)
{
    celula *nova;
    nova = malloc(sizeof(celula));

    nova->conteudo = *p_valor;
    nova->proximo = pilha->proximo;
    pilha->proximo = nova;
}

void imprimir(celula *p)
{
    if (p != NULL)
    {
        printf("%d", p->conteudo);
        if (p->proximo != NULL)
            printf(" "); // Evita espa?o em branco no final
        imprimir(p->proximo);
    }
}

void desempilhar(void)
{
    int remov;
    celula *lixo;
    lixo = pilha->proximo;
    remov = lixo->conteudo; // guarda o valor removido, caso fosse necess?rio retorn?-lo
    pilha->proximo = lixo->proximo;
    free(lixo);
}