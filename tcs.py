string=""
with open("DATA.in","rb") as f:
    string = f.readline().strip()

    while string!="":
        s= 0
        n = ""
        for i in string:
            if i.isdigit():
                n += chr(i)
                s+= int(i)-48
        if n!="":
            print(int(n),s)
        string = f.readline().strip()