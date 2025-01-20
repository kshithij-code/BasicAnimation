from keyboard import is_pressed
from time import sleep
from click import clear

space = "- "
entity = "# "
length = 10
matrix = []
gap = 0.5
for i in range(length - 1):
    matrix.append([space] * (length - 1))


def rep(mat):
    for i in mat:
        for j in i:
            print(j, end=" ")
        print()

def loop(arr,tim):
    rep(arr)
    sleep(tim)
    clear()

length=len(matrix)-1
x = 0
y = length
for i in range(int(length-length/2)+1):
    matrix[y][x] = entity
    loop(matrix,gap)
    x += 1
    y -= 1

y += 1
x -= 1
for i in range(int(length-length/2)):
    y += 1
    x += 1
    matrix[y][x] = entity
    loop(matrix, gap)

rep(matrix)


