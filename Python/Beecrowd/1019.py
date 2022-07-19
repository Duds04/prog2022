N = int(input())
horas = 0
minutos = 0
segundos = 0

if((N//3600)!=0):
    horas = N//3600
    N -= horas * 3600
if(N//60!=0):
    minutos = N//60
    N -= minutos * 60

segundos = N

print(f"{horas}:{minutos}:{segundos}")
