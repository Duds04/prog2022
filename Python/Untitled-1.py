p, t = map(int, input("Digite p e t: ").split(" "))
n = 1
contm, x = [0, 0]
while True:
    n = int(input())
    if(n!=1):
        if(t>=contm):
            x += n
        contm+=1
    else:
        break

if(x>p):
    print(f"Apenas {x} pessoas a salvo")
else:
    print("Todos a salvo")