#include <stdio.h>
#include <math.h>
#include <stdlib.h>
float calculaMedia(float m1, float m2, float m3);

int main(){
    float m1, m2, m3;

    printf("Escreva: ");
    scanf("%f %f %f", &m1, &m2, &m3);
    printf("\nResult: %.2f", calculaMedia(m1, m2, m3));

    return 0;
}


float calculaMedia(float m1, float m2, float m3){
    float media = 0;
    //printf("%f %f %f", m1, m2, m3);
    media = (m1 + m2 + m3)/3;

    return media;
}