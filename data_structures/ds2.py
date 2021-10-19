a = [4, 0, 1, -2, 3]
n=5

b = [0] * n
for i in range(n):
    if i == 0:
        b[i] = a[i] + a[i + 1]
    elif i == n - 1:
        b[i] = a[i - 1] + a[i]
    else:
        b[i] = a[i - 1] + a[i] + a[i + 1]

print(b)