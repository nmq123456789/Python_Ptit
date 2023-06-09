s = input()
s = s.lower()
if s[len(s) - 3 : len(s)] == ".py":
    print("yes")
else:
    print("no")