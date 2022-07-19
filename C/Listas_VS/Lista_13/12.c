#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int converte(int num);
//int menor(int n1, int n2, int n3);

int main(){
    int num;

    printf("Escreva: ");
    scanf("%d", &num);
    //printf("\nResultado: %lf", converte(num));
    converte(num);

    return 0;
}

int converte(int num){
    int t50, t20, t10, t5, t2, t1;
    t50 = 0;
    t20 = 0;
    t10 = 0;
    t5 = 0;
    t2 = 0;
    t1 = 0;

    while(num/50!=0){
        printf("1");
        num -= 50;
        t50++;
    }while(num/20!=0){
        printf("2");
        num -= 20;
        t20++;
    }while(num/10!=0){
        printf("3");
        num -= 10;
        t10++;
    }while(num/5!=0){
        printf("4");
        num -= 5;
        t5++;
    }while(num/2!=0){
        printf("5");
        num -= 2;
        t2++;
    }
    t1 = num;

    printf("\nResults: \n%d\n%d\n%d\n%d\n%d\n%d", t50, t20, t10, t5, t2, t1);
    return 0;
}