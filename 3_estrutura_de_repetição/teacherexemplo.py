# faça um algoritmo que leia 5 números e
# informe o maior numero

contador = 1
maior = 0
while contador <= 5:
    numero = int(input(f"Digite o {contador} numero: "))

    if contador == 1 or numero > maior:
        maior = numero
    
    contador += 1

print(f"O maior numero é {maior}")