salario = float(input())
imposto = 0
aux = 0

if(salario>2000):
    aux = salario - 3000
    if(aux>0):
        imposto = ((salario-2000)-aux)* 0.08
    else:
        imposto = (salario - 2000) * 0.08
if(salario>3000 and aux>0):
    if (aux > 1500):
        aux = salario - 4500
        imposto += ((salario-3000)-aux)* 0.18
    else:
        imposto += aux * 0.18
if(salario>4500):
        imposto += aux * 0.28
if(salario>0 and salario<=2000):
    print("Isento")
else:
    print(f"R$ {imposto:.2f}")