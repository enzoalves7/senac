# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input("Digite o valor de n: "))

# Verifica se o valor de n é válido
if n <= 0:
    print("O valor de n deve ser maior que zero.")
else:
    # Inicializa os primeiros dois termos da série
    termo1 = 1
    termo2 = 1

    # Imprime os primeiros n termos da série de Fibonacci
    print(termo1)
    print(termo2)

    for i in range(3, n+1):
        termo_atual = termo1 + termo2
        print(termo_atual)
        
        # Atualiza os termos anteriores
        termo1 = termo2
        termo2 = termo_atual


