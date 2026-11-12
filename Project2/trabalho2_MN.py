
#________________________________________________________________________________________________________________________
#__________________________________EXERCÍCIO 1  Método das Bisseções Sucessivas__________________________________________
#________________________________________________________________________________________________________________________

import math

def f(x):
    return math.sin(x**2)+1.1-math.e**(-x)
def bisse_sucessivas(a, b, epsilon):
    erroiter = abs(b-a)
    count = 0
    #a = -0.2
    #b = -0.1 
    while(erroiter > epsilon):
        m = (a + b) / 2

        if (f(m) == 0):
            erroiter=0
        elif (f(a) * f(m) < 0):
            b = m
        elif (f(b) * f(m) < 0):
            a = m 
        
        count += 1
        erroiter /= 2

    return m, erroiter, count


print("\nEXERCÍCIO 1: Método das Bisseções Sucessivas\n")
resultado, erro_majorado, n_iter = bisse_sucessivas(-0.2, -0.1, 5*10**-9)
print (f"raiz: {resultado} +- {erro_majorado} ---> iterações: {n_iter}\n")
print("\n__________________________________________________________________________________________________\n")

#________________________________________________________________________________________________________________________
#__________________________________________EXERCÍCIO 1 Método de Newton__________________________________________________
#________________________________________________________________________________________________________________________

def f(x): # 
    return math.sin(x**2)+1.1-math.e**(-x)

def f_derivada(x):
    return 2*x*math.cos(x**2)+math.e**(-x)

def f_derivada2(x):
    return 2*math.cos(x**2)-4*math.sin(x**2)-math.e**(-x)

def g(x):
    return x - f(x)/f_derivada(x)

def newton_metodo(x0, a, b, erro):
    #a=-0,2; b=-0,1 [-0,2;-0,1]
    M = (f_derivada2(a) / f_derivada(a)) * (1/2)
    erro_majorado2 = abs(b-a)
    n = 0
    while erro_majorado2 > erro:
        x1 = g(x0)
        erro_majorado2 = M * erro_majorado2**2
        x0 = x1
        n += 1
    return x0, erro_majorado2, n

print("\nEXERCÍCIO 1: Método de Newton\n")
resultado, erro_majorado, n_iter = newton_metodo(-0.1,-0.2, -0.1, 5*10**-9)
print (f"raiz: {resultado} +- {erro_majorado} ---> iterações: {n_iter}\n")
print("\n__________________________________________________________________________________________________\n")

#________________________________________________________________________________________________________________________
#__________________________________________________EXERCÍCIO  2__________________________________________________________
#________________________________________________________________________________________________________________________

def g1(x):
    #x = g1(x) = x − x**3 − 4*x**2 + 10
    return x - x**3 - 4*x**2 + 10

def g2(x):
    #x = g2(x) = math.sqrt((10/x) - 4*x)
    return math.sqrt((10/x) - 4*x)



def g4(x):
    #x = g4(x) = math.sqrt(10/(4 + x))
    return math.sqrt(10/(4 + x))

def g5(x):
    #x = g5(x) = (2*x**3 + 4*x**2 + 10)/(3*x**2 + 8*x)

    return (2*x**3 + 4*x**2 + 10)/(3*x**2 + 8*x)


