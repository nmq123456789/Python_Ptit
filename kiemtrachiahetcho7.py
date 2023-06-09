t = int(input())
for i in range(t):
    count = 1
    n = input()
    while int(n) % 7 != 0 and count < 1001:
        n = str(n)
        n = int(n) + int(n[::-1])
        n = str(n)
        count += 1
    print(n)

