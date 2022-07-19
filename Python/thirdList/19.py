# 19
S, divisor = 1,1

for i in range(1,52):
    divisor += 2
    if(i%2!=0):
        S -= 1 / ((divisor) ** 3)
    else:
        S += 1 / ((divisor) ** 3)



print(f"pi = {((S*32)**(1/3))}")