# 14

idade = int(input("Digite sua idade:"))

if(idade<16):
    print("Não eleitor")
elif(idade>=18 and idade<65):
    print("Eleitor obrigatório")
elif(idade>=16 or idade>=65):
    print("Eleitor facultativo")