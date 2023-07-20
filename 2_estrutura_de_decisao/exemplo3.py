nota1 = float(input("Digite sua 1° nota: "))
nota2 = float(input("Digite sua 2° nota: "))
media = (nota1 + nota2) /2
situação = ""
if media >= 9.0 and media <= 10.0:
    situação = "A"
elif media >= 7.5 and media <= 9.0:
    situação = "B"
elif media >= 6.0 and media <= 7.5:
    situação = "C"
elif media >= 4.0 and media <= 6.0:
    situação = "D"
else:
    media >= 0.0 and media <= 4.0
    situação = "E"
print(f"Suas notas: {nota1}, {nota2}")
print(f"Sua media foi: {media}")
print(f"Situação: {situação}")

if situação in ["A", "B", "C"]:
    situação = "Aprovado!!!"
else:
    situação = ["D", "E"]
    situação = "Reprovado"