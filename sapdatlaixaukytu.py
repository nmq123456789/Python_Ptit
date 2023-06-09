t = int(input())
for i in range(t):
    s1 = input()
    s2 = input()
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2: 
        print("Test", i + 1, end = "")
        print(": YES")

    else: 
        print("Test", i + 1, end = "")
        print(": NO")
