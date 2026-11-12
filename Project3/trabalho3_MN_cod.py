import numpy as np
import sympy as sp


        # Definir a função matemática f(x)
def f(val):
    return val**2 + np.sin(6*val)

# Criar 8 pontos igualmente espaçados entre -1 e 1
# n+1 = 8 pontos, logo n = 7 (grau do polinómio)
x_dados = np.linspace(-1, 1, 8)
y_dados = f(x_dados)

def calcular_termos_Lk_simbolicos(x_lista, x_simbolo):
    """
    Cria uma lista com todas as expressões algébricas L_k(x).
    Esta é a função explícita pedida para calcular os Lk.
    """
    n = len(x_lista)
    lista_Lk = []
    
    # Para cada nó k (de 0 a 7)
    for k in range(n):
        L_k = 1  # (elemento neutro)
        
        #Loop que percorre 
        for j in range(n):
            if j != k:
                # fórmula: (x - xj) / (xk - xj)
                numerador = x_simbolo - x_lista[j]
                denominador = x_lista[k] - x_lista[j]
                
                # Multiplica ao termo acumulado
                L_k = L_k * (numerador / denominador)
        
        lista_Lk.append(L_k)
        
    return lista_Lk

def resolver_lagrange_completo():
     
    # Defenir a variável 'x' para usar nas equações
    x = sp.symbols('x')
    
    # 2. Calcular todos os Lk(x) 
    termos_L = calcular_termos_Lk_simbolicos(x_dados, x)

    polinomio = 0
    for k in range(len(y_dados)):
        polinomio += y_dados[k] * termos_L[k]
    
    print("=== POLINÓMIO INTERPOLADOR P(x) (Método Lagrange)===")
    
    # escreve o polinómio na forma ax^7 + bx^6 + ...
    polinomio_final = sp.expand(polinomio)
    
    print("\nExpressão final aproximada do polinómio interpolador:")
    

    sp.pprint(sp.N(polinomio_final, 4))
    
    return polinomio_final

def resolver_spline_natural(x_lista, y_lista):
    """
    Calcula os coeficientes (a, b, c, d) para cada intervalo do Spline.
    """
    n = len(x_lista) - 1  # Temos n intervalos
    h = np.diff(x_lista)  # Calcula todos os h_i (distâncias x_i+1 - x_i)
    
    # --- 1. Montar a Matriz A e o vetor B para achar os Momentos (M) ---
    # Sistema A * M = B
    A = np.zeros((n + 1, n + 1))
    B = np.zeros(n + 1)
    
    # Condições de Fronteira Natural: M_0 = 0 e M_n = 0
    # Na matriz, isso é: 1*M_0 = 0  e  1*M_n = 0
    A[0, 0] = 1.0
    A[n, n] = 1.0
    B[0] = 0.0
    B[n] = 0.0
    
    
    
    for i in range(1, n):
        # Coeficiente de M_{i-1} (h_i-1 / 6)
    
        
        # Termo M_{i-1}
        A[i, i-1] = h[i-1] / 6
        
        # Termo M_i (Diagonal) -> (h_{i-1} + h_i) / 3
        A[i, i] = (h[i-1] + h[i]) / 3
        
        # Termo M_{i+1}
        A[i, i+1] = h[i] / 6
        
        # Lado Direito (Diferenças Divididas)
        # (f_{i+1} - f_i)/h_{i+1}  -  (f_i - f_{i-1})/h_i
        # Nota: No python y_lista corresponde a f
        termo_dir = (y_lista[i+1] - y_lista[i]) / h[i]
        termo_esq = (y_lista[i] - y_lista[i-1]) / h[i-1]
        B[i] = termo_dir - termo_esq
        
    #  Resolver o Sistema Linear 
    # Isto dá-nos os valores de M (segundas derivadas)
    M = np.linalg.solve(A, B)
    
    #  Calcular coeficientes a, b, c, d para o polinómio 
    # S_i(x) = a + b(x-xi) + c(x-xi)^2 + d(x-xi)^3
    coeficientes = []
    
    print("\n=== Coeficientes do Spline Cúbico Natural ===")
    print(f"{'Intervalo':<10} | {'a':<10} | {'b':<10} | {'c':<10} | {'d':<10}")
    
    for i in range(n):
        # a_i é simplesmente f(x_i)
        a = y_lista[i]
        
        # c_i = M_i / 2 
        c = M[i] / 2
        
        # d_i = (M_{i+1} - M_i) / (6 * h_i)  
        d = (M[i+1] - M[i]) / (6 * h[i])
        
        # b_i é isolado na equação do S_i(x)
        b = (y_lista[i+1] - y_lista[i]) / h[i] - (2*h[i]*M[i] + h[i]*M[i+1]) / 6
        
        coeficientes.append((a, b, c, d))
        print(f"[{i}, {i+1}]      | {a:.4f}     | {b:.4f}     | {c:.4f}     | {d:.4f}")

    return coeficientes

