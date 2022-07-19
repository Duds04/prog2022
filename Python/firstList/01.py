# 01
valor_gasto = float(input("\nDigite o valor das despesas realizadas no restaurante:"))
gorjeta = valor_gasto * 0.1
valor_total = valor_gasto + gorjeta
print(f"O valor da gorjeta foi: R${gorjeta:.2f}\nO valor total foi: {valor_total:.2f}")