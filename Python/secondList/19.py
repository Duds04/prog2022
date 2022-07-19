# 19

idade = int(input("Digite a idade da pessoa:"))
peso = float(input("Digite o peso da pessoa:"))

if(idade>=12):
    if(peso>=60):
        mg = 1000
    else:
        mg = 875
else:
    if(peso>=5 and peso<9):
        mg = 125
    elif (peso >= 9 and peso<16):
        mg = 250
    elif (peso >= 16 and peso<24):
        mg = 275
    elif (peso >= 24 and peso<30):
        mg = 500
    else:
        mg = 750

ml = mg/500
gotas = ml * 20

print({gotas})