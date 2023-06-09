x = int(input())
while(x > 0):
    y = int(input())
    if(y <= 10): print(y)
    else:
        t = 0 
        d = 1
        while(y >= 10):
            if(int(y % 10 + t) >= 5): 
                t = 1
            else: 
                t = 0
            y = int(y / 10)
            d *= 10
        print (int((y + t) * d))
    x = x - 1



