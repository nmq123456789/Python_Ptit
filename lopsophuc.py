for i in range(int(input())):
    a, b , c , d = [int(x) for x in input().split()]
    x = (complex(a, b) + complex(c, d)) * complex(a, b)
    y = (complex(a, b) + complex(c, d)) ** 2
    dau1, dau2 = '+', '+'
    if x.imag < 0: dau1 = '-'
    if y.imag < 0: dau2 = '-'
    print(f'{int(x.real)} {dau1} {int(abs(x.imag))}i, {int(y.real)} {dau2} {int(abs(y.imag))}i')