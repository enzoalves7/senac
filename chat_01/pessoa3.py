# Gerente

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def mostrar_informacoes(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)


class Gerente(Pessoa):
    def __init__(self, nome, cpf, setor):
        super().__init__(nome, cpf)
        self.setor = setor
        self.quantidade_equipe = 0
        self.salario = 0

    def informacoes_Gerente(self):
        super().mostrar_informacoes()
        print("Setor:", self.setor)
        print("Quantidade de Equipe:", self.quantidade_equipe)
        print("Salário:", self.salario)

    def calculo_bonificacao(self):
        if self.quantidade_equipe >= 10:
            bonificacao = self.salario * 0.10
        else:
            bonificacao = self.salario * 0.05

        self.salario += bonificacao


# Obtendo informações do gerente
nome_informado = input("Digite o nome do gerente: ")
cpf_informado = input("Digite o CPF do gerente: ")
setor_informado = input("Digite o setor do gerente: ")
salario_informado = float(input("Digite o salário do gerente: "))
quantidade_equipe_informada = int(input("Digite a quantidade de equipe sob sua supervisão: "))

gerente1 = Gerente(nome_informado, cpf_informado, setor_informado)
gerente1.salario = salario_informado
gerente1.quantidade_equipe = quantidade_equipe_informada

# Exibindo informações do gerente
gerente1.informacoes_Gerente()

# Realizando cálculo da bonificação e atualizando o salário do gerente
gerente1.calculo_bonificacao()

# Exibindo novamente as informações atualizadas do gerente
print("\nApós o cálculo da bonificação:")
gerente1.informacoes_Gerente()
