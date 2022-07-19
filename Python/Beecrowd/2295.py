A, G, RA, RG = map(float, input().split(" "))

car_alcool = (A / RA)
car_gasolina = (G / RG)

if(car_alcool<car_gasolina):
    print("A")
else:
    print("G")