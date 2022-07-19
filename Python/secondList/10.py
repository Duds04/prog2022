# 10

A = int(input("Digite o número A:"))
B = int(input("Digite o número B:"))
C = int(input("Digite o número C:"))

if (A>B):
    if(B>C):
        print(f"{A}-{B}-{C}")
    elif(A>C):
        print(f"{A}-{C}-{B}")
    else:
        print(f"{C}-{A}-{B}")
elif(B>C):
    if(A>C):
        print(f"{B}-{A}-{C}")
    else:
        print(f"{B}-{C}-{A}")
else:
    print(f"{C}-{B}-{A}")

