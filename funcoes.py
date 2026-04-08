import math
import random
def rolar_dados(x):
    valores=[]
    for i in range(x):
        valores.append(random.randint(1,6))
    return valores
