#include<stdio.h>
int epar(int num){ // Verifica se é par.
    if (num % 2 == 0){
        return 1;
    }else{
        return 0;
    }
    
}

int eprimo(int num){
    int cont = 0;
    for (int i = 1; i <= num; i++){
        if (num%i==0){
            cont++;
        }
        if (cont > 2){
            break;
        }
    }
    if(cont == 2){
        return 1;
    }else{
        return 0;
    }
    
}

int main(void){
    #define TOTALNUMEROS 3
    int soma_par, soma_primo, num;
    soma_par = 0;
    soma_primo=0;

    for (int i = 1; i <= TOTALNUMEROS; i++){
        printf("Digite um valor positivo:\n");
        scanf("%d",&num);
        if(eprimo(num)){
            soma_primo += num;
        }

        if(epar(num)){
            soma_par += num;
        }
    }
    printf("Soma dos pares  = %d\n",soma_par);
    printf("Soma dos primos = %d\n",soma_primo);

    
}