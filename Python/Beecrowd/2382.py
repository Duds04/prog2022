L, A, P, R = map(int, input().split(" "))

operacao = ((L**2)+(A**2)+(P**2))**(1/2)
diametro = R+R

if(diametro>=operacao):
    print('S')
else:
    print('N')