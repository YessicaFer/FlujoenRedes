from random import random, choice
n=10
nodos=[]
with open ("puntosdif.dat", "w") as salida:
    for t in range(n):
        x=random()
        y=random()
        c=choice([5,7,9,13])
        d=random()
        nodos.append((x,y,c,d))
        print(x, y, c, d, file=salida)

with open("puntos1dif.plot", "w") as archivo:
    print("set term png", file=archivo)
    print("set output 'nod1.png'", file=archivo)
    print("set xrange [0:1]", file=archivo)
    print("set yrange [0:1]", file=archivo)
    print("set pointsize 3", file=archivo)
    print("set size square", file=archivo)
    print("set key off", file=archivo)
    print("plot 'puntosdif.dat' using 1:2:3:4 with points pt var lc palette var", file=archivo)
    print("quit()", file=archivo)
