# 15
nome_vendedor = input("Digite o nome do vendedor: ")
carros_vendidos  = int(input("Digite a quantidade de carros vendidos: "))
valor_venda  = float(input("Digite o valor total das vendas: "))

salario = 500 + (50*carros_vendidos) + (valor_venda*0.05)

print(f"O valor do salário do vendedor {nome_vendedor} foi: {salario}")