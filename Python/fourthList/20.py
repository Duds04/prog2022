massa = float(input())
segundos = 0
while(m>0.10):
    m=(m*0.75)
    segundos+=30

horas = segundos//3600
minutos=(segundos%3600)//60
segundos=(segundos%3600)%60

print(f"Tempo:{horas}:{minutos}:{segundos}")
