# 18

custo_fabrica = float(input("Digite o custo de fabrica:"))

preco_com_imposto = custo_fabrica  + (0.45 * custo_fabrica)
custo_consumidor = preco_com_imposto + (0.28 * preco_com_imposto)

print(f"O custo para o consumidor é {custo_consumidor}")