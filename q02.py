import numpy as np

arr = np.random.rand(5, 4)

print arr

x = -1
y = -1
for i in arr:
    x = -1
    y = y+1
    for j in i:
        x = x+1
        arr[y][x] = int(j*1000)
        if  (arr[y][x] > 50):
            arr[y][x] = 100

print arr
