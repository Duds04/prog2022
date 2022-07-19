# 17

tempo = int(input("Digite o tempo:"))
velocidade_media = int(input("Digite a velocidade média:"))

distancia = tempo * velocidade_media
litros = distancia / 12

print(f"A quantidade de litros gastos foi de {litros:.1f} litros")