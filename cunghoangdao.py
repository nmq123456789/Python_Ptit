t = int(input())
cung = ["Bach Duong", "Kim Nguu", "Song Tu", "Cu Giai",
        "Su Tu", "Xu Nu", "Thien Binh", "Thien Yet", "Nhan Ma",
        "Ma Ket", "Bao Binh", "Song Ngu"
        ]
time = [[4, 19], [5, 20], [6, 20], [7, 22], [8, 22], [9, 22],
        [10, 22], [11, 22], [12, 21], [1, 19], [2, 18], [3, 20]
        ]
def find(d, m):
    for i in range(len(time)):
        if m == time[i][0]:
            if d <= time[i][1]:
                return i
            else:
                if i + 1 == len(time):
                    return 0
                else:
                    return i+1


while t > 0:
    t -= 1
    d, m = [int(i) for i in input().split(" ")]
    print(cung[find(d, m)])