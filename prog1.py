import timeit, time, keyboard
from click import clear

result = [1, 3, 5, 3, 1]


def obj(r):
    for i in result:
        spaces = (max(result) - i) // 2
        print("    " + " " * spaces * r + "#" * i + " " * spaces + "    ")


def sur():
    print("__" * max(result))


def space(a):
    for i in range(a):
        print("  " * max(result))


start = timeit.default_timer()

while True:
    if keyboard.is_pressed('left'):
        space(1)
        obj(0)
        space(1)
        sur()
    elif keyboard.is_pressed("space"):
        break
    elif keyboard.is_pressed("right"):
        space(1)
        obj(2)
        space(1)
        sur()
    else:
        space(1)
        obj(1)
        space(1)
        sur()
    time.sleep(0.2)
    clear()

stop = timeit.default_timer()
print("Time: ",stop-start)
