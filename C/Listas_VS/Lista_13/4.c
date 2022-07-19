#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int inverte(char num[]);

int main(){
    char num[4]; 
    printf("Escreva: ");
    scanf("%s", &num);
    printf("%d ", inverte(num));
   
    return 0;
}

int inverte(char num[]){
    char invertido[3];
    for (int i = 2; i >= 0; i=i-1)
    {
        invertido[(2-i)] = num[i];
    }

    int aux = atoi(invertido);
    return aux;
}
 