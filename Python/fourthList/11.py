destino = input("Digite a regiao: ")
ida_volta = input("É ida e volta (S ou N): ")

if(destino == "Regiao Norte"):
    if(ida_volta == "S"):
        print(f"R$ 900,00")
    else:
        print(f"R$ 500,00")
elif(destino == "Regiao Nordeste"):
    if(ida_volta == "S"):
        print(f"R$ 650,00")
    else:
        print(f"R$ 350,00")
elif(destino == "Regiao Centro-Oeste"):
    if(ida_volta == "S"):
        print(f"R$ 600,00")
    else:
        print(f"R$ 350,00")
elif(destino == "Regiao Sul"):
    if(ida_volta == "S"):
        print(f"R$ 550,00")
    else:
        print(f"R$ 300,00")