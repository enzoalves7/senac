# Desenvolva um gerador de tabuada 
# capaz de gerar qualquer 
# numero inteiro entre 0 a 10. 
# O usuario deve informar qual numero que 
#ele deseja ver na tabuada

numero = int(input("Digite um número entre 0 a 10: "))

if numero < 0 or numero > 10:
    print("Número inválido. Por favor, digite um número entre 0 e 10.")
else:
    print(f"Tabuada de {numero}")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
