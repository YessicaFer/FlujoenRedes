from random import random, choice
from math import sqrt
from math import floor, ceil
n=30
nodos=[]
aristas=[]
with open ("ejemplo40.dat", "w") as salida:
    for t in range(n):
        x=random()
        y=random()
        c=choice([5,7,9,13])
        d=random()
        nodos.append((x,y,c,d))
        print(x, y, c, d, file=salida)

def euclidiana(ñ,r):
    return ((((ñ[0]-r[0])**2)+((ñ[1]-r[1])**2))**(1/2))

for (x1, y1, c1, d1) in nodos[0:n]:
    e=random()*10
    if (abs(e) - abs(int(e)))<0.5:
        f=floor(e)
    else:
        f=ceil(e)
    for (x2, y2, c2, d2) in nodos[0:n-2]:
        for (x3, y3, c3, d3) in nodos[0:n-4]:
            if euclidiana((x1,y1,c1,d1),(x2,y2,c2,d2))< euclidiana((x1, y1, c1, d1),(x3,y3,c3,d3)):
                if euclidiana((x1,y1,c1,d1),(x2,y2,c2,d2))<0.5:
                    if c1==c2:
                        aristas.append((x1, y1, x2, y2,f))
            else:
                if euclidiana((x1,y1,c1,d1),(x3,y3,c3,d3))<0.5:
                    if c1==c3:
                        aristas.append((x1, y1, x3, y3,f))

with open("ejemplo40.plot", "w") as archivo:
    print("set term png", file=archivo)
    print("set output 'grafica40.png'", file=archivo)
    print("set xrange [0:1]", file=archivo)
    print("set yrange [0:1]", file=archivo)
    print("set pointsize 3", file=archivo)
    print("set size square", file=archivo)
    print("set key off", file=archivo)
    num = 1
    for a in aristas:
        (x1, y1, x2, y2, f) = a
        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lw 1.5 lt {:d}".format(num, x1, y1, x2, y2, f), file=archivo)
        num += 1
    print("show arrow", file=archivo)
    print("plot 'ejemplo40.dat' using 1:2:3:4 with points pt var lc palette var", file=archivo)
    print("quit()", file=archivo)


