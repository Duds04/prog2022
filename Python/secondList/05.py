# 05

divisor = int(input("Digite o divisor:"))
dividendo = int(input("Digite o dividendo:"))

if divisor != 0:
    quociente = dividendo // divisor
    resto = dividendo % divisor
    print(f"Quociente: {quociente}\nResto:{resto}")
else:
    print("Divisão não permitida")
