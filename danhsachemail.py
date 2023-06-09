a = []
with open('CONTACT.in.txt') as file:
    for i in file:
        a.append(i.lower().rstrip().strip())
st = set(a)
st = sorted(st)
for i in st: print(i)
        
