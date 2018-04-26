from random import random, randint, normalvariate, expovariate

class GrafoYessica:
    def __init__(self):
        self.n=0
        self.d = {}
        self.V= dict()
        self.E=dict()
        self.pesos=dict()
        self.vecinos=dict()
        self.pos=dict()
        with open ("cuadricula1.dat", "w") as f:
            print("", end="",file=f)

    def manhattan(self,n1,n2):
        x1=self.V[n1][0]
        y1=self.V[n1][1]
        x2=self.V[n2][0]
        y2=self.V[n2][1]
        return abs(x1-x2)+abs(y1-y2)
        
    def nodoscrear(self):
        v=0
        for i in range (0,k):
            for j in range (0,k):
                v +=1
                x=i+1
                y=j+1
                self.V[v]=(x,y)
                with open ("cuadricula1.dat", "a") as salida:
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
                    self.pesos[(x1,y1),(x2,y2)]=self.pesos[(x2,y2),(x1,y1)]=normalvariate(1, 0.5)
                    self.E[(i,j)]=self.E[(i,j)]=0
                    self.vecinos[i].add(j)
                    self.vecinos[j].add(i)

    def conectaaleatorio(self, prob):
        for m in range(len(self.V)):
            for w in range(len(self.V)):
                if m is not w and (m,w) not in self.E:
                    if random()< prob:
                        x1=self.V[i][0]
                        y1=self.V[i][1]
                        x2=self.V[j][0]
                        y2=self.V[j][1]
                        self.pesos[(x1,y1),(x2,y2)]=self.pesos[(x2,y2),(x1,y1)]=expovariate(0.1)
                        self.E[(m,w)]=self.E[(w,m)]=0
                        self.vecinos[m].add(w)
                        self.vecinos[w].add(m)

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
 
    def ford_fulkerson(self): # algoritmo de Ford y Fulkerson
        self.s=(self.V[91][0],self.V[91][1])
        self.t=(self.V[10][0],self.V[10][1])
        if self.s == self.t:
            return 0
        maximo = 0
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
            maximo += incr
        return maximo

    def archivo(self):
        with open("cuadricula1.plot", "w") as archivo:
            print("set term eps", file=archivo)
            print("set output 'cuadricula1.eps'", file=archivo)
            print("set pointsize 1", file=archivo)
            print("set xrange[{:d}:{:d}]".format(0, k+1), file=archivo)
            print("set yrange[{:d}:{:d}]".format(0, k+1), file=archivo)
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
            print("plot 'cuadricula1.dat' using 1:2 with points pt 7", file=archivo)
            print("quit()", file=archivo)

k=10
l=1
prob=2^(-3)
G=GrafoYessica()
G.nodoscrear()
G.conecta(l)
G.conectaaleatorio(prob)
print(G.ford_fulkerson())
G.archivo()
