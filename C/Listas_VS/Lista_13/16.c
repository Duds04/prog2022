#include <stdio.h>
#include <stdlib.h>
#include <math.h>
float calcula(double n1, char operacao, double n2);

int main(){
    float n1, n2;
    char operacao;

    printf("Escreva: ");
    scanf("%f%c%f", &n1, &operacao, &n2);
    printf("\nResultado: %f", calcula(n1, operacao, n2));

    return 0;
}

float calcula(double n1, char operacao, double n2){
    if(operacao == '/'){
        return (n1/n2);
    } else if(operacao == '-'){
        return (n1-n2);
    } else if(operacao == '+'){
        printf("Entrou: %d", (n1+n2));
        return (n1+n2);
    } else if(operacao == '*'){
        return (n1*n2);
    } 
    return -1;
}