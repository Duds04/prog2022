#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void soma(float n1,float n2,float n3,float n4,float n5);

int main(){
    float n1, n2, n3, n4, n5;

    printf("Escreva: ");
    scanf("%f %f %f %f %f", &n1, &n2, &n3, &n4, &n5);
    soma(n1, n2, n3, n4, n5);

    return 0;
}

void soma(float n1,float n2,float n3,float n4,float n5){
    float soma;
    soma =  n1+ n2+ n3+ n4+ n5;
    if(soma<60.0){
        printf("Reprovado");
    }else{
        printf("Aprovado");
    }
}