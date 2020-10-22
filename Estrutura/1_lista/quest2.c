#include <stdio.h>
#include <math.h>

void imprimeTriangulo(int *p);

int main() {
    int n;
    scanf("%d", &n);
    imprimeTriangulo(&n);

    return 0;
}

void imprimeTriangulo(int *p) {
    int j = *p;
    while (j != 0)
    {
        for (int i = 1; i <= j; i++)
        {
            printf("%d", j);
            if (i != j)
                printf("-");
        }
        printf("\n");
        j--;
    }
    printf("\n");
}