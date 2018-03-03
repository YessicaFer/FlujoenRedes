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
    def __init__(self):
        self.n=0
        self.x=dict()
        self.y=dict()
        self.c=dict()
        self.d=dict()
        
    def nodoscrear(self, tamaño):
        self.n=tamaño
        with open ("prueba1.dat", "w") as salida:
            for t in range (tamaño):
                self.x[t]=random()
                self.y[t]=random()
                self.c[t]=choice([5,7,9,13])
                self.d[t]=random()
                print(self.x[t], self.y[t], self.c[t], self.d[t], file=salida)
            

    def conectar(self, tamaño):
        for x in range(tamaño):
            v=choice([1,2,3,4,5])
            self.e=random()*10
            f=updown(self.e)
            for i in range (tamaño-2):
                for m in range (tamaño-4):
                    if euclidiana((self.x[x],self.y[x],self.c[x],self.d[x]),(self.x[i],self.y[i],self.c[i],self.d[i]))< euclidiana((self.x[x], self.y[x], self.c[x], self.d[x]),(self.x[m],self.y[m],self.c[m],self.d[m])):
                        if euclidiana((self.x[x],self.y[x],self.c[x],self.d[x]),(self.x[i],self.y[i],self.c[m],self.d[m]))<0.5:
                            if self.c[x]==self.c[i]:
                                aristas.append((self.x[x], self.y[x], self.x[i], self.y[i],f,v))
                    else:
                        if euclidiana((self.x[x],self.y[x],self.c[x],self.d[x]),(self.x[x],self.y[m],self.c[m],self.d[m]))<0.5:
                            if self.c[x]==self.c[m]:
                                aristas.append((self.x[x], self.y[x], self.x[m], self.y[m],f,v))

        with open("tarea2.plot", "w") as archivo:
            print("set term eps", file=archivo)
            print("set output 'grafica2.eps'", file=archivo)
            print("set xrange [-.1:1.1]", file=archivo)
            print("set yrange [-.1:1.1]", file=archivo)
            print("set pointsize 1", file=archivo)
            print("set size square", file=archivo)
            print("set key off", file=archivo)
            if grafoorientado is 1:
                if grafocapacitado is 1:
                    num = 1
                    for a in aristas:
                        (self.x[num], self.y[num], self.x[num+1], self.y[num+1], f, v) = a
                        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} head filled size 0.04,8 lt {:d} dashtype {:d}".format(num, self.x[num], self.y[num], self.x[num+1], self.y[num+1], f, v), file=archivo)
                        num += 1
                else:
                    num = 1
                    for a in aristas:
                        (self.x[num], self.y[num], self.x[num+1], self.y[num+1], f, v) = a
                        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} head filled size 0.04,7 lt {:d}".format(num, self.x[num], self.y[num], self.x[num+1], self.y[num+1], f, v), file=archivo)
                        num += 1
            else:
                if grafocapacitado is 1:
                    num = 1
                    for a in aristas:
                        (self.x[num], self.y[num], self.x[num+1], self.y[num+1], f, v) = a
                        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lt {:d} dashtype {:d}".format(num, self.x[num], self.y[num], self.x[num+1], self.y[num+1], f, v), file=archivo)
                        num += 1
                else:
                    num = 1
                    for a in aristas:
                        (self.x[num], self.y[num], self.x[num+1], self.y[num+1], f, v) = a
                        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lw 1.5 lt {:d}".format(num, self.x[num], self.y[num], self.x[num+1], self.y[num+1], f, v), file=archivo)
                        num += 1
            print("show arrow", file=archivo)
            print("plot 'prueba1.dat' using 1:2:3:4 with points pt var lc palette var", file=archivo)
            print("quit()", file=archivo)

            
n=20
aristas=[]
grafoorientado=0      #para que sea orientado grafoorientado=1/ de lo contrario 2
grafocapacitado=0     #para que sea capacitado grafocapacitado=1/ de lo contrario 2
#si grafoorientado=2 y grafocapacitado=2 se forma un grafo simple
G=GrafoYessica()
G.nodoscrear(n)
G.conectar(n)
