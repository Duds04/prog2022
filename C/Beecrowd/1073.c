#include <stdio.h>
#include <math.h>
void quadrado(int n);


int main(){
    int n1;
    scanf("%d", &n1);
    quadrado(n1);
    return 0;
}

void quadrado(int n){
    int quad;
    for(int i=2; i<=n; i+=2){
        quad = pow(i, 2);
        printf("%d^2 = %d\n", i, quad);
    }
    
}