# 14

eleitores = int(input("Digite o total de eleitores: "))
cad1,cad2,cad3,cad4,nulo,branco = 0, 0, 0, 0, 0, 0

for i in range(eleitores):
    voto = int(input("Digite o código do voto: "))
    if(voto == 1):
        cad1 +=1
    elif(voto == 2):
        cad2 +=1
    elif (voto == 3):
        cad3 += 1
    elif (voto == 4):
        cad4 += 1
    elif (voto == 5):
        nulo += 1
    elif (voto == 6):
        branco += 1

print(f"Total de votos do candidato 1: {cad1}")
print(f"Total de votos do candidato 2: {cad2}")
print(f"Total de votos do candidato 3: {cad3}")
print(f"Total de votos do candidato 4: {cad4}")
print(f"Total de votos nulos: {nulo}")
print(f"Total de votos em branco: {branco}")
print(f"Percentual de votos nulos e brancos sobre o total: {((nulo+branco)/eleitores)*100:.2f}%")
