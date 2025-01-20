from click import clear
import time,sys,timeit
result = [1, 3, 5, 7, 5, 3, 1]
def obj():
    global result
    spaces = (max(result) - 1) // 2
    for i in result:
        print("    "+" " * spaces + "#" * i+" "*spaces+"    ")
def sur():
    print("__" * max(result))
    time.sleep(0.1)
    clear()
def space(a):
    for i in range(a):
        print("             ")

def generate_sequence(num):
    result = []
    for i in range(num + 1):
        result.append(i)

    for i in range(num - 1, -1, -1):
        result.append(i)

    return result


ani=int(input("enter space distance\n"))
a=generate_sequence(num=ani)
rep=int(input("enter iteration number\n"))

start = timeit.default_timer()

for j in range(rep):
    for i in a:
        sys.stdout.write(str(i)+"\n")
        space(i)
        obj()
        space(max(a)-i)
        sur()
        sys.stdout.write('\r')
stop = timeit.default_timer()
print("Time: ",stop-start)
