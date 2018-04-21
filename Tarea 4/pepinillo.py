from random import random, randint
from math import sqrt, cos, pi, sin, ceil, fmod, floor
import time

class GrafoYessica:
    def __init__(self):
        self.n=0
        self.d = {}
        self.V= dict()
        self.E=dict()
        self.vecinos=dict()
        self.pos=dict()
        self.suma = 0
        with open ("prueba1.dat", "w") as f:
            print("", end="",file=f)
        with open ("Floyd-Warshallprueba1.dat.dat", "w") as f:
            print("", end="",file=f)
        
    def nodoscrear(self, v):
        self.pos[v] = (c[0]+(r * cos(angulo * v)), c[1]+(r* sin(angulo * v)))
        x= (self.pos[v][0])*10
        y=(self.pos[v][1])*10
        self.V[v]=(x,y)
        with open ("prueba1.dat", "a") as salida:
            print(x, y, file=salida)
        if not v in self.vecinos:
            self.vecinos[v]=set()

    def euclidiana(self,n1,n2):
        x1=self.V[n1][0]
        y1=self.V[n1][1]
        x2=self.V[n2][0]
        y2=self.V[n2][1]
        return sqrt( ((x1-x2)**2)+((y1-y2)**2) )

    def conecta(self, k):
        for j in range(k):
            for i in range(len(self.V)):
                if i< (len(self.V)-(j+1)):
                    self.E[(i, i+(j+1))] = self.E[(i+(j+1), i)]=self.euclidiana(i,(i+(j+1)))
                    self.vecinos[i].add(i+(j+1))
                    self.vecinos[i+(j+1)].add(i)
                else:
                    self.E[(i, (i + (j+1)) - len(self.V))] = self.E[(i + (j+1)) - len(self.V), i]=self.euclidiana(i,(i + (j+1)) - len(self.V))
                    self.vecinos[i].add((i + (j+1)) - len(self.V))
                    self.vecinos[(i + (j+1)) - len(self.V)].add(i)

    def conectaaleatorio(self, prob):
        for m in range(len(self.V)):
            for w in range(prob):
                if m is not w and (m,w) not in self.E:
                    if randint(1,n)< prob:
                        self.E[(m,w)]=self.E[(w,m)]=self.euclidiana(m,w)
                        self.vecinos[m].add(w)
                        self.vecinos[w].add(m)

    def floyd_warshall(self):
        for z in range(len(self.V)):
            self.d[(z, z)] =0 # distancia reflexiva es cero
            for u in range(len(self.E)): # para vecinos, la distancia es el peso
                if (z,u) in self.E:
                    self.d[(z, u)] = self.E[(z,u)]
        for intermedio in range(len(self.V)):
            for desde in range(len(self.V)):
                for hasta in range(len(self.V)):
                    di = None
                    if (desde, intermedio) in self.d:
                        di = self.d[(desde, intermedio)]
                    ih = None
                    if (intermedio, hasta) in self.d:
                        ih = self.d[(intermedio, hasta)]
                    if di is not None and ih is not None:
                        c = di + ih # largo del camino via "i"
                        if (desde, hasta) not in self.d or c < self.d[(desde, hasta)]:
                            self.d[(desde, hasta)] = c # mejora al camino actual
        with open("Floyd-Warshallprueba1.dat", "at") as archivo:
            print(self.d, file=archivo)
        return self.d

    def promediodistancias(self):
        for key, value in self.d.items():
            self.suma= self.suma+value
        return self.suma/n

    def promclusters(self):
        csuma=0
        for v in range(len(self.V)):
            m=0
            for i in self.vecinos[v]:
                for b in self.vecinos[v]:
                    if b in self.vecinos[v]:
                        m += 1
            csuma += m/(n*(n-1))
        return csuma/len(self.V)

    def cota(self):
        circumferencelength= 2*(pi)*r
        supremo=circumferencelength/(len(self.d)/k)-n
        if supremo> self.suma/n:
            return (self.suma/n)/supremo

    def archivo(self):
        with open("prueba1.plot", "w") as archivo:
            print("set term eps", file=archivo)
            print("set output 'prueba1.eps'", file=archivo)
            print("set pointsize 1", file=archivo)
            print("set xrange[{:f}:{:f}]".format(0, 10), file=archivo)
            print("set yrange[{:f}:{:f}]".format(0, 10), file=archivo)
            print("set size square", file=archivo)
            print("set key off", file=archivo)
            num=1
            for a in self.E:
                n1=a[0]
                n2=a[1]
                x1=self.V[n1][0]
                y1=self.V[n1][1]
                x2=self.V[n2][0]
                y2=self.V[n2][1]
                print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead".format(num, x1, y1, x2, y2), file=archivo)
                num += 1
            print("show arrow", file=archivo)
            print("plot 'prueba1.dat' using 1:2 with points pt 7", file=archivo)
            print("quit()", file=archivo)

n=12
k=4
if fmod(n,2)==0:
    if  k>=floor(n/2):
        print("El valor dado a k no es un valor permitido")
    else:
        r=0.3
        prob=ceil((0.15)*n)
        G=GrafoYessica()
        c=(0.5,0.5)
        angulo=2*pi/n
        for v in range (0,n):
            G.nodoscrear(v)
        G.conecta(k)
        G.conectaaleatorio(prob)
        G.archivo()
        G.floyd_warshall()
        with open("Resultadoaverageprueba1.dat", "at") as h:
            print(G.promediodistancias(), h=file)
        with open("Resultadoclusterprueba1.dat", "at") as o:
            print(G.promclusters(), o=file)
        with open("Resultad/s.dat", "at") as q:
            print(G.cota(), q=file)
else:
    if k>=floor((n-1)/2):
        print("El valor dado a k no es un valor permitido")
    else:
        r=0.3
        prob=ceil((0.15)*n)
        G=GrafoYessica()
        c=(0.5,0.5)
        angulo=2*pi/n
        for v in range (0,n):
            G.nodoscrear(v)
        G.conecta(k)
        G.conectaaleatorio(prob)
        G.archivo()
        G.floyd_warshall()
        with open("Resultadoaverageprueba1.dat", "at") as h:
            print(G.promediodistancias(), file=h)
        with open("Resultadoclusterprueba1.dat", "at") as l:
            print(G.promclusters(), file=l)
        with open("Resultad/s.dat", "at") as q:
            print(G.cota(), file=q)
