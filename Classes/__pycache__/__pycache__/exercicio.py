import math

class Forma:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def area(self):
        return 0

class Retangulo(Forma):
    def __init__(self, nome, cor, base, altura):
        super().__init__(nome, cor)
        self.base = base
        self.altura = altura

    def areaRetangulo(self):
        return self.base * self.altura

class Circulo(Forma):
    def __init__(self, nome, cor, raio):
        super().__init__(nome, cor)
        self.raio = raio

    def areaCirculo(self):
        return math.pi * self.raio ** 2

print("Criação de Retângulo")
nome_retangulo = input("Digite o nome do Retângulo: ")
cor_retangulo = input("Digite a cor do Retângulo: ")
base_retangulo = float(input("Digite a base do Retângulo: "))
altura_retangulo = float(input("Digite a altura do Retângulo: "))

meu_retangulo = Retangulo(nome_retangulo, cor_retangulo, base_retangulo, altura_retangulo)
print("\nInformações do Retângulo:")
print(f"Nome: {meu_retangulo.nome}\nCor: {meu_retangulo.cor}")
print(f"Base: {meu_retangulo.base}\nAltura: {meu_retangulo.altura}")
print(f"Área do Retângulo: {meu_retangulo.areaRetangulo()}")

print("\nCriação de Círculo")
nome_circulo = input("Digite o nome do Círculo: ")
cor_circulo = input("Digite a cor do Círculo: ")
raio_circulo = float(input("Digite o raio do Círculo: "))

meu_circulo = Circulo(nome_circulo, cor_circulo, raio_circulo)
print("\nInformações do Círculo:")
print(f"Nome: {meu_circulo.nome}\nCor: {meu_circulo.cor}")
print(f"Raio: {meu_circulo.raio}")
print(f"Área do Círculo: {meu_circulo.areaCirculo():.2f}")
