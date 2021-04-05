#include <stdio.h>
/**
 * Ler dois números e informar o maior;
*/
int max(int x, int y);

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    printf("O maior é: %d\n", max(a, b));
    return 0;
}

int max(int x, int y)
{
    return (x >= y) ? x : y;
}