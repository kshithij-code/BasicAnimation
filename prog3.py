import time, click

import keyboard

space = "."
entity = "0"
length = 10
matrix = []
gap = 0.1
for i in range(length):
    matrix.append([space] * length)


def rep(mat):
    for i in mat:
        for j in i:
            print(j, end=" ")
        print()

def loop(arr,tim):
    rep(arr)
    time.sleep(tim)
    click.clear()

i = j = 0
while True:
    if keyboard.is_pressed('right'):
        if j != length - 1:
            j += 1
        else:
            j = 0
        if j >= 0:
            matrix[i][j - 1] = space

        matrix[i][j] = entity
        loop(matrix,gap)
    elif keyboard.is_pressed('left'):
        if j != 0:
            j -= 1
        else:
            j = length - 1
        if j < length - 1:
            matrix[i][j + 1] = space
        if j == length - 1:
            matrix[i][0] = space
        matrix[i][j] = entity
        loop(matrix,gap)
    elif keyboard.is_pressed('down'):
        if i != length - 1:
            i += 1
        else:
            i = 0
        if i >= 0:
            matrix[i - 1][j] = space
        matrix[i][j] = entity
        loop(matrix,gap)
    elif keyboard.is_pressed('up'):
        if i != 0:
            i -= 1
        else:
            i = length - 1
        matrix[i][j] = entity
        if i < length - 1:
            matrix[i + 1][j] = space
        if i == length - 1:
            matrix[0][j] = space
        loop(matrix,gap)
    elif keyboard.is_pressed('space'):
        time.sleep(gap)
        break
    else:
        loop(matrix, gap)
