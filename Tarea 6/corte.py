from random import random, randint, normalvariate, expovariate, uniform, choice
from math import floor, ceil
import time

class GrafoYessica:
    def __init__(self):
        self.n=0
        self.d = {}
        self.V= dict()
        self.B=dict()
        self.E=dict()
        self.pesos=dict()
        self.peso=dict()
        self.vecinos=dict()
        self.aristas=dict()
        self.elegidos=set()
        self.pos=dict()
        with open ("percolara2.dat", "w") as f:
            print("", end="",file=f)

    def manhattan(self,n1,n2):
        x1=self.V[n1][0]
        y1=self.V[n1][1]
        x2=self.V[n2][0]
        y2=self.V[n2][1]
        return abs(x1-x2)+abs(y1-y2)

    def puntomedio(self,n1,n2):
        x1=self.V[n1][0]
        y1=self.V[n1][1]
        x2=self.V[n2][0]
        y2=self.V[n2][1]
        return (((x1+x2)/2),((y1+y2)/2))

    def puntomedio1(self,n1,n2):
        c1=self.B[n1][1]
        c2=self.B[n2][1]
        x1=self.B[c1][0]
        y1=self.B[c1][1]
        x2=self.B[c2][0]
        y2=self.B[c2][1]
        return (((x1+x2)/2),((y1+y2)/2))
        
    def nodoscrear(self):
        v=0
        for i in range (0,k):
            for j in range (0,k):
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
            w=randint(1,k**2)
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

    def idea2(self):
        b=0
        while b!=(len(self.V)/2):
            m=randint(1,k**2)
            w=randint(1,k**2)
            if m!=w:
                if m not in self.elegidos:
                    if w not in self.elegidos:
                        b+=1
                        self.B[b]=((m,w), self.puntomedio(m,w))
                        c=self.B[b][1]
                        x=c[0]
                        y=c[1]
                        self.elegidos.add(m)
                        self.elegidos.add(w)
                        with open ("percolara2.dat", "a") as salida:
                            print(x, y, file=salida)
                        for i in range(len(self.E)):
                            a=i+1
                            if (m,a) and (a,m) in self.E:
                                if a!=m or a!=w:
                                    self.aristas[(a,m|w)]=self.aristas[(m|w,a)]=0
                                    x1=self.V[m][0]
                                    y1=self.V[m][1]
                                    x2=self.V[a][0]
                                    y2=self.V[a][1]
                                    self.peso[(x1,y1),(x2,y2)]=self.pesos[(x1,y1),(x2,y2)]
                                    self.peso[(x2,y2),(x1,y1)]=self.pesos[(x2,y2),(x1,y1)]

    def parejas(self):
        a=0
        while a<=(len(self.B)/2):
            m=randint(1,len(self.B))
            w=randint(1,len(self.B))
            if m!=w:
                if m not in self.elegidos:
                    if w not in self.elegidos:
                        a+=1
                        x=self.B[1][0]
                        y=self.B[1][1]
                        id1=self.B[m][0]
                        id2=self.B[w][0]
                        self.B[a]=((id1,id2), self.puntomedio1(m,w))
                        self.elegidos.add(m)
                        self.elegidos.add(w)
                        with open ("percolara2.dat", "a") as salida:
                            print(x, y, file=salida)
                

    def archivo(self,k):
        with open("percolara2.plot", "w") as archivo:
            print("set term eps", file=archivo)
            print("set output 'percolara2.eps'", file=archivo)
            print("set pointsize 1", file=archivo)
            print("set xrange[{:d}:{:d}]".format(0, k+1), file=archivo)
            print("set yrange[{:d}:{:d}]".format(0, k+1), file=archivo)
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

k=4
l=1
prob=0.00
G=GrafoYessica()
G.nodoscrear()
G.conecta(l)
G.archivo(k)
G.idea2()
G.parejas()
