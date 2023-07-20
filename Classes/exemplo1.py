class bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self, nova_cor):
        self.cor = nova_cor

    def mostrar_cor(self):
        return self.cor
bola1 = bola("azul", "70", "couro")
print(f"A cor da bola é {bola1.mostrar_cor()}")

bola1.trocar_cor("vermelha")
print(f"A nova cor é {bola1.cor}")
