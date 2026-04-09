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
def remover_dado(r,g,n):
    r.append(g[n])
    g.pop(n)
    return [r,g]
def calcula_pontos_regra_simples(f):
    d={1:0,2:0,3:0,4:0,5:0,6:0}
    for i in range(len(f)):
        if f[i]==1:
            d[1]+=1
        elif f[i]==2:
            d[2]+=2
        elif f[i]==3:
            d[3]+=3
        elif f[i]==4:
            d[4]+=4
        elif f[i]==5:
            d[5]+=5
        elif f[i]==6:
            d[6]+=6
    return d
def calcula_pontos_soma(lista):
    valor=0
    for o in range(len(lista)):
        valor+=lista[o]
    return valor
def calcula_pontos_sequencia_baixa(r):
    x=0
    r.sort()
    for i in range(len(r)-1):
        if r[i+1]==r[i]+1:
            x+=1
    if x==3:
        return 15
    else:
        return 0
