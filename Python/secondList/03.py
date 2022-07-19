# 03

idade_anos = int(input("Digite sua idade (em anos):"))
idade_meses = int(input("Digite quantos meses faltam para o seu aniversário:"))
idade_dias = int(input("Digite quantos dias para o seu aniversário:"))

idade_total = idade_anos * 365
idade_total += (idade_meses * 30)
idade_total += idade_dias

print(f"Sua idade em dias é: {idade_total}")
