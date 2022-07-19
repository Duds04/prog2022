compra = float(input("Digite valor compra: "))

if(compra<10):
    venda = compra * 1.7
elif(compra<30):
    venda = compra * 1.5
elif(compra<50):
    venda = compra * 1.4
else:
    venda = compra * 1.3

print(f"Valor venda {venda}")