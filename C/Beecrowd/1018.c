#include <stdio.h>
#include <math.h>
void cedulas(int entrada);


int main(){
    int entrada;
    scanf("%d", &entrada);

    cedulas(entrada);

    return 0;
}

void cedulas(int entrada){
    int n100, n50, n20, n10, n5, n2, n1, guarda;
    guarda = entrada;

        n100 = entrada/100;
        entrada-= n100*100;

        n50 = entrada/50;
        entrada-= n50*50;

        n20 = (entrada/20);
        entrada-= n20*20;

        n10 = (entrada/10);
        entrada-= n10*10;

        n5 = (entrada/5);
        entrada-= n5*5;

        n2 = (entrada/2);
        entrada-= n2*2;

    n1 = entrada;
    
    printf("%d\n",guarda);
    printf("%d nota(s) de R$ 100,00\n",n100);
    printf("%d nota(s) de R$ 50,00\n",n50);
    printf("%d nota(s) de R$ 20,00\n",n20);
    printf("%d nota(s) de R$ 10,00\n",n10);
    printf("%d nota(s) de R$ 5,00\n",n5);
    printf("%d nota(s) de R$ 2,00\n",n2);
    printf("%d nota(s) de R$ 1,00\n",n1);
}