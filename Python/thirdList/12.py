#12
fibonacci = [1,1]

for i in range(1,19):
    fibonacci.append(fibonacci[i]+fibonacci[i-1])

print(f"A sequencia de Fibonacci até o vigessimo nº é: \n{fibonacci}")