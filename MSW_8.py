#vypocty derivaci
def forward_derivate(f, point, step):
    return (f(point+step) - f(point))/step

def backward_derivate(f, point, step):
    return (f(point) - f(point-step))/step

def central_derivate(f, point, step):
    return (f(point+step) - f(point-step))/(2*step)

def forward_derivate_adaptive(f, point, adaptive):
    return (f(point+adaptive) - f(point))/adaptive

def backward_derivate_adaptive(f, point, adaptive):
    return (f(point) - f(point-adaptive))/adaptive

def central_derivate_adaptive(f, point, adaptive):
    return (f(point+adaptive) - f(point-adaptive))/(2*adaptive)

#funkce a volba
f = lambda x: x**2 - 3
point = 2
step = 0.2
adaptive = float(input("Zadejte adaptivni krok: "))

#mezi vysledky
for_derivate = forward_derivate(f, point, step)
back_derivate = backward_derivate(f, point, step)
centr_derivate = central_derivate(f, point, step)
for_derivate_adapt= forward_derivate_adaptive(f, point, adaptive)
back_derivate_adapt = backward_derivate_adaptive(f, point, adaptive)
centr_derivate_adapt = central_derivate_adaptive(f, point, adaptive)

#vysledky
print(f"Bez kroku pro doprednou: {for_derivate}, s krokem pro doprednou: {for_derivate_adapt}")
print(f"Bez kroku pro zpetnou: {back_derivate}, s krokem pro doprednou: {back_derivate_adapt}")
print(f"Bez kroku pro centralni: {centr_derivate}, s krokem pro doprednou: {centr_derivate_adapt}")