# construa um codigo que receba tres numeros 
# calcule a media aritmetrica entre eles
# e imprima o resultado

numero1 = float(input("Nota 1: "))
numero2 = float(input("Nota 2: "))
numero3 = float(input("Nota 3: "))
media = (numero1 + numero2 + numero3)/3

print(f"A media entre os numeros {numero1}, {numero2}, {numero3} é igual à {media}")


# verificar se a media é igual ou maior que 70
aprovado = media >= 70
reprovado = media < 30

if aprovado:
    print(f"Voce foi aprovado com a media {media}")
elif reprovado:
    print(f"Voce foi reprovado com a media {media}")
else: 
    print(f"Voce esta em recuperaçao com a media {media}")