def mostrar_equacoes_spline(coefs, x_lista):
    x = sp.symbols('x')
    print("\n=== Equações dos Polinómios por Intervalo ===")
    
    for i in range(len(coefs)):
        a, b, c, d = coefs[i]
        xi = x_lista[i]
        
        # Montar a equação: a + b(x-xi) + c(x-xi)^2 + d(x-xi)^3
        eq = a + b*(x - xi) + c*(x - xi)**2 + d*(x - xi)**3
        
        # Expandir
        eq_final = sp.expand(eq)
        
        print(f"Intervalo [{x_lista[i]:.2f}, {x_lista[i+1]:.2f}]:")
        # sp.pprint(sp.N(eq_final, 4))
        # Imprime de forma linear para poupar espaço
        print(f"S{i}(x) = {eq_final}")
        print("-" * 20)


x_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_2 = [8.6, 7.0, 6.4, 4.0, 2.8, 1.8, 1.8, 2.1, 3.2, 4.7, 6.2, 7.6]



def calcular_coeficientes_diferencas_divididas (x , y ) :
    n = len ( x )
    tabela = np . zeros (( n , n ) )
    tabela [: , 0] = y
    for j in range (1 , n ) :
        for i in range ( n - j ) :
            # Fórmula : ( f [ i +1] - f [ i ]) / ( x [ i + j ] - x [ i ])
            numerador = tabela [ i +1][ j -1] - tabela [ i ][ j -1]
            denominador = x [ i + j ] - x [ i ]
            tabela [ i ][ j ] = numerador / denominador
    return tabela [0 , :]


def resolver_newton_simbolico () :
    print ("=== POLINÓMIO INTERPOLADOR P(x) (Método Newton)===")
    x = sp . symbols ('x')
    coefs = calcular_coeficientes_diferencas_divididas ( x_2 , y_2 )
    polinomio = 0
    n = len ( x_2 )
    for k in range ( n ) :
        termo_atual = coefs [ k ]
        for i in range ( k ) :
            termo_atual = termo_atual * ( x - x_2 [ i ])
        polinomio += termo_atual
    polinomio_final = sp . expand ( polinomio )
    sp . pprint ( sp . N ( polinomio_final , 4) )

    return polinomio_final

print ("=== Exercício 1 ===")
print("=== Alínea a ===")
print("Pontos gerados (xi, yi):")
for i in range(len(x_dados)):
    print(f"  Ponto {i}: x = {x_dados[i]:.4f}, y = {y_dados[i]:.4f}")
print("\n" + "="*40 + "\n")

print("=== Alínea b ===")
resolver_lagrange_completo()
print("\n" + "="*20 + "\n")

coef1 = resolver_spline_natural (x_dados, y_dados)
mostrar_equacoes_spline (coef1, x_dados)

print("\n" + "="*40 + "\n")


print ("=== Exercício 2 ===")
print("=== Alínea a ===")

resolver_newton_simbolico()
print("\n" + "="*20 + "\n")

coef2 = resolver_spline_natural (x_2, y_2)
mostrar_equacoes_spline (coef2, x_2)


