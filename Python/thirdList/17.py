# 17

for i in range(0,50):
    if(i==0):
        anterior = 1
        S = anterior/1
    else:
        S += anterior/i+1
    anterior = anterior + 2

print(f"A soma deu = {S}")
