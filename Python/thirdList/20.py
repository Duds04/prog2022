# 20

x = int(input("Digite o valor de x: "))
S = 0

for i in range(25,0,-1):
    if (i % 2 == 0):
        S -= ((x) ** i) / (25 - (i - 1))
    else:
        S += ((x) ** i) / (25 - (i - 1))

print(f"Soma: {S}")
