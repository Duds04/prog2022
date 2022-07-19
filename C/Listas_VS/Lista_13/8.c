#include <stdio.h>
#include <stdlib.h>
#include <math.h>
float converteP(float medida);
float converteM(float medida);

int main(){
    float medida;

    printf("Escreva: ");
    scanf("%f", &medida);
    printf("\nResultado: %f\'%f\"", converteP(medida),converteM(medida));

    return 0;
}


float converteP(float medida){
    float convertido;
    convertido = medida/12;
    return convertido;
}

float converteM(float medida){
    float convertido;
    convertido = medida/39.37;
    return convertido;
}