M, N = map(int, input().split(" "))
lista = []

while M>0 and N>0:
    if(M<N):
        lista = list(range(M, N+1))
    if(N<M):
        lista = list(range(N, M+1))

    lista_formatada = ' '.join(map(str,lista))
    print(f"{lista_formatada} Sum={sum(lista)}")
    M, N = map(int, input().split(" "))
