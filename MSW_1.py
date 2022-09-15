import numpy as np
import time
import random
from scipy.misc import derivative

def gen(pocet_cisel):
    V1 = []    
    for i in range(pocet_cisel):
        V1.append(random.randrange(-100,100))    
    return (V1)

def scalar(V1,V2): 
    start_time = time.time()
    V3 = 0
    for i in range(len(V1)): 
        V3 = V3 + V1[i] * V2[i]
    end_time = time.time()
    doba =end_time - start_time
    #print(V3)  
    print(f"Čas potřebný k výpočtu scalarního součinu bez numpy byl: {doba}s")
    
def scalar_nmp(V1,V2):    
    V1 = np.array(V1)
    V2 = np.array(V2)
    start_time = time.time()    
    Vector3 = np.dot(V1,V2)      
    end_time = time.time()
    doba = end_time - start_time
    #print(Vector3)
    print(f"Čas potřebný k výpočtu scalarního součinu s numpy byl: {doba}s")

def integral(bod1,bod2,step):
    start_time = time.time()
    rngup = int(1/step)
    x1 = [x * step for x in range(rngup*bod1,rngup*bod2+1)]    
    int1 = 0
    for i in x1:    
        int1 = int1 + (3*i+2)*step
    end_time = time.time()
    doba = end_time - start_time
    #print(int1)
    print(f"Čas potřebný k výpočtu integralu bez numpy byl: {doba}s")

def integral_nmp(bod1,bod2,step):
    start_time = time.time()
    nmpy_array = np.arange(bod1,bod2,step)
    x = np.append(nmpy_array,bod2)
    y = 3*x+2
    numpy_trapz = np.trapz(y,x)
    end_time = time.time()
    doba = end_time - start_time
    #print(numpy_trapz)
    print(f"Čas potřebný k výpočtu integralu s numpy byl: {doba}s")
    
def determinant(matice):
    start_time = time.time()
    det = 0
    mat_len = len(matice)
    # přidání řůdků
    for i in range(len(matice)-1):
        matice.append(matice[i])
    # \/
    rr = list(reversed(range(mat_len)))
    for posun in range(mat_len):
        mezi_plus = 1
        mezi_minus = 1
        for xy in range(mat_len):
            mezi_plus *= matice[xy+posun][xy]
            mezi_minus *= matice[xy+posun][rr[xy]]
        det += mezi_plus
        det -= mezi_minus
    end_time = time.time()
    doba = end_time - start_time   
    print(f"Čas potřebný k výpočtu determinantu bez numpy byl: {doba}s")

def determinant_nmp(matice):
    start_time = time.time()
    det = np.linalg.det(matice)
    end_time = time.time()
    doba = end_time - start_time   
    print(f"Čas potřebný k výpočtu determinantu s numpy byl: {doba}s")
    
def matrix_multiply(A, B):  
    start_time = time.time()
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
   
    C = []
    while len(C) < rowsA:
        C.append([])
        while len(C[-1]) < colsB:
            C[-1].append(0.0)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total
    end_time = time.time()
    doba = end_time - start_time
    #print(C)
    print(f"Čas potřebný k výpočtu násobení matic bez numpy byl: {doba}s")
    
def matrix_multiply_nmp(matrixA,matrixB):
    start_time = time.time()
    A = np.dot(matrixA,matrixB)
    end_time = time.time()
    doba = end_time - start_time
    #print(A)
    print(f"Čas potřebný k výpočtu násobení matic s numpy byl: {doba}s")

def derivace(bodX,dx,fnc):
    start_time = time.time()
    f = lambda x: eval(fnc) 
    dy = f(bodX+dx) - f(bodX)
    vysledek = dy/dx
    end_time = time.time()
    doba = end_time-start_time
    #print(vysledek)
    print(f"Čas potřebný k výpočtu derivace bez scipy byl: {doba}s")
     
def derivace_scipy(bodX,dx,fnc):
    start_time = time.time()
    f = lambda x: eval(fnc)
    vysledek = derivative(f, bodX, dx)
    end_time = time.time()
    doba = end_time - start_time
    #print(vysledek)
    print(f"Čas potřebný k výpočtu derivace s scipy byl: {doba}s")
     
# Scalar
pocet_cisel = 10000
V1 = gen(pocet_cisel)
V2 = gen(pocet_cisel)
scalar(V1,V2)
scalar_nmp(V1,V2)

# Integral
bod1 = 0
bod2 = 10
step = 0.000001
integral(bod1, bod2, step)
integral_nmp(bod1,bod2,step)

# Determinant
matrix1 = [[6, 2, 1, 4],[4, -2, 5, 1],[2, 6, -1, 7],[3, 5, 7, 2]]
nmp_matrix1 = np.array(matrix1)
determinant(matrix1)
determinant_nmp(nmp_matrix1)

# Matrix multiply
matrix2 = [[1,4],[5,3]]
matrix3 = [[4,1],[1,9]]
nmp_matrix2 = np.array(matrix2)
nmp_matrix3 = np.array(matrix3)
matrix_multiply(matrix2,matrix3)
matrix_multiply_nmp(nmp_matrix2,nmp_matrix3)

# Derivace
bodX = 5
dx = 0.00000001
fnc = "3**x+x*2"
derivace(bodX,dx,fnc)
derivace_scipy(bodX, dx, fnc)




