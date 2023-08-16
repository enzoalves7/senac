class EstoqueNegativoError(Exception):
    def __init__(self, mensagem="Quantidade em estoque não pode ser negativa."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

class EstoqueInsuficienteError(Exception):
    def __init__(self, quantidade, estoque, mensagem="Quantidade em estoque insuficiente."):
        self.quantidade = quantidade
        self.estoque = estoque
        self.mensagem = f"{mensagem} Quantidade desejada: {quantidade}, Estoque disponível: {estoque}"
        super().__init__(self.mensagem)

class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def aumentar(self, quantidade):
        if quantidade < 0:
            raise EstoqueNegativoError("Quantidade a aumentar não pode ser negativa.")
        self.quantidade_estoque += quantidade

    def diminuir(self, quantidade):
        if quantidade < 0:
            raise EstoqueNegativoError("Quantidade a diminuir não pode ser negativa.")
        if quantidade > self.quantidade_estoque:
            raise EstoqueInsuficienteError(quantidade, self.quantidade_estoque)
        self.quantidade_estoque -= quantidade
# Criar produtos
produto1 = Produto("Camiseta", 25.0, 10)
produto2 = Produto("Calça", 50.0, 5)

carrinho = []

# Menu da loja
while True:
    print("\n*** Loja ***")
    print("1. Ver produtos")
    print("2. Adicionar produto")
    print("3. Adicionar ao carrinho")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("\nProdutos disponíveis:")
        print(f"{produto1.nome}: R${produto1.preco} (Estoque: {produto1.quantidade_estoque})")
        print(f"{produto2.nome}: R${produto2.preco} (Estoque: {produto2.quantidade_estoque})")
    elif escolha == "2":
        nome_produto = input("Digite o nome do produto: ")
        preco_produto = float(input("Digite o preço do produto: "))
        estoque_produto = int(input("Digite a quantidade em estoque: "))
        novo_produto = Produto(nome_produto, preco_produto, estoque_produto)
        print("Produto adicionado com sucesso.")
    elif escolha == "3":
        print("\nProdutos disponíveis:")
        print("1. Camiseta")
        print("2. Calça")
        opcao_produto = input("Escolha um produto para adicionar ao carrinho: ")

        if opcao_produto == "1":
            produto = produto1
        elif opcao_produto == "2":
            produto = produto2
        else:
            print("Opção inválida.")
            continue

        quantidade = int(input(f"Quantidade de {produto.nome} a adicionar: "))
        try:
            produto.diminuir(quantidade)
            carrinho.append((produto, quantidade))
            print(f"{quantidade} {produto.nome}(s) adicionado(s) ao carrinho.")
        except EstoqueNegativoError as ene:
            print(ene.mensagem)
        except EstoqueInsuficienteError as eie:
            print(eie.mensagem)
    elif escolha == "4":
        print("Saindo da loja.")
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")

# Exibir itens no carrinho
if carrinho:
    print("\nItens no carrinho:")
    total_carrinho = 0
    for item, quantidade in carrinho:
        subtotal = item.preco * quantidade
        print(f"{quantidade} {item.nome}(s) - Subtotal: R${subtotal:.2f}")
        total_carrinho += subtotal
    print(f"Total do carrinho: R${total_carrinho:.2f}")
else:
    print("\nCarrinho vazio.")