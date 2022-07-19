D = int(input())
A = int(input())
N = int(input())

total = D * 31

if(N>1 and N<15):
    total = (D + (A * (N-1))) * (31-(N-1))
elif(N>=15):
    total = (D + (A * (14))) * (31 - (N-1))

print(total)