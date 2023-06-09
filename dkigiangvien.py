class GiangVien:
    def __init__(self,code,name,number,lythuyet,thuchanh):
        self.code = code
        self.name = name
        self.number = number
        self.lythuyet = lythuyet
        self.thuchanh = thuchanh
    def __str__(self):
        return self.code + ' ' + self.name + ' ' + self.number + ' ' + self.lythuyet + ' ' + self.thuchanh

a =  list()

f = open("MONHOC.in", mode= 'r')

n = int(f.readline().strip())
for i in range(n):
    code = f.readline().strip()
    name = f.readline().strip()
    number = f.readline().strip()
    lythuyet = f.readline().strip()
    thuchanh = f.readline().strip()
    x = GiangVien(code,name,number,lythuyet,thuchanh)
    a.append(x)
a = sorted(a, key= lambda x : x.code)
for i in a:
    print(i)
    
   
        