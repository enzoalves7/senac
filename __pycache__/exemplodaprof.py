class Brinquedo:

    def __init__(self):
        self.tipo = str
        self.faixaE = str
        self.preco = float

    def ligar(self):
        print("O brinquedo está ligando!")

    def desligar(self):
        print("O brinquedo esta desligado!")

    def imprimir(self):
        print(f"Tipo: {self.tipo}\nFaixa: {self.faixaE}\nPreço: {self.preco}")
        