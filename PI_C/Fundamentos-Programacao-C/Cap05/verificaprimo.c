#include<stdio.h>
int main(void){
    int contadivisores = 0;
    int num;
    printf("Digite um valor\n");
    scanf("%d",&num);
    for(int i=1; i <= num; i++){
        if(num % i==0){
            contadivisores++;
        }
        if (contadivisores > 2){
            break;
        }
        
    }
    if(contadivisores == 2){
        printf("%d é primo.\n",num);
    } else{
        printf("%d não é primo.\n", num);
    }
}