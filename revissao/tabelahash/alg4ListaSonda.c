/**
 * 
*/
#include<stdlib.h>
#include<stdio.h>

typedef struct reg celula;
typedef celula *tabelaHash4;
#define M 10
struct reg
{
    int chave, ocorr;
};

tabelaHash4 tabela;


int contabiliza (int ch);
int hash(int ch, int m);
void imprimirTabela(tabelaHash4 tabela);
void inicializa(tabelaHash4 tabela);

tabelaHash4 tabela;
int main() {

    tabela = malloc(M * sizeof(celula));
    inicializa(tabela);

    contabiliza(333);
    contabiliza(336);
    contabiliza(1333);
    contabiliza(333);
    contabiliza(7777);
    contabiliza(446);
    contabiliza(556);
    contabiliza(999);



    imprimirTabela(tabela);
    return 0;
}


int contabiliza (int ch) {
   int c, sonda, h;
   h = hash (ch, M);
   for (sonda = 0; sonda < M; sonda++) {
      c = tabela[h].chave;
      if (c == -1 || c == ch) break;
      h = (h + 1) % M;
   }
   if (sonda >= M) 
      return EXIT_FAILURE;
   if (c == -1) 
      tabela[h].chave = ch;
   tabela[h].ocorr++;
   
   return EXIT_SUCCESS;
}

int hash(int ch, int m){
    return (ch % m);
}

void imprimirTabela(tabelaHash4 tabela){
    for (int i = 0; i < M; i++)
        printf("{%4d} = %d\n", tabela[i].chave,tabela[i].ocorr);
}

void inicializa(tabelaHash4 tabela){
    for (int i = 0; i < M; i++){
        tabela[i].chave = -1;
        tabela[i].ocorr = 0;
    }
}