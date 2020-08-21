#include <stdio.h> // standard I/O
#include<stdlib.h>
#include<time.h>
/*
    O computador irá gerar um número aleatório entre uma determinada faixa.
    O jogador terá algumas tentativas para chutar esse valor. De acordo com 
    o chute do jogador o computador mostrará pistas.
    
*/
#define FACIL 20
#define MEDIO 15
#define DIFICIL 6
#define PONTOS_INICIAIS 1000
int start; // Flag que controla a execução do jogo;
int upper,lower;
int ultimochute;
int main()
{
    do{
        printf("**********************************\n");
        printf("*Bem-vindo ao Jogo de Adivinhação*\n");
        printf("**********************************\n");
        srand(time(0)); // Semente
        // Como rand gera um número grande pegamos o resto da divisão por 100. [lower, upper]
        printf("Digite o intervalo para gerar o número aleatório [a,b]: \n");
        
        do{
        	scanf("%d %d", &lower,&upper);      
        	if(lower < 0){	
	        	printf("Número negativo não é permitido\nDigite Novamente\n");
        	}
        	
        }while(lower < 0); // Não é permitido número negativo
        	
        int numerosecreto = (rand()%(upper - lower + 1)+lower);
        // printf("%d\n", numerosecreto);

        int chute;
        double pontos = PONTOS_INICIAIS;
        int nivel, totaltentativas;
        printf("Qual o nível de dificuldade?\n");
        printf("(1) Fácil (2) Médio (3) Difícil\n\n");
        printf("Escolha: ");
        scanf("%d", &nivel);

        switch (nivel)
        {
        case 1:
            totaltentativas = FACIL;
            break;
        case 2:
            totaltentativas = MEDIO;
            break;
        case 3:
            totaltentativas = DIFICIL;
        default:
            totaltentativas = DIFICIL;
            break;
        }
        
        for( int i = 1; i <= totaltentativas; i++)
        {  
            printf("Tentativa %d de %d\n",i, totaltentativas);
            printf("Qual é o seu chute? \n");
            scanf("%d",&chute);
            int acertou = chute == numerosecreto; // Flag que define se acertou ou não. 1(True) ou 0(False) 
            int maior = chute > numerosecreto;    // Flag para verificar se é maior ou menor.
            
            // Não permite repetir números anteriores.
            if(ultimochute == chute){
                printf("Você já jogou esse número!");
                i--;
                continue;
            }

            if (chute < 0){
                printf("Não é permitido chutar número negativos!\n");
                i--;
                continue;
            }
            if (i != totaltentativas){
                double pontosperdidos = abs(chute - numerosecreto) / 2.0;
                pontos -= pontosperdidos;
                if (acertou)
                {
                    printf("Parabéns! Você acertou!\n");
                    printf("Você fez %.2f pontos\n", pontos);
                    break;
                } else if(maior){
                    printf("Seu chute foi alto!\n");
                }else{
                    printf("Seu chute foi baixo!\n");
                }
                ultimochute = chute; // Guarda o último chute
            } else{
                printf("Você perdeu, tente novamente!");
            }
        
        }
        printf("Deseja jogar novamente 1[SIM] 0[NÃO]?\n");
        scanf("%d",&start);
    }while(start == 1);
    printf("Obrigado por jogar!\n");
    return 0;
}
