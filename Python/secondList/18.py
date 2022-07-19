# 18

peso_terra = float(input("Digite o peso na Terra:"))
num_planeta = int(input("Digite o número do planeta:"))

if(num_planeta == 1):
    print(f"Peso em Mercúrio: {peso_terra * 0.37}")
elif(num_planeta == 2):
    print(f"Peso em Vênus: {peso_terra * 0.88}")
elif(num_planeta == 3):
    print(f"Peso em Marte: {peso_terra * 0.38}")
elif(num_planeta == 4):
    print(f"Peso em Júpiter: {peso_terra * 2.64}")
elif(num_planeta == 5):
    print(f"Peso em Saturno: {peso_terra * 1.15}")
elif(num_planeta == 6):
    print(f"Peso em Urano: {peso_terra * 1.17}")