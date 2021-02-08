/*
NÍVEL: Médio
Tópicos: estrutura de dados, Árvore 

Descrição
---------
Em estrutura de dados, chama-se de Árvore Binária Completa de grau D uma árvore em que todos os nós (exceto as folhas) possuem dois filhos e todas as folhas estão no mesmo nível D, sendo D a altura da árvore.

Por exemplo:
(7(13(0()())(1()()))(11(2()())(9()())))
          7
         / \
        /   \
       /     \
      /       \
     13       11
    / \       /\
   /   \     /  \
  0     1   2    9

Esta árvore binária é completa de grau = 2 pois todos os nós possuem dois filhos (exceto as folhas), todas as folhas estão no mesmo nível e a altura da árvore é 2 (a altura na raíz é 0).

Sua tarefa é simples. Dada uma árvore binária em notação de parêntese, verifique se ela é completa ou não. Se for, informe o total de nós da árvore. Caso contrário, informe quais nós tem apenas um filho.

Formato de entrada
------------------

A entrada consiste de uma linha contendo a string da árvore em notação de parênteses.

Formato de saída
----------------

A saída consiste de duas linhas:
A primeira linha contém a mensagem "completa" caso a árvore binária seja completa e "nao completa", caso contrário.
Na segunda linha, deve-se exibir:
    Caso a árvore seja completa: a mensagem "total de nos: N" onde N é um inteiro representando o total de nós na árvore
    Caso a árvore não seja completa: a mensagem "nos com um filho: N1 N2 N3 ... Ni", onde cada Ni é o inteiro que representa o nó. (N1, N2, N3, ... , Ni estão in ordem).
Cada linha deve conter um caractere de quebra de linha no final
Observe que na impressão da lista de nós, todos os nós estão separados por um caractere de espaço exceto o último nó.
*/

#include <stdlib.h>
#include <stdio.h>
typedef struct reg noh;
typedef int boolean;
struct reg
{
  int conteudo;
  noh *esq;
  noh *dir;
};

typedef noh *arvore;
typedef arvore *vectArv; // vetor de árvore

// Funções de impressão;
void visita_erd(arvore arv);
void imprimeNosIncompletos();

// Funções de preenchimento
arvore insere(int valor);
arvore lerArvoreRED(arvore raiz);

// funções auxiliares
int verificacompleta();
void imprimeResultado();
boolean verificaNivel(arvore arv, int nivel, int *nivelFolha);
boolean checa(arvore arv);

int totaldeNOS = 0;
int i = 0;
vectArv subarVector; // armazena as subárvores incompletas em um vetor de árvores

arvore minha_arvore = NULL;
int main()
{
  minha_arvore = lerArvoreRED(minha_arvore);
  subarVector = malloc(sizeof(arvore *) * totaldeNOS);

  visita_erd(minha_arvore);
  imprimeResultado();

  printf("\n");
  return EXIT_SUCCESS;
}

arvore insere(int valor)
{
  arvore nova_subAr;
  nova_subAr = malloc(sizeof(arvore));
  nova_subAr->conteudo = valor;
  nova_subAr->dir = NULL;
  nova_subAr->esq = NULL;

  return nova_subAr;
}

/**
 * Varredura E-R-D ou  inorder traversal, imprimeos elementos em 
 * VISITA
 * 1. a subárvore esquerda da raiz, em ordem e-r-d,
 * 2. a raiz,
 * 3. a subárvore direita da raiz, em ordem e-r-d, 
 * IMPRIME OS VALOES ORDEM ASCENDENTE CASO SEJA UMA ARVORE BINÁRIA DE BUSCA. 
*/
void visita_erd(arvore arv)
{
  if (arv != NULL)
  {
    visita_erd(arv->esq);
    if ((!(arv->esq == NULL && arv->dir == NULL)))
    { // nós que não são folhas
      subarVector[i++] = arv;
    }
    visita_erd(arv->dir);
  }
}

arvore lerArvoreRED(arvore raiz)
{
  int valorNUM;
  char carac;

  scanf("%c", &carac);
  if (carac == ' ')
    scanf("%c", &carac);
  if (carac == '(')
  {
    if (scanf("%d", &valorNUM))
    {
      raiz = insere(valorNUM);
      totaldeNOS++;
    }
    else
    {
      scanf("%c", &carac);
      return raiz;
    }
    raiz->esq = lerArvoreRED(raiz->esq);
    raiz->dir = lerArvoreRED(raiz->dir);
    scanf("%c", &carac);
  }
  return raiz;
}

/**
 * Função recursiva que verifica se todas as folhas esetão no mesmo nível
 * ANALIZAR ESSA FUNÇÃO
*/
boolean verificaNivel(arvore arv, int nivel, int *nivelFolha)
{
  if (arv == NULL)
    return 1; // caso base

  // Se um nó folha for encontrado
  if (arv->esq == NULL && arv->dir == NULL)
  {
    //Quando um nó folha é encontrado pela primeira vez
    if (*nivelFolha == 0)
    {
      *nivelFolha = nivel; // Define o nível da primeira folha encontrada
      return 1;
    }

    // Se este não for o nó da primeira folha,
    // compare seu nível com o nível da primeira folha
    return (nivel == *nivelFolha);
  }

  // Se este nó não for folha, verifique recursivamente as subárvores esquerda e direita
  return verificaNivel(arv->esq, nivel + 1, nivelFolha) &&
         verificaNivel(arv->dir, nivel + 1, nivelFolha);
}

/**
 * Dada uma árvore verifica se todas as folhas estão no mesmo nível; 
*/
boolean checa(arvore arv)
{
  int nivel = 0, nivelFolha = 0;
  return verificaNivel(arv, nivel, &nivelFolha);
}

void imprimeNosIncompletos()
{
  for (int i = 0; subarVector[i] != NULL; i++)
  {
    if (subarVector[i]->dir == NULL || subarVector[i]->esq == NULL) // imprime apenas nos incompletos
      printf("%d ", subarVector[i]->conteudo);
  }
}
int verificacompleta()
{
  for (int i = 0; subarVector[i] != NULL; i++)
  {
    if (subarVector[i]->dir == NULL || subarVector[i]->esq == NULL) // Verifica se há 0 ou 1 filho
      return 0;
  }
  return 1;
}
void imprimeResultado()
{
  if (verificacompleta() && checa(minha_arvore))
  {
    printf("completa\ntotal de nos: %d", totaldeNOS);
  }
  else
  {
    printf("nao completa\nnos com um filho: ");imprimeNosIncompletos();
  }
}