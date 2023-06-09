def ql(n, a, b, c):
    if n == 1:
        print(a,"->", c)
        return
    ql(n - 1, a, c, b) 
    ql(1, a, b, c)
    ql(n - 1, b, a, c)
    return
n = int(input())
a = 'A'
b = 'B'
c = 'C'
ql(n, a, b, c)