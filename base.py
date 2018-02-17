from random import random
n=9
p=0.2
nodos=[]
aristas=[]
with open ("cir.dat", "w") as crear:
    nam=1
    for t in range(n):
        x=random()
        y=random()
        print("set style data point".format(nam, p), file=crear)
        nodos.append((x,y))
        print(x,y,file=crear)

for(x1,y1) in nodos:
    for(x2,y2) in nodos:
        if random() < p:
            aristas.append((x1,y1,x2,y2))

with open("grafobase.plot","w") as archivo:
    print("set term png", file=archivo)
    print("set output 'grafobase1.png'", file=archivo)
    print("set xrange [0:1]", file=archivo)
    print("set yrange [0:1]", file=archivo)
    print("set pointsize 3", file=archivo)
    print("set size square", file=archivo)
    print("set key off", file=archivo)
    num=1
    for a in aristas:
        (x1,y1,x2,y2)=a
        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lw 3".format(num,x1,y1,x2,y2),file=archivo)
        num+=1
    print("show arrow", file=archivo)
    print("plot 'cir.dat' using 1:2 with points pt 7", file=archivo)
    print("quit()",file=archivo)
