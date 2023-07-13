# faca um algoritmo que leia 
# tres numeros e mostre o maior deles

# Professor...

# Ler três números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Verificar o maior número
maior = numero1

if numero2 > maior:
    maior = numero2

if numero3 > maior:
    maior = numero3

# Mostrar o maior número
print("O maior número é:", maior)
