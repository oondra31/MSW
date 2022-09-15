import numpy as np
import time
import matplotlib.pyplot as plt

#Jacobiho metoda 
def jacobiho_metoda(diag_once,right_matrix, niteraci, x):
    diagonale = np.diag(diag_once)
    triangle_lower = np.tril(diag_once, k = -1)
    triangle_upper = np.triu(diag_once, k = 1)
    for i in range(niteraci):
        x = (right_matrix - np.matmul((triangle_lower + triangle_upper),x))/diagonale
        if (np.allclose(x, vysledek_gaussovy_metody, rtol=1e-8, atol=1e-9,)) == True: 
            break
    return x

#Gaussova metoda 
def gaussova_metoda(diag_once,right_matrix):
    x = np.linalg.solve(diag_once, right_matrix)
    return x

casyG2 = [ ]
casyJ2 = [ ]

#tvorba rady rovnic
size = input ("Zadejte velikost ctvercove matice = " ) 
print("Zvolena velikost ctvercove matice je :", size)
size = int(size)

for step in range (size-1):
    step = step + 2
    matrix = np.ones(step) 
    np.array
    
    #diagonalni matice
    diag = np.diagflat([matrix])
    np.diag
    
    #jednotkova matice
    once = np.ones((step, step), dtype=int)
    np.array
   
    #jednotkova + diagonalni matice
    diag_once = diag + once
    
    #tvorba matice prava strana
    right_once = np.ones(step)
    np.array
    right_matrix = right_once*(step+1)    

    for v in range (100):
        x = np.ones(len(diag_once))
        
        #vypocty + cas pro Gaussovu metodu
        casyG1 = [ ]
        gstart = time.perf_counter()
        vysledek_gaussovy_metody = gaussova_metoda(diag_once,right_matrix)
        gend = time.perf_counter()
        g = gend - gstart
        g = round(1000000*g)
        
        #vypocty + cas pro Jacobiho metodu
        casyJ1 = [ ]
        jstart = time.perf_counter()
        vysledek_jacobiho_metody = jacobiho_metoda(diag_once,right_matrix,100,x)
        jend = time.perf_counter()
        j = jend - jstart
        j = round(1000000*j)
    
        casyG1.append(g)
        casyJ1.append(j)

    PG = np.mean(casyG1)
    PJ = np.mean(casyJ1)    

    casyG2.append(PG)   
    casyJ2.append(PJ)   

#vysledny graf
fig, ax = plt.subplots ()
line = plt.plot(casyG2, label = "Gaussova eliminace")
line = plt.plot(casyJ2, label = "Jacobiho iteracni metoda")
plt.title(r"Potrebny cas k vypoctu dane linearni soustavy rovnic")
plt.xlabel('Velikost ctvercove matice')
plt.ylabel('Doba vypoctu [10^-6 s]')

ax.legend(loc=2)

plt.show() 