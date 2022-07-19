N = int(input())
aux = N

nota100 = 0
nota20 = 0
nota50 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0

if((N//100)!=0):
    nota100 = N//100
    N -= nota100*100
if((N//50)!=0):
    nota50 = N//50
    N-= nota50*50
if((N//20)!=0):
    nota20 = N//20
    N -= nota20 * 20
if((N//10)!=0):
    nota10 = N // 10
    N -= nota10 * 10
if(N//5!=0):
    nota5 = N // 5
    N -= nota5 * 5
if (N // 2 != 0):
    nota2 = N // 2
    N -= nota2 * 2
if(N//1!=0):
    nota1 = N // 1


print(aux)
print(f"{nota100} nota(s) de R$ 100,00")
print(f"{nota50} nota(s) de R$ 50,00")
print(f"{nota20} nota(s) de R$ 20,00")
print(f"{nota10} nota(s) de R$ 10,00")
print(f"{nota5} nota(s) de R$ 5,00")
print(f"{nota2} nota(s) de R$ 2,00")
print(f"{nota1} nota(s) de R$ 1,00")