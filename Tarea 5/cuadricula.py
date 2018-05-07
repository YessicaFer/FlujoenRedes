from random import random, randint, normalvariate, expovariate, uniform, choice
from math import floor, ceil
import time

class GrafoYessica:
    def __init__(self):
        self.n=0
        self.d = {}
        self.V= dict()
        self.E=dict()
        self.pesos=dict()
        self.vecinos=dict()
        self.pos=dict()
        with open ("percolara2.dat", "w") as f:
            print("", end="",file=f)

    def manhattan(self,n1,n2):
        x1=self.V[n1][0]
        y1=self.V[n1][1]
        x2=self.V[n2][0]
        y2=self.V[n2][1]
        return abs(x1-x2)+abs(y1-y2)
        
    def nodoscrear(self):
        v=0
        for i in range (0,n):
            for j in range (0,n):
                v +=1
                x=i+1
                y=j+1
                self.V[v]=(x,y)
                with open ("percolara2.dat", "a") as salida:
                    print(x, y, file=salida)
                if not v in self.vecinos:
                    self.vecinos[v]=set()

    def conecta(self, l):
        for i in range(1, len(self.V)+1):
            for j in range(1, len(self.V)+1):
                if i is not j and self.manhattan(i,j)<=l:
                    x1=self.V[i][0]
                    y1=self.V[i][1]
                    x2=self.V[j][0]
                    y2=self.V[j][1]
                    self.pesos[(x1,y1),(x2,y2)]=self.pesos[(x2,y2),(x1,y1)]=floor(normalvariate(5, 5**(1/2)))
                    self.E[(i,j)]=self.E[(j,i)]=0
                    self.vecinos[i].add(j)
                    self.vecinos[j].add(i)

        for m in range(1, len(self.V)+1):
            w=randint(1,k)
            if m is not w and (m,w) not in self.E:
                if random()< prob:
                    x1=self.V[m][0]
                    y1=self.V[m][1]
                    x2=self.V[w][0]
                    y2=self.V[w][1]
                    self.pesos[(x1,y1),(x2,y2)]=self.pesos[(x2,y2),(x1,y1)]=ceil(expovariate(0.1))
                    self.E[(m,w)]=self.E[(w,m)]=0
                    self.vecinos[m].add(w)
                    self.vecinos[w].add(m)

    def percolacion(self,nodo,arista,l):
        a=0
        if nodo is True:
            m=randint(1,k)
            if m in self.vecinos:
                del self.vecinos[m]
                for i in range(len(self.E)):
                    b=i+1
                    if b != m and (b,m) in self.E:
                        if (m,b) in self.E and m in self.V and b in self.V:
                            x1=self.V[m][0]
                            y1=self.V[m][1]
                            x2=self.V[b][0]
                            y2=self.V[b][1]
                            if ((x1,y1),(x2,y2)) in self.pesos:
                                del self.E[(m,b)]
                                del self.E[(b,m)]
                                del self.pesos[(x1,y1),(x2,y2)]
                                del self.pesos[(x2,y2),(x1,y1)]
        else:
            if arista is True:
                while a!=4:
                    m=randint(1,k)
                    g=choice([m+l,m+n,m-n,m-1,(m+n+1),(m+n-1),(m-n+1),(m-n-1)])
                    if (g,m) in self.E:
                        if (m,g) in self.E and m in self.V and g in self.V:
                            x1=self.V[m][0]
                            y1=self.V[m][1]
                            x2=self.V[g][0]
                            y2=self.V[g][1]
                            if ((x1,y1),(x2,y2)) in self.pesos:
                                a+=1
                                del self.E[(m,g)]
                                del self.E[(g,m)]
                                del self.pesos[(x1,y1),(x2,y2)]
                                del self.pesos[(x2,y2),(x1,y1)]
                    else:
                        m=randint(1,k)
                        g=choice([m+l,m+n,m-n,m-1,(m+n+1),(m+n-1),(m-n+1),(m-n-1)])
                        if (g,m) in self.E:
                            if (m,g) in self.E and m in self.V and g in self.V:
                                x1=self.V[m][0]
                                y1=self.V[m][1]
                                x2=self.V[g][0]
                                y2=self.V[g][1]
                                if ((x1,y1),(x2,y2)) in self.pesos:
                                    a+=1
                                    del self.E[(m,g)]
                                    del self.E[(g,m)]
                                    del self.pesos[(x1,y1),(x2,y2)]
                                    del self.pesos[(x2,y2),(x1,y1)]
                        
    def camino(self): # construcción de un camino aumentante
        cola = [self.s]
        usados = set()
        camino = dict()
        while len(cola) > 0:
            u = cola.pop(0)
            usados.add(u)
            for ((w, v)) in self.pesos:
                if w == u and v not in cola and v not in usados:
                    actual = self.flujo.get((u, v), 0)
                    dif = self.pesos[(u, v)] - actual
                    if dif > 0:
                        cola.append(v)
                        camino[v] = (u, dif)
        if self.t in usados:
            return camino
        else:
            return None
 
    def ford_fulkerson(self, s, t): # algoritmo de Ford y Fulkerson
        self.s=(self.V[s][0],self.V[s][1])
        self.t=(self.V[t][0],self.V[t][1])
        if self.s == self.t:
            return 0
        self.maximo = 0
        self.flujo = dict()
        while True:
            aum = self.camino()
            if aum is None:
                break # ya no hay
            incr = min(aum.values(), key = (lambda k: k[1]))[1]
            u = self.t
            while u in aum:
                v = aum[u][0]
                actual = self.flujo.get((v, u), 0) # cero si no hay
                inverso = self.flujo.get((u, v), 0)
                self.flujo[(v, u)] = actual + incr
                self.flujo[(u, v)] = inverso - incr
                u = v
            self.maximo += incr
        if percolar is True:
            filename="Ford-Fulkersonpercolara2v.csv"
            with open(filename, "at") as archivo:
                print(self.maximo, file=archivo)
        else:
            filename="Ford-Fulkerson2v.csv"
            with open(filename, "at") as archivo:
                print(self.maximo, file=archivo)
        return self.maximo

    def archivo(self,k):
        with open("percolara2.plot", "w") as archivo:
            print("set term eps", file=archivo)
            print("set output 'percolara2.eps'", file=archivo)
            print("set pointsize 0.8", file=archivo)
            print("set xrange[{:d}:{:d}]".format(0, n+1), file=archivo)
            print("set yrange[{:d}:{:d}]".format(0, n+1), file=archivo)
            print("set size square", file=archivo)
            print("unset xtics", file=archivo)
            print("unset ytics", file=archivo)
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
            print("plot 'percolara2.dat' using 1:2 with points pt 7", file=archivo)
            print("quit()", file=archivo)

arista=True
nodo=True
percolar=True
filename="tiempopercolaciona2v.csv"
n=10
if percolar is True:
    with open(filename,"at") as hile:
        k=n*n
        l=2
        prob=0.003
        G=GrafoYessica()
        G.nodoscrear()
        G.conecta(l)
        start_time = time.clock()
        pasta=G.ford_fulkerson((10*10)-(10-1),10)
        print (time.clock() - start_time, file=hile)
        while pasta>0:
            G.percolacion(nodo,arista,l)
            start_time = time.clock()
            pasta=G.ford_fulkerson((10*10)-(10-1),10)
            print (time.clock() - start_time, file=hile)
        G.archivo(k)
else:
    with open(filename,"at") as hile:
        k=n*n
        l=2
        prob=0.03
        G=GrafoYessica()
        G.nodoscrear()
        G.conecta(l)
        start_time = time.clock()
        G.ford_fulkerson((5*5)-(5-1),5)
        print (time.clock() - start_time, file=hile)
        G.archivo(k)
