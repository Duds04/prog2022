#10

n = int(input("Digite um nº: "))

fatorial = 1

if(n!=0):
    for i in range(n, 1, -1):
        fatorial *= i

print(f"O N! (fatorial de N) é: {fatorial}")
