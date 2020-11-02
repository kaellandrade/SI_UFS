#include <stdio.h>
#define LENGTH 4
/*DESCRIÇÃO
-----------
Ambrosina é uma fotógrafa muito peculiar. Ela só aceita tirar fotos de pessoas se as pessoas estiverem em grupos de exatamente 04 pessoas.
Tudo isso porque Ambrosina tem uma mania esquisita de ordenação. 
Para ela, a pessoa mais baixa deve ficar sempre do lado esquerdo, a segunda mais baixa do lado direito, no meio, logo após a mais baixa, fica a terceira mais baixa e em seguida a mais alta.
Abaixo segue uma ilustração de uma foto tirada por Ambrosina:
https://thehuxley.com/api/v1/problems/image/c2aa8c3c42c4cb0edf47085370bdb55717875202a.png



Formato de entrada:
A entrada consiste de 04 números reais maiores que zero correspondendo às alturas de 04 pessoas. 
Cada número é dado em uma linha diferente. A entrada pode não estar ordenada.



Formato de saída:
Consiste de 04 números reais, separados por um final de linha, ordenados de acordo com a mania de Ambrosina. 
Os números devem ser formatados com 02 casas decimais.

Exemplo entrada:
40
30
20
10

Exemplo Saída:
10.00
30.00
40.00
20.00
*/
void ordena(float *vet);
void troca(float *x, float *y);
void imprimeArray(float *vet);
void mudaPosicao(float *vet);

void main(void)
{
    float valor, *p_valor;
    p_valor = &valor;

    float vetor[LENGTH];

    // Armazena 4 valores lidos no vetor
    for (int i = 0; i < LENGTH; i++)
    {
        scanf("%f", p_valor);
        vetor[i] = *p_valor;
    }

    ordena(vetor);      // Ordena os valroes de vetor
    mudaPosicao(vetor); // Desloca a segunda pessoa para última posição
    imprimeArray(vetor);
}

// Imprime um dado vetor passado por referência
void imprimeArray(float *vet)
{
    for (int i = 0; i < LENGTH; i++)
    {
        printf("%.2f\n", vet[i]);
    }
}

// Dado um valor x e y. x=y e y=x
void troca(float *x, float *y)
{
    float auxiliar;
    auxiliar = *x;
    *x = *y;
    *y = auxiliar;
}

// Ordena um dado vetor passado por referência
void ordena(float *vet)
{
    for (int i = 0; i < LENGTH; i++)
    {
        for (int j = 0; j < (LENGTH - 1); j++)
        {
            if (vet[j] > vet[j + 1])
            {
                troca(&vet[j], &vet[j + 1]);
            }
        }
    }
}

// Leva o segundo elemento de um vetor(passado por referência) para última posição
void mudaPosicao(float *vet)
{
    int i, *p_i;
    p_i = &i;
    *p_i = 1;
    while (*p_i != LENGTH - 1)
    {
        troca(&vet[*p_i], &vet[*p_i + 1]);
        (*p_i)++;
    }
}