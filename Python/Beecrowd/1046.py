inicial, final = map(int, input().split(" "))

total = inicial - final

if(inicial>final):
    aux = 24 - inicial
    total = aux + final
elif(final>inicial):
    total = final - inicial
elif(total == 0):
    total = 24


print(f"O JOGO DUROU {total} HORA(S)")