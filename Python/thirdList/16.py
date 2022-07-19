# 16
qnt_sim = 0
qnt_não = 0
qnt_fem_sim = 0
qnt_masc_nao = 0

for i in range(2000):
    sexo = int(input("Digite seu sexo (1= masculino, 2 = feminino): "))
    resposta = int(input("Digite sua resposta (1 = sim, 2 = não): "))
    if(resposta == 1):
        qnt_sim +=1
        if(sexo == 2):
            qnt_fem_sim += 1
    if(resposta == 2):
        qnt_não +=1
        if(sexo == 1):
            qnt_masc_nao +=1

print(f"Quantidade de pessoas que responderam sim: {qnt_sim}")
print(f"Quantidade de pessoas que responderam não: {qnt_não}")
print(f"Porcentagem de pessoas do sexo feminino que responderam sim : {(qnt_fem_sim/2000)*100:.2f}")
print(f"Porcentagem de pessoas do sexo masculino que responderam não : {(qnt_masc_nao/2000)*100:.2f}")

