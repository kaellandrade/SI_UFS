#include<stdio.h>
#include<stdlib.h>

int main()
{
    int a,b,c,n;
    a = 0;
    b = 1;
    printf("Digite o números de termos: \n");
    scanf("%d",&n);
    if (n == 0)
    {
        printf("0\n");
    } else if(n==1){
        printf("1\n");
    } else if(n==2){
        printf("1, 1\n");
    } else{
        printf("1, ");
        for (int i = 2; i <= n; i++){  
            c = a + b;
            printf("%d, ",c);
            a = b;
            b = c;
        }
        printf("\n");
    }
}
