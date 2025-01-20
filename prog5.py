from math import tan, cos, radians, ceil,degrees
from time import sleep
from click import clear

g = 9.8
ang = radians(30)
u0 = 20
space = "  "
entity = "0 "
length = 11
matrix = []
gap = 0.2
g_var=0

def y_value(O, u0, x) -> int:
    global g,g_var
    t_fom = ceil(x * tan(O) - ((g * (x ** 2)) / (2 * (u0 ** 2) * (cos(O) ** 2))))
    if t_fom == 0:
        g_var +=1
        return 0
    if g_var!=2:
        return t_fom
    return 0


def rep(mat):
    mat = [i[::-1] for i in mat[::-1]]
    mat = [i[::-1] for i in mat]
    for i in mat:
        for j in i:
            print(j, end=" ")
        print()


def loop(arr, tim):
    rep(arr)
    sleep(tim)
    clear()


for i in range(length - 1):
    matrix.append([space] * (length - 1))

x_values = [i for i in range(length-1)]
y_values = [y_value(ang, u0, i) for i in x_values]

coord = {x_values[i]: y_values[i] for i in range(len(x_values))}

for x, y in coord.items():
    matrix[y][x] = entity
    if length<=28:
        loop(matrix, gap)
        print(f"the angle of trajectory is {degrees(ang)}")
        print(f"the velocity of the object is {u0}")

rep(matrix)
