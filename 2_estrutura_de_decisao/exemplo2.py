# faca um algoritmo que leia 
# tres numeros e mostre o maior deles

num1 = float(input("Digite seu numero: "))
num2 = float(input("Digite seu numero: "))
num3 = float(input("Digite seu numero: "))

numero_maior = max({num1, num2, num3})
print(f"O maior numero é: {numero_maior}")