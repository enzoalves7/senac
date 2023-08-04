# Funcionario

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def mostrar_informacoes(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, cargo):
        super().__init__(nome, cpf)
        self.cargo = cargo
        self.salario = 0

    def informacoes_Funcionario(self):
        super().mostrar_informacoes()
        print("Cargo:", self.cargo)
        print("Salário:", self.salario)

    def calculo_horaExtra(self, horas):
        valor_hora_extra = 15.00
        self.salario += valor_hora_extra * horas

nome_informado = input("Digite o nome do funcionário: ")
cpf_informado = input("Digite o CPF do funcionário: ")
cargo_informado = input("Digite o cargo do funcionário: ")
salario_informado = float(input("Digite o salário do funcionário: "))

funcionario1 = Funcionario(nome_informado, cpf_informado, cargo_informado)
funcionario1.salario = salario_informado

funcionario1.informacoes_Funcionario()

horas_extra = float(input("Digite a quantidade de horas extras trabalhadas: "))
funcionario1.calculo_horaExtra(horas_extra)

print("\nApós o cálculo de hora extra:")
funcionario1.informacoes_Funcionario()
