import functools

class VCK:
    def __init__(self, name, diem, chiso, hieuso):
        self.name = name
        self.diem = diem
        self.chiso = chiso
        self.hieuso = hieuso
    def out(self):
        print(self.name, self.diem, self.chiso, self.hieuso)

def cmp(a, b):
    if a.diem < b.diem: return 1
    elif a.diem == b.diem:
        if a.chiso < b.chiso: return 1
        elif a.chiso == b.chiso:
            if a.hieuso < b.hieuso: return 1
            else: return -1
        else: return -1
    else: return -1

n = int(input())
list = []
for i in range(n):
    name = input()
    a = input().split()
    list.append(VCK(name, int(a[0]), int(a[1]), int(a[2])))
list = sorted(list, key = functools.cmp_to_key(cmp))
for i in list :
    i.out()
