def sodep(n):
    for i in range(0, len(n)):
        if ord(n[i]) % 2 == 1:
            return 0
    return 1
a = []
for j in range(1, 1000):
    if(sodep(str(j)) == 1): 
        a = a + [int(str(j) + str(j)[::-1])]
t = int(input())
for i in range(t):
    n = int(input())
    for i in a:
        if i < n: print(i, end = " ")
    print()
