# faça um algoritmo que leia 5 números e
# informe o maior numero

numero1 = float(input("Número 1: "))
numero2 = float(input("Número 2: "))
numero3 = float(input("Número 3: "))
numero4 = float(input("Número 4: "))
numero5 = float(input("Número 5: "))

numero_maior = max({numero1, numero2, numero3, numero4, numero5})
print(f"O maior numero é: {numero_maior}")