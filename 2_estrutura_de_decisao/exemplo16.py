a = float(input("Digite A: "))
import math
if a == 0:
    print("o valor de A nao pode ser 0")
else:
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

delta = b**2-4*a*c
if delta < 0:
    print("Não possui raízes")
elif delta == 0:
    raiz = -b/(2*a)
    print(f"Possui uma raiz {raiz:.2f}")
else:
    raiz1 = (-b + math.sqrt(delta))/2*a
    raiz2 = (-b - math.sqrt(delta))/2*a
    print(f"Possui 2 raizes - Raiz 1: {raiz1} e Raiz 2: {raiz2}")