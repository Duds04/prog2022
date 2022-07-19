#include <stdio.h>
#include <math.h>
int converte(int segundos);


int main(){
    int segundos;
    scanf("%d", &segundos);

    converte(segundos);


    return 0;
}

int converte(int segundos){
    int minutos, horas;

    horas = segundos/(60*60);
    segundos-= (60*60)*horas;
    // se for 0 ele inicializa com 0
    minutos = (segundos/60);
    segundos-= 60 * minutos;


    printf("%d:%d:%d\n", horas, minutos, segundos);
    return 0;
}