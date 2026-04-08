import math
import random
def rolar_dados(x):
    valores=[]
    for i in range(x):
        valores.append(random.randint(1,6))
    return valores
def guardar_dado(r,g,n):
    g.append(r[n])
    r.pop(n)
    return [r,g]