import functools

class DanhSach:
    def __init__(self, name, ac, submit):
        self.name = name
        self.ac = ac
        self.submit = submit

def cmp(a, b):
    if a.ac < b.ac: return 1
    elif a.ac == b.ac:
        if a.submit > b.submit: return 1
        elif a.submit == b.submit:
            if a.name > b.name: return 1
            else: return -1
        else: return -1
    else: return -1

n = int(input())
list = []
for i in range(n):
    name = input()
    ac, submit = [int(x) for x in input().split()]
    list.append(DanhSach(name, ac, submit))
list = sorted(list, key = functools.cmp_to_key(cmp))
for i in list :
    print(i.name, i.ac, i.submit)
