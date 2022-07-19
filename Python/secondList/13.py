# 13

num = int(input("Digite um número:"))

if(num%3==0 and num%7==0):
    print(f"É divisível por 3 e 7.")
elif(num%3==0):
    print(f"É divisível por 3.")
elif(num%7==0):
    print(f"É divisível por 7.")