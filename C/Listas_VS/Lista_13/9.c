#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int sinal(int num);

int main(){
    int num;

    printf("Escreva: ");
    scanf("%d", &num);
    //printf("\nResultado: %d", sinal(num));
    sinal(num);

    return 0;
}

int sinal(int num){
    
    if(num>0){
        printf("Positivo");
        return 1;
    }else{
        printf("Negativo");
        return 0;
    }
}