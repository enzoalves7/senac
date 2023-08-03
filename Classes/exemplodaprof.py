class Pessoa: 

    def __init__(self, nome):
        self.nome = nome
        self.idade = int

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}"

if __name__ : "__main__"

pessoa = Pessoa ("Enxo")
pessoa.idade = 1
print(pessoa)
