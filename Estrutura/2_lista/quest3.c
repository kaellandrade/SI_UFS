#include <stdio.h>
/*DESCRIÇÃO:
------------
Crie um programa que tenha apenas uma função, além do programa principal, 
que receberá como parâmetros três números naturais i, f e x e que deverá mostrar todos os valores múltiplos de x no intervalo [i, f]. 
O PROGRAMA PRINCIPAL deverá ler os valores e a FUNÇÃO deverá exibir os múltiplos.

Formato de entrada:
10
20
5

Formato de saída:
10
15
20
*/
void exibeMultiplos(int *start, int *finish, int *x);

int main() {
    int i;
    int f;
    int x;
    scanf("%d %d %d", &i, &f, &x);
    exibeMultiplos(&i, &f, &x);
}

void exibeMultiplos(int *start, int *finish, int *x) {
    while ((*start) <= (*finish)) {
        if ((*start) % (*x) == 0)
        {
            printf("%d\n", *start);
        }
        (*start)++;
    }
}
