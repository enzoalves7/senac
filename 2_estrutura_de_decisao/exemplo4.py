lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))
area = (lado1+lado2*lado3)/2
if lado1 == lado2 == lado3:
    print("O triangulo é equilatero possui os tres lados iguais!")
elif lado1 != lado2 == lado3 or lado1 == lado2 != lado3:
    print("O triangulo é isosceles possui os dois lados iguais!")
elif lado1 != lado2 != lado3:
    print("O tringulo é escaleno possui os tres lados diferentes!")
print(f"A area do triangulo é {area}")