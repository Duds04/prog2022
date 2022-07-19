#11

tabuada = []

for i in range(1,20):
    num = int(input(f"\nDigite o {i}º valor: "))
    for i in range (1, num+1):
        tabuada.append(i*num)
    print(f"A tabuada do {num} (de 1 até {num}) é: \n{tabuada}")
    tabuada = []