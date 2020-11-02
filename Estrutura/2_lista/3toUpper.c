#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define LENGTH 100

/*DESCRIÇÃO:
------------
Você precisa ordenar nomes em uma agenda por ondem alfabética, um jeito simples de fazer isso, é passar todos os caracteres para maiúsculos ou minúsculos, para facilitar a comparação.
Escreva um programa, que dado um nome, passe ele para maiúsculo.

Formato de entrada:
Uma string de até 100 caracteres, contendo um nome

Formato de saída:
O nome em letras maiúsculas, seguido de uma quebra de linha.
*/
void toUpper(char *p);

int main(){
    char str[LENGTH]; // Define um vetor de caracteres
    fgets(str, LENGTH, stdin);
    toUpper(&str[0]);
    printf("%s", str);
    return 0;
}

void toUpper(char *p){
    int i = 0;
    // Itere enquanto não chegar ao fim do vetor
    while (p[i] != '\0' )
    {
        // Percorre o vetor verificando se é um char minúsculo e diferente de ' '. 
        //NOTA: Usando a tabela ASCII para fazer a conversão.
        if (p[i] != ' ' && !(p[i] >= 65 && p[i] <= 90)) {
            p[i] = (p[i] - 32);
        }

        i++;
    }
}