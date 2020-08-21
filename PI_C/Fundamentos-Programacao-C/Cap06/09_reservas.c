#include<stdio.h>
#define LENGTH 1

int voo[LENGTH];
int origem[LENGTH];
int destino[LENGTH];
int lugares[LENGTH];
int num_voo,resposta,resposta2, num_origem, num_destino;

int consultaPorDestino(int destino_voo){ // Função que consulta voo por destino;
    for (int i = 0; i < LENGTH; i++)
    {
        if(destino_voo == destino[i]){
            printf("\n");
            printf("+=+=+=+=+=+=+=+=+=+=+=+=+=\n");
            printf("Voo................= %d\n",voo[i]);
            printf("Origem............ = %d\n",origem[i]);
            printf("Destino........... = %d\n",destino[i]);
            printf("Lugares disponíveis= %d\n",lugares[i]);
            printf("+=+=+=+=+=+=+=+=+=+=+=+=+=\n\n");

        }else
        {
            printf("Não foi possível consultar, voo não existe!\n");
        }
        
    }
    
}

int consultaPorOrigem(int origem_voo){ // Função que consulta voo por origem;
    for (int i = 0; i < LENGTH; i++)
    {
        if(origem_voo == origem[i]){
            printf("\n");
            printf("+=+=+=+=+=+=+=+=+=+=+=+=+=\n");
            printf("Voo................= %d\n",voo[i]);
            printf("Origem............ = %d\n",origem[i]);
            printf("Destino........... = %d\n",destino[i]);
            printf("Lugares disponíveis= %d\n",lugares[i]);
            printf("+=+=+=+=+=+=+=+=+=+=+=+=+=\n\n");


        }else
        {
            printf("Não foi possível consultar, voo não existe!\n");
        }
        
    }
    
}

int consultaPorNumero(int num_voo){ // Função que consulta voo por número;
    for (int i = 0; i < LENGTH; i++)
    {
        if(num_voo == voo[i]){
            printf("\n");
            printf("+=+=+=+=+=+=+=+=+=+=+=+=+=\n");
            printf("Voo................= %d\n",voo[i]);
            printf("Origem............ = %d\n",origem[i]);
            printf("Destino........... = %d\n",destino[i]);
            printf("Lugares disponíveis= %d\n",lugares[i]);
            printf("+=+=+=+=+=+=+=+=+=+=+=+=+=\n\n");


        }else
        {
            printf("Não foi possível consultar, voo não existe!\n");
        }
        
    }
    
}

int reserva(int num_voo){ // Função que reserva voos;
    for (int i = 0; i < LENGTH; i++)
    {
        if(num_voo == voo[i]){ // Verifica se o voo existe;
            if (lugares[i]>0)
            {
                printf("Reserva confirmada!\n");
                lugares[i]--;
            }else{
                printf("Sem lugares para esse voo!\n");
            }
            
        }else{
            printf("Esse voo não existe!\n");
        }
    }
}

int main(void){
    // Ler o voo, origem, destino;
    for (int i = 0; i < LENGTH; i++)
    {
        printf("%dº Voo: \n",i+1);
        scanf("%d",&voo[i]);
        printf("Qual a origem? \n");
        scanf("%d",&origem[i]);
        printf("Qual o destino? \n");
        scanf("%d",&destino[i]);
        printf("Quantos lugares disponíveis? \n");
        scanf("%d",&lugares[i]);
    }
    do{
        printf("-----------MENU-----------\n");
        printf("1-Consultar\n");
        printf("2-Reservar\n");
        printf("3-Sair\n");
        printf("--------------------------\n");
        scanf("%d",&resposta);
        if (resposta == 1)
        {
           do
           {
                printf("---------Consultar--------\n");
                printf("1-Por número\n");
                printf("2-Por Origem\n");
                printf("3-Por destino\n");
                printf("--------------------------\n");
                scanf("%d", &resposta2);
                if (resposta2 == 1)
                {
                    printf("Digite o número do voo para consulta:\n");
                    scanf("%d",&num_voo);
                    consultaPorNumero(num_voo);
                }
                if(resposta2 == 2){
                    printf("Digite a origem do voo para consulta:\n");
                    scanf("%d",&num_origem);
                    consultaPorOrigem(num_origem);
                }
                if(resposta2 == 3){
                    printf("Digite o destino do voo para consulta:\n");
                    scanf("%d",&num_destino);
                    consultaPorDestino(num_destino);
                }
                
                
           } while (resposta2 < 1 || resposta2>3);
            
        }else if(resposta == 2){
            printf("Qual o número do voo que você pretende viajar? \n");
            scanf("%d",&num_voo);

            reserva(num_voo); // Verificar essa função!

        }else if(resposta == 3){
            printf("\n\n");
            printf("***Obrigado pela sua preferência!***\n");
            break;
        }
        
    }while((resposta<1 || resposta>3)||resposta !=3 );
    
} 