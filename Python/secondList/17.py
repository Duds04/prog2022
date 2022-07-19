# 17

salario = float(input("Digite o sálario bruto:"))
prestacao = float(input("Digite a prestação:"))

if(prestacao > (salario*0.3)):
    print("Empréstimo não pode ser concedido")
else:
    print("Empréstimo pode ser concedido")