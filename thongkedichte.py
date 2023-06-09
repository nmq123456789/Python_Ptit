
m, n = [int(x) for x in input().split()]
a =[[]] * m * n
tong = 0
for i in range(m):
    a[i] = [int(x) for x in input().split()]
for i in range(m):
    for j in range(n):
        if a[i][j] == -1:
            if i > 0 and j > 0:
                # if a[i - 1][j - 1] != -1:
                    tong += a[i - 1][j - 1]
                    a[i - 1][j - 1] = 0
            if j > 0:
                # if a[i][j - 1] != -1:
                    tong += a[i][j - 1]
                    a[i][j - 1] = 0
            if i < m - 1 and j > 0:
                # if a[i + 1][j - 1] != -1:
                    tong += a[i + 1][j - 1]
                    a[i + 1][j - 1] = 0
            if i < m - 1:
                # if a[i + 1][j] != -1:
                    tong += a[i + 1][j]
                    a[i + 1][j] = 0
            if i < m - 1 and j < n - 1:
                # if a[i + 1][j + 1] != -1:
                    tong += a[i + 1][j + 1]
                    a[i + 1][j + 1] = 0
            if j < n - 1:
                # if a[i][j + 1] != -1:
                    tong+=a[i][j + 1]
                    a[i][j + 1] = 0
            if i > 0 and j < n - 1:
                # if a[i - 1][j + 1] != -1:
                    tong += a[i - 1][j + 1]
                    a[i - 1][j + 1] = 0
            if i > 0:
                # if a[i - 1][j] != -1:
                    tong += a[i - 1][j]
                    a[i - 1][j] = 0
print(tong)
