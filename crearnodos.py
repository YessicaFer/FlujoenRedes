from random import random
n=10
nodos=[]
with open ("puntos.dat", "w") as salida:
    for t in range(n):
        x=random()
        y=random()
        nodos.append((x,y))
        print(x, y, file=salida)

with open("puntos1.plot", "w") as archivo:
    print("set term png", file=archivo)
    print("set output 'nod.png'", file=archivo)
    print("set xrange [0:1]", file=archivo)
    print("set yrange [0:1]", file=archivo)
    print("set pointsize 3", file=archivo)
    print("set size square", file=archivo)
    print("set key off", file=archivo)
    print("plot 'nodos.dat' using 1:2 with points pt 7", file=archivo)
    print("quit()", file=archivo)
