#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void ordena(int* vetor, int n);
void printarVetor(int v[], int n);

int main(){
    int n = 5;
    //vetor já é um ponteiro
    int v[n];
     
    for(int i=0; i<n; i++){
        printf("\nEscreva: ");
        scanf("%d", &v[i]);
    }

    printf("Print antes: ");
    printarVetor(v, n);

    ordena(v, n);
    printf("Print depois: ");
    printarVetor(v, n);

    return 0;
}

void printarVetor(int v[], int n){
    for(int i=0; i<n; i++){
        printf("%d ", v[i]);
    }
    printf("\n");
}

void ordena(int* vetor, int n){
    int guarda;
    guarda = 0; 
    for (int i = 0; i <= n; i++){
        for (int j = 0; j <= (n-1)-i; j++) 
        /* a cada repeticao ele vai ate o final menos 1, pq ele percorre tudo deixa o menor no final, 
        depois faz isso dnv mas sem considerar o menor que já está no final*/
        {
            if (vetor[j] > vetor[j + 1])
            {
                guarda = vetor[j];
                vetor[j] = vetor[j + 1];
                vetor[j + 1] = guarda;
            }
        }
    }
    printf("\nDurante: ");
    printarVetor(vetor, n);
}
