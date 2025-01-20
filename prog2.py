import time,keyboard,timeit
from click import clear

start=timeit.default_timer()
i=0
lent=20
while True:
    mov = ["-"] *i + ["#"] + ["-"] * (lent-i)
    print("".join(mov))
    time.sleep(0.1)
    clear()
    if keyboard.is_pressed('right'):
        i+=1
    elif keyboard.is_pressed('left'):
        i-=1
    if i>lent:
        i=0
    elif i<0:
        i=lent
    if keyboard.is_pressed('space'):
        break
end = timeit.default_timer()
print("Time: ",end-start)
