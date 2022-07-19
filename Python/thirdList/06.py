#06

x = int(input("Digite o valor de x: "))
z = int(input("Digite o valor de z: "))

if (x<z):
    for x in range(x,(z+1)):
        print(x)
else:
    for x in range(x,(z-1),-1):
        print(x)