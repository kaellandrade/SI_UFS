#include <stdio.h>
#include <stdlib.h>
#define LENGTH 5
/*DESCRIÇÃO
------------
Ambrosio e seus quatro amigos (Peu, Minerin, Entidade e Jeff) almoçam todos os dias no Restaurante Universitário, 
mas odeiam pegar filas, no RU você pode pegar duas filas: A de ir comprar a comida e a de levar as bandejas após comer. 
Da primeira é impossível se livrar, já da segunda não, existe a possibilidade de uma  pessoa levar todas as bandejas da 
mesa (um amigo levar as bandejas de todos os outros), pensando nisso Ambrosio chegou a uma solução para decidir quem deveria levar a bandeja de todos:

Na segunda-feira é o primeiro dia que eles vão para o RU, nesse dia será marcado o tempo que cada amigo acabou de comer, feito isso, aquele que teve
o menor tempo não vai levar as bandejas mais nenhum dia naquela semana, o segundo menor tempo levará na terça-feira, o terceiro na quarta-feira e assim sucessivamente, 
para facilitar o seu trabalho e evitar contestações Ambrosio pediu para que você criasse um programa que dado o tempo que cada integrante do seu grupo de amigos (incluindo ele) terminou de comer na segunda-feira e exibisse a ordem que deveria ser seguida naquela semana.

Obs: o tempo de entrada sempre é lido na seguinte ordem: Ambrosio, Peu, Minerin, Entidade, Jeff.

Formato de entrada:
A entrada é formada por 5 números inteiros representando o tempo que cada amigo terminou de comer na segunda-feira (tempo do i-ésimo amigo é sempre menor igual a 120).

Formato de saída:
Na saída você deve apresentar o dia da semana, seguido de dois pontos, espaço e o nome do amigo que levará as bandejas 
nesse dia, por exemplo:

Terca-feira: Ambrosio
Quarta-feira: Peu
Quinta-feira: Minerin
Sexta-feira: Entidade

Exemplo entrada:
69 86 10 29 34

Exemplo Saída:
Terca-feira: Entidade
Quarta-feira: Jeff
Quinta-feira: Ambrosio
Sexta-feira: Peu

*/

void quemLevaBandeja(int *a, int *p, int *m, int *e, int *j, int *vet);
void imprimeDia(int *dia);
void troca(int *x, int *y);
void ordenaVetor(int *vet);

int main(void)
{
    int ambrosio, peru, minerim, entidade, jef, vet[LENGTH];
    for (int i = 0; i < LENGTH; i++)
    {
        scanf("%d", &vet[i]);
    }
    // Armazena os valores de cada aluno, pois o vetor será ordenado.
    ambrosio = vet[0];
    peru = vet[1];
    minerim = vet[2];
    entidade = vet[3];
    jef = vet[4];
    ordenaVetor(vet); // ordena o vetor;
    quemLevaBandeja(&ambrosio, &peru, &minerim, &entidade, &jef, &vet[0]);
    return EXIT_SUCCESS;
}
void quemLevaBandeja(int *a, int *p, int *m, int *e, int *j, int *vet)
{
    int valueAtual;
    // percorre os dias de levar a bandeja, T, Q, Q e S
    for (int i = 1; i < LENGTH; i++)
    {
        valueAtual = vet[i];
        imprimeDia(&i); // dia i i[1] = terça, i[2] = quarta ... i[4] = sexta

        if (*a == valueAtual)  // Verifica se o valor de vet[i] corresponde ao valor entrado por Ambrosio
        {
            printf("Ambrosio");
        }
        else if (*p == valueAtual) // Verifica se o valor de vet[i] corresponde ao valor entrado por Peu
        {
            printf("Peu");
        }
        
        else if (*m == valueAtual) // Verifica se o valor de vet[i] corresponde ao valor entrado por Minerin
        {
            printf("Minerin");
        }
        else if (*e == valueAtual)
        {
            printf("Entidade"); // Verifica se o valor de vet[i] corresponde ao valor entrado por Entidade
        }
        else
        {
            printf("Jeff");
        }
        printf("\n");
    }
}

// Dado um número x, será impresso o dia da semana correspondente a x.
// Ex: 0 = segunda, 1 = terça ... 4 = sexta (neste caso, segunda fica de fora);
void imprimeDia(int *dia)
{
    if (*dia == 1)
        printf("Terca-feira: ");
    if (*dia == 2)
        printf("Quarta-feira: ");
    if (*dia == 3)
        printf("Quinta-feira: ");
    if (*dia == 4)
        printf("Sexta-feira: ");
}

// Dado um valor x e y. x=y e y=x
void troca(int *x, int *y)
{
    int aux;
    aux = *x;
    *x = *y;
    *y = aux;
}

// Ordena um dado vetor passado por referência
void ordenaVetor(int *vet)
{
    for (int i = 0; i < LENGTH; i++)
    {
        for (int j = 0; j < LENGTH - 1; j++)
        {
            if (vet[j] > vet[j + 1])
            {
                troca(&vet[j], &vet[j + 1]);
            }
        }
    }
}
