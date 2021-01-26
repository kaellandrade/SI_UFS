#include <stdio.h>
#define LENGTH 15
#define VETLENGTH 5
/*DESCRIÇÃO
-----------
Tacógrafos são dispositivos instalados em determinados tipos de veículos, que registram a velocidade, tempo e
distância percorrida por tal veículo. São utilizados principalmente em veículos de transporte coletivo e de transporte
de cargas, assim ajudando a evitar abusos de velocidade por parte dos motoristas.

A empresa SBC (Sociedade Brasileira dos Caminhoneiros) decidiu encomendar uma versão um pouco mais
básica (e barata) para seus associados não precisarem gastar tanto na instalação desses aparelhos. Essas versões
modificadas registram apenas os intervalos de tempo e as velocidades médias do caminhão naqueles intervalos.

Apesar das restrições dos aparelhos novos, a SBC quer poder saber qual foi a distância percorrida pelos caminh
ões. Você deverá escrever um programa que recebe uma série de intervalos de tempo com suas respectivas
velocidades médias e calcula qual foi a distância total percorrida pelo caminhão de acordo com o tacógrafo.


Formato de entrada:
A primeira linha da entrada contém um inteiro N (1 <= N <= 1000) representando a quantidade de intervalos
de tempo registrados no tacógrafo. As N linhas seguintes descrevem os intervalos de tempo. Cada uma dessas
linhas possui dois inteiros T e V (1 <= T <= 100, 0 <= V <= 120), que representam, respectivamente o tempo
decorrido (em horas) e a velocidade média (em quilômetros por hora) no intervalo de tempo.


Formato de saída:
Seu programa deve imprimir uma única linha, contendo um único número inteiro representando a distância
total percorrida, em quilômetros.

*/
int calcVel(int *tempoH, int *km_por_horas);
void imprimeTotalPercorrido(int *totalDistancia);


int main (){
    int qtIntervalos, totDistancia, tempo, km, *p_intervalos, *p_totalDistancia, *p_tempo, *p_km;
    p_intervalos = &qtIntervalos;
    p_totalDistancia = &totDistancia;
    p_tempo = &tempo;
    p_km = &km;
    *p_totalDistancia = 0;

    scanf("%d", p_intervalos);

    while (*p_intervalos > 0){
        scanf("%d %d", p_tempo, p_km);
        // Acumulador da distância percorrida
        *p_totalDistancia += calcVel(p_tempo, p_km); 
        (*p_intervalos) --;
    }
    // Mostra o valor contido no acumulador p_totalDistancia
    imprimeTotalPercorrido(p_totalDistancia);
    
}
// dado um tempo(H) e uma velocidade(KM/H), será calculada a velocidade
int calcVel(int *tempoH, int *km_por_horas){
    return (*tempoH) * (*km_por_horas);
}


void imprimeTotalPercorrido(int *totalDistancia){
    printf("%d\n", *totalDistancia);
}