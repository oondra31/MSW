from math import *
import time
from scipy import optimize

#funkce
list_fce = [lambda x: x**3-x**2+x/2-6, lambda x: e**(x**2+x/4)-9, lambda x: sin(2*x)]

#výpočet kořenů funkcí
def fce_bisect(min,max,max_iters,fce):
  for step in range(max_iters):  
    middle=(min+max)/2  
    if (fce(min)*fce(middle))<0:
      max=middle
    else:
      min=middle
  return middle

time_before=time.time()

min=0     
max=5
poc_kroku=100

for i,fce in enumerate(list_fce):
    koren=fce_bisect(min,max,poc_kroku,fce)
    print(f"kořen funkce f{i}= {koren}")
print(f"Čas pomocí metody Bisekce: {time.time() - time_before} s\n")

#Newtonova metoda
time_before=time.time()

min=0
max=5

for i,fce in enumerate(list_fce):
    koren = optimize.newton(fce, x0=(min+max/2))
    print(f"kořen funkce f{i}= {koren}")

print(f"Čas pomocí Newtonovy metody: {time.time() - time_before} s\n")
print(f"metody mají dostatečně vysokou přesnost a metoda bisekce byla rychlejší pro 100 kroků")


