salario = float(input())

if(salario<=400.0):
    reajuste = (salario*0.15)
    salario += reajuste
    reajuste_percentual = "15 %"
elif(salario<=800.0):
    reajuste = (salario*0.12)
    salario += reajuste
    reajuste_percentual = "12 %"
elif(salario<=1200.0):
    reajuste = (salario*0.10)
    salario += reajuste
    reajuste_percentual = "10 %"
elif (salario <= 2000.0):
    reajuste = (salario*0.07)
    salario += reajuste
    reajuste_percentual = "7 %"
elif(salario> 2000.0):
    reajuste = (salario*0.04)
    salario += reajuste
    reajuste_percentual = "4 %"

print(f"Novo salario: {salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {reajuste_percentual}")