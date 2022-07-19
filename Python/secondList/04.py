# 04

idade_dias = int(input("Digite sua idade (em dias):"))

idade_anos = int(idade_dias // 365)
idade_dias -= idade_anos * 365
idade_meses = int(idade_dias // 30)
idade_dias -= idade_meses * 30

print(f"Idade em anos: {idade_anos}\nIdade em meses: {idade_meses}\nIdade em dias: {idade_dias}")