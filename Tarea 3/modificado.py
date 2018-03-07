
from random import random, choice, randint
from math import sqrt, floor, ceil

def euclidiana(ñ,r):
    return ((((ñ[0]-r[0])**2)+((ñ[1]-r[1])**2))**(0.5))

class GrafoYessica:
    def __init__(self):
        self.n=0
        self.V=dict()
        self.aristas = []
        self.orientado = True # Verdadero
        self.capacitado = True #Verdadero
        with open ("prueba1.dat", "w") as f:
            print("", end="",file=f)
        
    def nodoscrear(self, v, x, y, c, d):
        self.V[v]=(x,y,c,d)
        with open ("prueba1.dat", "a") as salida:
            print(x, y, c, d, file=salida)
            

    def conectar(self, n1, n2, peso=1):
        # n1 : índice del nodo "desde"
        # n2 : índice del nodo "hasta"
        # peso : peso del arco entre n1 y n2; por defecto (si no pones nada) es 1
        f = randint(0, 10)
        self.aristas.append((n1, n2, f, peso))

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
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} lt {:d} dashtype {:d}".format(num, x1, y1, x2, y2, a[2], a[3]), file=archivo)
                else:
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lt {:d} dashtype {:d}".format(num, x1, y1, x2, y2, a[2], a[3]), file=archivo)
                num += 1
            print("show arrow", file=archivo)
            print("plot 'prueba1.dat' using 1:2:3:4 with points pt var lc palette var", file=archivo)
            print("quit()", file=archivo)

            
n=20
G=GrafoYessica()
for v in range (n):
    G.nodoscrear(v, random(), random(), choice([5,7,9,13]), random())
for n1 in range (n):
    for n2 in range(n):
        G.conectar(n1,n2,choice([1,2,3,4,5]))
        
G.archivo()
#G.ford_fulkerson(aristas,1,20)
