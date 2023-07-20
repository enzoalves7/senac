class pessoa:
  #  nome = ""
  #  sobrenome =""
    peso = 0.0
    altura = 0.0

    def __init__(self, n, snome):
        self.nome = n
        self.sobrenome = snome

    def andar(self):
        print("Pessoa está andando")

    def falar(self):
        print("Está pessoa esta falando...")

    def calculoIMC(self, altura, peso):
        return peso / altura ** 2
    
    def alterar_peso(self, p):
        self.peso = p

    def pegar_peso(self):
        return self.peso
    
    def imprimir(self):
        print(f"Nome: {self.nome}; Sobrenome: {self.sobrenome}; Peso: {self.peso}; Altura: {self.altura}")
    
    def __str__(self):
        return f"Nome: {self.nome}; Sobrenome: {self.sobrenome}; Peso: {self.peso}; Altura: {self.altura}"

if __name__ == '__main__':
    p1 = pessoa("", "")
    p1.nome = "Maria"
    p1.sobrenome = "Silva"
    p1.peso = 50.20
    p1.altura = 180.10

    print(f"Nome: {p1.nome}; Sobrenome: {p1.sobrenome}; Peso: {p1.peso}; Altura: {p1.altura}")

    p1.alterar_peso(60.7)
    p1.falar()
    p1.andar()
    print(f"IMC: {p1.calculoIMC(p1.peso, p1.altura)}")
    p1.imprimir()
    print(p1)
