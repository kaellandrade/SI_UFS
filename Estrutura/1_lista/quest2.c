#include <stdio.h>
#include <math.h>

void imprimeTriangulo(int n){
    int j = n;
    while (j != 0){
        for (int i = 1; i <= j; i++){
            printf("%d", j);
            if (i != j) printf("-");    
        }
        printf("\n");
        j--;
    }
    printf("\n");
}

int main(){
    int n;
    scanf("%d", &n);
    imprimeTriangulo(n);

    return 0;
}