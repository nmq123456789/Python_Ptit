def New(s):
    n = 0
    for i in s : n += ord(i) - ord('0')
    return str(n)
s = input()
cnt = 0
while(len(s) > 1) :
    s = New(s)
    cnt += 1
print(cnt)