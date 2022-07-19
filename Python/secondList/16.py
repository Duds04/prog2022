# 16

num = int(input("Digite um número (1 a 12):"))

if(num>=1 and num<=3):
    print("1º Trimestre")
elif(num>=4 and num<=6):
    print("2º Trimestre")
elif(num>=7 and num<=9):
    print("3º Trimestre")
elif (num>=10 and num<=12):
    print("4º Trimestre")
else:
    print("Mês inválido")
