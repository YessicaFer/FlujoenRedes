
from random import random, choice, randint
from math import sqrt, floor, ceil

class GrafoYessica:
    def __init__(self):
        self.n=0
        self.V=dict()
        self.aristas = []
        self.orientado = True # Verdadero
        with open ("prueba1.dat", "w") as f:
            print("", end="",file=f)
        
    def nodoscrear(self, v, x, y, c, d):
        self.V[v]=(x,y,c,d)
        with open ("prueba1.dat", "a") as salida:
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
        self.aristas.append((n1, n2, f, capacidad))

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
        d = {}
        for z in range(len(self.V)):
            d[(z, z)] = 0 # distancia reflexiva es cero
            for u in range (len(self.aristas)): # para vecinos, la distancia es el peso
                point1=self.aristas[u][0]
                point2=self.aristas[u][1]
                d[(point1, point2)] = self.aristas[u][3]
        for intermedio in range(len(self.V)):
            for desde in range(len(self.V)):
                for hasta in range(len(self.V)):
                    di = None
                    if (desde, intermedio) in d:
                        di = d[(desde, intermedio)]
                    ih = None
                    if (intermedio, hasta) in d:
                        ih = d[(intermedio, hasta)]
                    if di is not None and ih is not None:
                        c = di + ih # largo del camino via "i"
                        if (desde, hasta) not in d or c < d[(desde, hasta)]:
                            d[(desde, hasta)] = c # mejora al camino actual
        return d

    def camino(self): # construcción de un camino aumentante
        cola = [self.s]
        usados = set()
        camino = dict()
        while len(cola) > 0:
            u = cola.pop(0)
            usados.add(u)
            for (w, v) in self.c:
                if w == u and v not in cola and v not in usados:
                    actual = flujo.get((u, v), 0)
                    dif = self.c[(u, v)] - actual
                    if dif > 0:
                        cola.append(v)
                        camino[v] = (u, dif)
        if self.t in usados:
            return camino
        else: # no se alcanzó
            return None
 
    def ford_fulkerson(self): # algoritmo de Ford y Fulkerson
        for q in range (len(self.V)):
            for k in range(len(self.V)):
                if q is not k and self.V[q][2] == self.V[k][2]:
                    self.s=self.V[q]
                    self.t=self.V[k]
                else:
                    q+=1
                    k+=1
        if self.s == self.t:
            return 0
        maximo = 0
        flujo = dict()
        while True:
            self.c=self.floyd_warshall()
            aum = self.camino()
            if aum is None:
                break # ya no hay
            incr = min(aum.values(), key = (lambda k: k[1]))[1]
            u = self.t
            while u in aum:
                v = aum[u][0]
                actual = flujo.get((v, u), 0) # cero si no hay
                inverso = flujo.get((u, v), 0)
                flujo[(v, u)] = actual + incr
                flujo[(u, v)] = inverso - incr
                u = v
            maximo += incr
        return maximo

    def archivo(self):
        with open("tarea2.plot", "w") as archivo:
            print("set term eps", file=archivo)
            print("set output 'grafica2.eps'", file=archivo)
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
                if self.orientado is True:
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} head filled size 0.04,8 lt {:d} dashtype {:d}".format(num, x1, y1, x2, y2, a[2], a[3]), file=archivo)
                else:
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lt {:d} dashtype {:d}".format(num, x1, y1, x2, y2, a[2], a[3]), file=archivo)
                num += 1
            print("show arrow", file=archivo)
            print("plot 'prueba1.dat' using 1:2:3:4 with points pt var lc palette var", file=archivo)
            print("quit()", file=archivo)
            
n=30
G=GrafoYessica()
for v in range (n):
    G.nodoscrear(v, random(), random(), choice([5,7,9,13]), random())
G.menorentredos()
G.archivo()
print(G.floyd_warshall())
print(G.ford_fulkerson())
