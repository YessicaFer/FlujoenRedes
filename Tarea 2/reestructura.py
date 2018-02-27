from random import random, choice
from math import sqrt, floor, ceil

def euclidiana(ñ,r):
    return ((((ñ[0]-r[0])**2)+((ñ[1]-r[1])**2))**(0.5))

def updown(blabla):
    if (abs(blabla) - abs(int(blabla)))<0.5:
        f=floor(blabla)
    else:
        f=ceil(blabla)
    return f

class GrafoYessica:
    def _init_(self):
        self.n=0
        self.x=dict()
        self.y=dict
        self.c=dict()
        self.d=dict()
        
    def nodoscrear(self, tamaño):
        self.n=tamaño
        for t in range (tamaño):
            self.x[t]=random()
            self.y[t]=random()
            self.c[t]=choice([5,7,9,13])
            self.d[t]=random()

    def conectar(self):
        for x in range(tamaño):
            self.e=random()*10
            updown(self.e)
            for i in [0,self.n-2]:
                for m in [0,self.n-4]:
                    if euclidiana((self.x[x],self.y[x],self.c[x],self.d[x]),(self.x[i],self.y[i],self.c[i],self.d[i]))< euclidiana((self.x[x], self.y[x], self.c[x], self.d[x]),(self.x[m],self.y[m],self.c[m],self.d[m])):
                        if euclidiana((self.x[x],self.y[x],self.c[x],self.d[x]),(self.x[i],self.y[i],self.c[m],self.d[m]))<0.5:
                            if self.c[x]==self.c[i]:
                                aristas.append((self.x[x], self.y[x], self.x[i], self.y[i],f))
                    else:
                        if euclidiana((self.x[x],self.y[x],self.c[x],self.d[x]),(self.x[x],self.y[m],self.c[m],self.d[m]))<0.5:
                            if self.c[x]==self.c[m]:
                                aristas.append((self.x[x], self.y[x], self.x[m], self.y[m],f))

def archivo (self, tamaño):
    with open("tarea2.plot", "w") as archivo:
        print("set term png", file=archivo)
        print("set output 'grafica2.png'", file=archivo)
        print("set xrange [0:1]", file=archivo)
        print("set yrange [0:1]", file=archivo)
        print("set pointsize 3", file=archivo)
        print("set size square", file=archivo)
        print("set key off", file=archivo)
        num = 1
        for a in aristas:
            (self.x[x], self.y[x], self.x[i], self.y[i], f) = a
            print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lw 1.5 lt {:d}".format(num, self.x[x], self.y[x], self.x[i], self.y[i], f), file=archivo)
            num += 1
        print("show arrow", file=archivo)
        print("plot 'ejemplo40.dat' using 1:2:3:4 with points pt var lc palette var", file=archivo)
        print("quit()", file=archivo)
