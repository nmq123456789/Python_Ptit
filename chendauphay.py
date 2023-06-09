n = input()
s = ""
d = 1
for i in range(len(n) - 1, -1,- 1):
    s += n[i]
    if(d % 3 == 0 and i != 0): s += ','
    d += 1
cnt = s[::-1]
print(cnt)