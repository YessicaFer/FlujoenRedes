from random import random, choice, randint, randrange
from math import sqrt, floor, ceil
import time

class GrafoYessica:
    def __init__(self):
        self.n=0
        self.d= {}
        self.V=dict()
        self.vecinos=dict()
        self.aristas = []
        self.pesos=dict()
        with open ("avp1.dat", "w") as f:
            print("", end="",file=f)
        
    def nodoscrear(self, v, x, y, c, d):
        self.V[v]=(x,y,c,d)
        if not v in self.vecinos:
            self.vecinos[v]=set()
        with open ("avp1.dat", "a") as salida:
            print(x, y, c, d, file=salida)

    def euclidiana(self,n1,n2):
        x1=self.V[n1][0]
        y1=self.V[n1][1]
        x2=self.V[n2][0]
        y2=self.V[n2][1]
        return sqrt( ((x1-x2)**2)+((y1-y2)**2) )
            

    def conectar(self, n1, n2, f, capacidad):
        # n1 : índice del nodo "desde"
        # n2 : índice del nodo "hasta"
        # peso : peso del arco entre n1 y n2; por defecto (si no pones nada) es 1
        if orientado is True:
            self.aristas.append((n1, n2, f, capacidad))
            self.vecinos[n1].add(n2)
            x1=self.V[n1][0]
            y1=self.V[n1][1]
            x2=self.V[n2][0]
            y2=self.V[n2][1]
            if capacidad==1:
                tamaño=randint(1,5)
                self.pesos[(x1,y1),(x2,y2)]=tamaño
            if capacidad==2:
                tamaño=randint(6,10)
                self.pesos[(x1,y1),(x2,y2)]=tamaño
            if capacidad==3:
                tamaño=randint(11,15)
                self.pesos[(x1,y1),(x2,y2)]=tamaño
            if capacidad==4:
                tamaño=randint(16,20)
                self.pesos[(x1,y1),(x2,y2)]=tamaño
            if capacidad==5:
                tamaño=randint(21,25)
                self.pesos[(x1,y1),(x2,y2)]=tamaño
        else:
            self.aristas.append((n1, n2, f, capacidad))
            self.aristas.append((n2, n1, f, capacidad))
            self.vecinos[n1].add(n2)
            self.vecinos[n2].add(n1)
            x1=self.V[n1][0]
            y1=self.V[n1][1]
            x2=self.V[n2][0]
            y2=self.V[n2][1]
            if capacidad==1:
                tamaño=randint(1,5)
                self.pesos[(x1,y1),(x2,y2)]=tamaño
                self.pesos[(x2,y2),(x1,y1)]=tamaño
            if capacidad==2:
                tamaño=randint(6,10)
                self.pesos[(x1,y1),(x2,y2)]=tamaño
                self.pesos[(x2,y2),(x1,y1)]=tamaño
            if capacidad==3:
                tamaño=randint(11,15)
                self.pesos[(x1,y1),(x2,y2)]=tamaño
                self.pesos[(x2,y2),(x1,y1)]=tamaño
            if capacidad==4:
                tamaño=randint(16,20)
                self.pesos[(x1,y1),(x2,y2)]=tamaño
                self.pesos[(x2,y2),(x1,y1)]=tamaño
            if capacidad==5:
                tamaño=randint(21,25)
                self.pesos[(x1,y1),(x2,y2)]=tamaño
                self.pesos[(x2,y2),(x1,y1)]=tamaño

    def yoconecto(self,n):
        if orientado is True:
            t=1
            while t<n:
                q=randrange(0, n)
                p=randrange(0, n)
                f=randrange(0, 10)
                peso=choice([1,2,3,4,5])
                #self.aristas.append((q, p, f, peso))
                if q is not p and (q, p, f, peso) not in self.aristas:
                    self.aristas.append((q, p, f, peso))
                    self.vecinos[q].add(p)
                    x1=self.V[q][0]
                    y1=self.V[q][1]
                    x2=self.V[p][0]
                    y2=self.V[p][1]
                    if peso==1:
                        tamaño=randint(1,5)
                        self.pesos[(x1,y1),(x2,y2)]=tamaño
                    if peso==2:
                        tamaño=randint(6,10)
                        self.pesos[(x1,y1),(x2,y2)]=tamaño
                    if peso==3:
                        tamaño=randint(11,15)
                        self.pesos[(x1,y1),(x2,y2)]=tamaño
                    if peso==4:
                        tamaño=randint(16,20)
                        self.pesos[(x1,y1),(x2,y2)]=tamaño
                    if peso==5:
                        tamaño=randint(21,25)
                        self.pesos[(x1,y1),(x2,y2)]=tamaño
                t+= 1
                
        else:
            t=1
            while t<n:
                q=randrange(0, n)
                p=randrange(0, n)
                f=randrange(0, 10)
                peso=choice([1,2,3,4,5])
                if q!=p and (q, p, f, peso) not in self.aristas:
                    self.aristas.append((q, p, f, peso))
                    self.vecinos[q].add(p)
                    x1=self.V[q][0]
                    y1=self.V[q][1]
                    x2=self.V[p][0]
                    y2=self.V[p][1]
                    if peso==1:
                        tamaño=randint(1,5)
                        self.pesos[(x1,y1),(x2,y2)]=self.pesos[(x2,y2),(x1,y1)]=tamaño
                    if peso==2:
                        tamaño=randint(6,10)
                        self.pesos[(x1,y1),(x2,y2)]=self.pesos[(x2,y2),(x1,y1)]=tamaño
                    if peso==3:
                        tamaño=randint(11,15)
                        self.pesos[(x1,y1),(x2,y2)]=self.pesos[(x2,y2),(x1,y1)]=tamaño
                    if peso==4:
                        tamaño=randint(16,20)
                        self.pesos[(x1,y1),(x2,y2)]=self.pesos[(x2,y2),(x1,y1)]=tamaño
                    if peso==5:
                        tamaño=randint(21,25)
                        self.pesos[(x1,y1),(x2,y2)]=self.pesos[(x2,y2),(x1,y1)]=tamaño
                t+= 1   

    def menorentredos(self):
        for x in range(len(self.V)):
            f = randint(0, 10)
            for i in range(len(self.V)):
                for w in range(len(self.V)):
                    if x is not i and x is not w and i is not w:
                        xi=self.euclidiana(x,i)
                        xw=self.euclidiana(x,w)
                        if xi<xw:
                            if self.euclidiana(x,i)<0.4:
                                if self.V[x][2]==self.V[i][2]:
                                    peso=choice([1,2,3,4,5])
                                    self.conectar(x,i,f,peso)

                        else:
                            if self.euclidiana(x,w)<0.4:
                                if self.V[x][2]==self.V[w][2]:
                                    peso=choice([1,2,3,4,5])
                                    self.conectar(x,w,f,peso)
                                    
    def floyd_warshall(self):
        for z in range(len(self.V)):
            self.d[(z, z)] = 0 # distancia reflexiva es cero
            for u in self.vecinos[z]: # para vecinos, la distancia es el peso
                self.d[(z, u)] = self.aristas[u][3]
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
        with open("Floyd-Warshall.dat", "at") as archivo:
            print(self.d, file=archivo)
        return self.d

    def promediodistancias(self):
        suma = 0
        for key, value in self.d.items():
            suma= suma+value
        return suma/n

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

    def cota_superior(self):
        

    def archivo(self):
        with open("avp1.plot", "w") as archivo:
            print("set term eps", file=archivo)
            print("set output 'avp1.eps'", file=archivo)
            print("set xrange [-.1:1.1]", file=archivo)
            print("set yrange [-.1:1.1]", file=archivo)
            print("set pointsize 1", file=archivo)
            print("set size square", file=archivo)
            print("set key off", file=archivo)
            num=1
            for a in self.aristas:
                n1=a[0]
                n2=a[1]
                x1=self.V[n1][0]
                y1=self.V[n1][1]
                x2=self.V[n2][0]
                y2=self.V[n2][1]
                if orientado is True:
                    if cap is False:
                        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} head filled size 0.04,8 lt {:d}".format(num, x1, y1, x2, y2, a[2]), file=archivo)
                    else:
                        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} head filled size 0.04,8 lt {:d} dashtype {:d}".format(num, x1, y1, x2, y2, a[2], a[3]), file=archivo)
                else:
                    if cap is False:
                        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lt {:d}".format(num, x1, y1, x2, y2, a[2]), file=archivo)
                    else:
                        print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lt {:d} dashtype {:d}".format(num, x1, y1, x2, y2, a[2], a[3]), file=archivo)
                num += 1
            print("show arrow", file=archivo)
            print("plot 'avp1.dat' using 1:2:3:4 with points pt var lc palette var", file=archivo)
            print("quit()", file=archivo)
            
cap = True #Si cap=True el grafo sera con ponderacion en las aristas/False para no agregar ponderacion
orientado = True #Si orientado=True el grafo sera con orientacion en las aristas/False para no agregar orientacion

n= 30
G=GrafoYessica()
for v in range (n):
    G.nodoscrear(v, random(), random(), choice([5,7,9,13]), random())
G.menorentredos()
G.yoconecto(n)
G.archivo()
G.floyd_warshall()
print(G.promediodistancias())
print(G.promclusters())
