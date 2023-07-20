peso_de_peixe = float(input("Digite o peso do seu peixe: "))
limite_de_peso = 50.0
peso_extra = 0.0
multa = 0.0

if peso_de_peixe > limite_de_peso:
    peso_extra = limite_de_peso - peso_de_peixe
    multa = peso_extra * 4.0
    print(f"Peso excedido: {peso_extra} kg")
    print(f"Multa a ser paga: R$ {multa}")
else:
    print("Não houve excesso de peso. Nenhuma multa é devida.")




