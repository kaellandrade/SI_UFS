#include<stdio.h>
// 1, 2, 3, 
// 4, 5, 6
// 1, 4, 2, 5, 3, 6

// imprime um vetor v com seu respectivo tamanho
int imprimeVetor(int v[], int tamanho){
    for(int i = 0; i < tamanho; i++){
        printf("%d\n", v[i]);
    }
}

int main() {
    int len;
    scanf("%d", &len);
    int p[len];
    int q[len];
    int pq[len*2];

    int k = 0;
    int i = 0;
    int j = 0;


    // ler p
    for (int i = 0; i < len; i++){
        scanf("%d", &p[i]);
    }
    // ler q
    for (int i = 0; i < len; i++){
        scanf("%d", &q[i]);
    }

    while (k < len*2){
        pq[k] = p[i];
        pq[k+1] = q[j];
        k+=2;
        j++;
        i++;
    }
    

    imprimeVetor(pq, len*2);

}