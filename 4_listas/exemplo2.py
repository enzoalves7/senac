# Fça um algoritmo que leia 20 numeros inteiros 
# e armazene-os numa lista. Armazene os numeros 
# pares na lista par e os numeros impares na
# lista impar. imprima as tres listas.


numeros = []
par = []
impar = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}° número: "))
    numeros.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print("Números digitados:", numeros)
print("Números pares:", par)
print("Números ímpares:", impar)




