
for i in  range(5):
    a, b = map(int, input().split(" "))
    for i in range(a, b+1):
        if(i%2==0):
            print(i)