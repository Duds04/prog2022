salario_min = float(input("Digite o valor do salario: "))
quilowatts = int(input("Digite a quantidade de quilowatts gastas: "))

valor_kw = (salario_min/7)/100
valor_total = valor_kw * quilowatts
valor_descontado = valor_total - (valor_total*0.1)

print(f"Valor por kw: {valor_kw:.2f}")
print(f"Valor total: {valor_total:.2f}")
print(f"Valor total: {valor_descontado:.2f}")