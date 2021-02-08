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
// Funções de impressão;
void visita_erd(arvore arv);
void visita_red(arvore arv);
void visita_edr(arvore arv);
void visita_dre(arvore arv);

// Funções de preenchimento
arvore insere(int valor);
arvore lerArvoreRED(arvore raiz);
// arvore encontraPai(arvore arv);


// altura e profundidade
int altura(arvore arv);
int qtd_folhas(arvore arv);
boolean verificaNivel(arvore arv, int nivel, int *nivelFolha);
boolean checa(arvore arv);

// Primeiro e último nó varredura e-r-d
arvore primeiroNo(arvore arv);
arvore ultimoNo(arvore arv);

int totaldeNOS = 0;
int main()
{
    arvore minha_arvore = NULL;
    minha_arvore = lerArvoreRED(minha_arvore);
    // minha_arvore = encontraPai(minha_arvore);

    printf("Varredura E-R-D: ");
    visita_erd(minha_arvore);

    printf("\nAltura da árvore: %d\n", altura(minha_arvore));
    printf("\nFolhas QTD: %d\n", qtd_folhas(minha_arvore));

    printf("Folhas no mesmo nível: %d", checa(minha_arvore));

    printf("\nÚltimo nó: %d", ultimoNo(minha_arvore)->conteudo);

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
        printf("%d, ", arv->conteudo);
        visita_erd(arv->dir);
    }
}

/**
 * Varredura R-E-D ou  preorder traversal, varredura prefixa, pré-fixa
 * VISITA
 * 1. a raiz,
 * 2. a subárvore esquerda da raiz, em preorder r-e-d,
 * 3. subárvore direita da raiz, em preorder r-e-d, 
*/
void visita_red(arvore arv)
{
    if (arv != NULL)
    {
        visita_erd(arv->esq);
        printf("%d", arv->conteudo);
        visita_erd(arv->dir);
    }
}

/**
 * Varredura postorder traversal, ou varredura em pós-ordem, ou varredura posfixa.
 * VISITA
 * 1. a subárvore esquerda da raiz, em pós-ordem e-d-r,
 * 2. subárvore direita da raiz, em pós-ordem e-d-r, 
 * 3. a raiz,
*/
void visita_edr(arvore arv)
{
    if (arv != NULL)
    {
        visita_erd(arv->esq);
        printf("%d", arv->conteudo);
        visita_erd(arv->dir);
    }
}
/**
 * Varredura D-E-R
 * VISITA
 * 1. a subárvore direita da raiz, em ordem d-e-r, 
 * 2. a raiz,
 * 3. a subárvore esquerda da raiz, em ordem e-r-d,
 * IMPRIME OS VALOES ORDEM DECRESCENTE CASO SEJA UMA ARVORE BINÁRIA DE BUSCA. 
*/
void visita_dre(arvore arv)
{
    if (arv != NULL)
    {
        visita_dre(arv->dir);
        printf("%d, ", arv->conteudo);
        visita_dre(arv->esq);
    }
}

int altura(arvore arv)
{
    if (arv == NULL)
    {
        return -1; // altura da arvore vazia
    }
    else
    {
        int he = altura(arv->esq);
        int hd = altura(arv->dir);
        if (he < hd)
            return hd + 1;
        else
            return he + 1;
    }
}

int qtd_folhas(arvore arv)
{
    if (arv == NULL)
        return 0;

    else if (arv->esq == NULL && arv->dir == NULL) // encontrou uma folha
        return 1;

    else
        return qtd_folhas(arv->esq) + qtd_folhas(arv->dir);
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

/**
 * Dada uma árvore será mostrado seu primeiro nó. Considerando a varredura E-R-D
*/
arvore primeiroNo(arvore arv)
{
    if (arv->esq == NULL)
        return arv;
    else
        return primeiroNo(arv->esq);
}

/**
 * Dada uma árvore será mostrado seu último nó. Considerando a varredura E-R-D
*/
arvore ultimoNo(arvore arv)
{
    if (arv->dir == NULL)
        return arv;
    else
        return ultimoNo(arv->dir);
}