class Memoria:
    def __init__(self):
        self.marca = ""
        self.capacidade = ""

    def __str__(self):
        return f"{self.marca}\n{self.capacidade}"

class Processador:
    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self.velocidade = velocidade

    def __str__(self):
        return f"{self.modelo}\n{self.velocidade}"
 
class Armazenamento:
     def __init__(self, tipo, capacidade):
        self.tipo = tipo
        self.capacidade = capacidade

class Computador:
    def __init__(self):
        self.memoria = Memoria()
        self.processador = Processador("", "")
        self.armazenamento = Armazenamento("", "")
        
    def __str__(self):
        return f"Memória: {self.memoria}\nProcessador: {self.processador}\nArmazenamento: {self.armazenamento}"
