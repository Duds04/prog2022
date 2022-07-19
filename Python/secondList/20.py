# 20

numero_bola = int(input("Digite o número da bola:"))
dinheiro = float(input("Digite o valor do dinheiro restante:"))

if(numero_bola == 0):
    premio = dinheiro * 1.05
elif(numero_bola == 1):
    premio = dinheiro * 1.25
elif(numero_bola == 2):
    premio = dinheiro * 1.10
elif(numero_bola == 3):
    premio = dinheiro * 1.07
elif(numero_bola == 4):
    premio = dinheiro * 1.08
elif(numero_bola == 5):
    premio = dinheiro * 1.05
elif(numero_bola == 6):
    premio = dinheiro * 1.15
elif(numero_bola == 7):
    premio = dinheiro * 1.12
elif(numero_bola == 8):
    premio = dinheiro * 1.03
elif(numero_bola == 9):
    premio = dinheiro * 1.10

print(f"O prêmio p/ bola {numero_bola} foi de : {premio}")