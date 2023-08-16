class EstoqueNegativoError(Exception):
    def __init__(self, message="Quantidade em estoque não pode ser negativa"):
        self.message = message
        super().__init__(self.message)

class EstoqueInsuficienteError(Exception):
    def __init__(self, estoque_atual, quantidade_desejada):
        self.message = f"Estoque insuficiente. Estoque atual: {estoque_atual}, Quantidade desejada: {quantidade_desejada}"
        super().__init__(self.message)

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def aumentar(self, quantidade):
        if quantidade < 0:
            raise EstoqueNegativoError("Quantidade para aumentar não pode ser negativa")
        self.quantidade += quantidade

    def diminuir(self, quantidade):
        if quantidade < 0:
            raise EstoqueNegativoError("Quantidade para diminuir não pode ser negativa")
        if quantidade > self.quantidade:
            raise EstoqueInsuficienteError(self.quantidade, quantidade)
        self.quantidade -= quantidade

# Solicitar informações do usuário
nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))
quantidade_inicial = int(input("Digite a quantidade inicial em estoque: "))

# Criar o objeto Produto
produto = Produto(nome_produto, preco_produto, quantidade_inicial)

try:
    # Testar o método aumentar
    quantidade_aumentar = int(input("Digite a quantidade para aumentar o estoque: "))
    produto.aumentar(quantidade_aumentar)

    # Testar o método diminuir
    quantidade_diminuir = int(input("Digite a quantidade para diminuir o estoque: "))
    produto.diminuir(quantidade_diminuir)

except (EstoqueNegativoError, EstoqueInsuficienteError) as e:
    print("Erro:", e)

# Imprimir informações finais do produto
print(f"Produto: {produto.nome}")
print(f"Preço: R${produto.preco:.2f}")
print(f"Quantidade em estoque: {produto.quantidade}")
