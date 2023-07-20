# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e 
# continue pedindo até que o usuário informe um valor válido.

nota1 = float(input("Digite sua 1° nota: "))
nota2 = float(input("Digite sua 2° nota: "))
nota3 = int(input("Digite sua 3° nota: "))
media = (nota1 + nota2 + nota3)/3
if media >= 70:
    print("Congratulations, you were approved!"),
else:
    media <= 70,
    print("Sorry you were disapproved")
print(f"A sua media {media}")

