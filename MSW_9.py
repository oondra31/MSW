import numpy as np
from scipy import integrate

#funkce
def polynomial_function(x):
    return x**3 - 3*x + 7

def harmonic_function(x):
    return 2*np.sin(3*x) 

def logarithm_function(x):
    return np.log(6*x) + (2/3)

#funkce vypoctu 
def riemannuv_ctverec(funkce, lower_limit, upper_limit):
    return integrate.quadrature(funkce, lower_limit ,upper_limit)

def simpsonova_metoda(funkce, lower_limit, upper_limit, step=0.01):
    return integrate.simpson(funkce(np.arange(lower_limit, upper_limit+step, step)), np.arange(lower_limit, upper_limit+step, step))

def rombergova_metoda(funkce, lower_limit, upper_limit):
    return integrate.romberg(funkce, lower_limit, upper_limit)
 
#vysledky
print("Polynomicka funkce")
print(f"Pomoci Riemannova ctverce {riemannuv_ctverec(polynomial_function, 1, 2)[0]}")
print(f"Pomoci Simpsonovy metody {simpsonova_metoda(polynomial_function, 1, 2)}")
print(f"Pomoci Rombergovy metody {rombergova_metoda(polynomial_function, 1, 2)}")

print("\nHarmonicka funkce")
print(f"Pomoci Riemannova ctverce {riemannuv_ctverec(harmonic_function, 1, 2)[0]}")
print(f"Pomoci Simpsonovy metody {simpsonova_metoda(harmonic_function, 1, 2)}")
print(f"Pomoci Rombergovy metody {rombergova_metoda(harmonic_function, 1, 2)}")

print("\nLogaritmicka funkce")
print(f"Pomoci Riemannova ctverce {riemannuv_ctverec(logarithm_function, 1, 2)[0]}")
print(f"Pomoci Simpsonovy metody {simpsonova_metoda(logarithm_function, 1, 2)}")
print(f"Pomoci Rombergovy metody {rombergova_metoda(logarithm_function, 1, 2)}")