#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int converteFC(int fahrenheit);
int converteFK(int fahrenheit);
int converteCF(int celsius);
int converteCK(int celsius);
int converteKF(int kelvin);
int converteKC(int kelvin);

int main(){
    int temperatura, imprima;
    printf("Escreva: ");
    scanf("%d", &temperatura);
    for(int i=1; i<=6;i++){
        switch(i){
            case 1:
                imprima = converteFC(temperatura);
                break;
            case 2:
                imprima = converteFK(temperatura);
                break;
            case 3:
                imprima = converteCF(temperatura);
                break;
            case 4:
                imprima = converteCK(temperatura);
                break;
            case 5:
                imprima = converteKF(temperatura);
                break;
            case 6:
                imprima = converteKC(temperatura);
                break;
            default:
                break;
        }
        printf("\nResult: %d\n", imprima);
    }  
}

int converteFC(int fahrenheit){
        return (int)((fahrenheit-32)/1.8);
}
int converteFK(int fahrenheit){
    return (int)(((fahrenheit-32)*(5/9))+273);
}
int converteCF(int celsius){
    return (int) ((1.8*celsius)+32);
}
int converteCK(int celsius){
    return (int)(celsius+273);
}
int converteKF(int kelvin){
    return (int)(((kelvin-273)*1.8)+32);
}
int converteKC(int kelvin){
    return (int)(kelvin-273);
}