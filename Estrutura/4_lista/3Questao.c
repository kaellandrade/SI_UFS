#include <stdio.h>
#include <stdlib.h>

typedef struct reg celula;

struct reg
{
  int conteudo;
  celula *proximo;
};

celula *addFila(int *p_valor, celula *fi);
int tiraFila(celula *fi);
void imprimeFila(celula *fi);
void intercala(int *Pk, int *TAM1, int *TAM2, celula *c1, celula *c2);

celula *caixa1, *caixa2;

int main(void)
{
  // Inicializa a cabe�a da pilha;
  int lengFila1, lengFila2, k, valor;

  caixa1 = malloc(sizeof(celula));
  caixa2 = malloc(sizeof(celula));

  caixa1->proximo = caixa1;
  caixa2->proximo = caixa2;

  // Preenche a primeira fila
  scanf("%d", &lengFila1);
  scanf("%d", &lengFila2);
  scanf("%d", &k);
  // Preenche a primira fila
  while (lengFila1 > 0)
  {
    scanf("%d", &valor);
    caixa1 = addFila(&valor, caixa1);
    lengFila1--;
  }

  // Preenche a segunda fila
  while (lengFila2 > 0)
  {
    scanf("%d", &valor);
    caixa2 = addFila(&valor, caixa2);
    lengFila2--;
  }
  printf("\n\n");
  intercala(&k, &lengFila1, &lengFila2, caixa1, caixa2);

  return EXIT_SUCCESS;
}

// Devolve o endere�o da cabe�a da fila
celula *addFila(int *p_valor, celula *fi)
{
  celula *nova;
  nova = malloc(sizeof(celula));
  nova->proximo = fi->proximo;
  fi->proximo = nova;
  fi->conteudo = *p_valor;
  return nova;
}

int tiraFila(celula *fi)
{
  int valor;
  celula *p;
  p = fi->proximo;
  valor = p->conteudo;
  fi->proximo = p->proximo;
  free(p);
  return valor;
}

void imprimeFila(celula *fi)
{
  celula *p;
  p = fi->proximo;
  // printf("[Cabe�a]->");
  while (p != fi)
  {
    printf("%d\n", p->conteudo);
    p = p->proximo;
  }
}

void intercala(int *Pk, int *TAM1, int *TAM2, celula *c1, celula *c2)
{
  if (*Pk == 2)
  {
    for (int i = 0; i <= *TAM1; i++)
    {
      printf("%d\n", tiraFila(c1));
      printf("%d\n", tiraFila(c2));
    }
  }
  else
  {
    for (int i = 0; i <= *TAM2; i++)
    {
      printf("%d\n", tiraFila(c2));
      printf("%d\n", tiraFila(c1));
    }
  }

  imprimeFila(c1);
  imprimeFila(c2);
}