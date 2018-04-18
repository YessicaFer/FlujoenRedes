from random import random, randint
from math import sqrt, cos, pi, sin

class GrafoYessica:
    def __init__(self):
        self.n=0
        self.d = {}
        self.V= dict()
        self.E=dict()
        self.vecinos=dict()
        self.pos=dict()
        with open ("p3-cap.dat", "w") as f:
            print("", end="",file=f)
        
    def nodoscrear(self, v):
        self.pos[v] = (c[0]+(0.3 * cos(angulo * v)), c[1]+(0.3 * sin(angulo * v)))
        x= self.pos[v][0]
        y=self.pos[v][1]
        self.V[v]=(x,y)
        with open ("p3-cap.dat", "a") as salida:
            print(x, y, file=salida)
        if not v in self.vecinos:
            self.vecinos[v]=set()

    def conecta(self, v, k):
        self.E[(v, u)] = self.E[(u, v)]=k
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)

    def euclidiana(self,n1,n2):
        x1=self.V[n1][0]
        y1=self.V[n1][1]
        x2=self.V[n2][0]
        y2=self.V[n2][1]
        return sqrt( ((x1-x2)**2)+((y1-y2)**2) )

    def floyd_warshall(self):
        for z in range(len(self.V)):
            self.d[(z, z)] = self.E[(z,z)]=0 # distancia reflexiva es cero
            for u in range(len(self.E)): # para vecinos, la distancia es el peso
                if (z,u) in self.E:
                    self.d[(z, u)] = self.E[(z,u)]
                else:
                    self.d[(z, u)] = 0
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
        with open("Floyd-Warshallpepinillo.dat", "at") as archivo:
            print(self.d, file=archivo)
        return self.d

    def archivo(self):
        with open("p3-cap.plot", "w") as archivo:
            print("set term eps", file=archivo)
            print("set output 'p3-cap.eps'", file=archivo)
            print("set xrange [-.1:1.1]", file=archivo)
            print("set yrange [-.1:1.1]", file=archivo)
            print("set pointsize 1", file=archivo)
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
            print("plot 'p3-cap.dat' using 1:2 with points pt 7", file=archivo)
            print("quit()", file=archivo)

n=10
k=1
G=GrafoYessica()
c=(0.5,0.5)
angulo=2*pi/n
for v in range (0,n):
    G.nodoscrear(v)
for v in range (0,n):
    for u in range(1, k+1):
        G.conecta(v,k)
G.archivo()
G.floyd_warshall()
#print(G.promediodistancias())
#print(G.promclusters())
