n1 = float(input("Digite nota 1: "))
n2 = float(input("Digite nota 2: "))

media = (n1+n2)/2

if(media >=7):
    print("Aprovado")
elif(media<3):
    print("Reprovado")
else:
    print("Em exame")