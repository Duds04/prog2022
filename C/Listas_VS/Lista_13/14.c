#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int converte(int hora,int min,int segundo);

int main(){
    int hora, min, segundo;

    printf("Escreva: ");
    scanf("%d %d %d", &hora, &min, &segundo);
    printf("\nResultado: %d", converte(hora, min, segundo));

    return 0;
}

int converte(int hora,int min,int segundo){
    int ch, cm, soma;
    soma = 0;
    ch = 0;
    cm = 0;
    soma = 0;
    
    ch = (hora*60)*60;
    cm = (min*60);
    soma = segundo +ch +cm;

    return soma;
}