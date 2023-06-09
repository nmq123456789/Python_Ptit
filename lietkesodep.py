def sodep(n):
    if len(n) % 2 == 1: return 0
    if(n != n[::-1]): return 0
    for i in range(0, len(n)):
        if n[i] != '0' and n[i] != '2'and n[i] != '4' and n[i] != '6' and n[i] != '8':
            return 0
    return 1

t = int(input())
for i in range(t):
    n = int(input())
    for j in range(10, n):
        if(sodep(str(j)) == 1): print(j, end = " ")
    print()
