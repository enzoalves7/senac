class Pessoa: 
    def __init__(self, nome, cpf, salario, cargo):
        self.nome = nome 
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo

    def mostrar_informacoes(self):
        print("Digite o que vc que ver:")
        print("1. Nome")
        print("2. CPF")
        print("3. Salário")
        print("4. Cargo")
        print("5. Para Sair!")
        print(int(input("Digite a opção desejada: ")))

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, cargo):
        super().__init__(nome, cpf)
        self.cargo = cargo
        self.salario = int

    def informacoes_Funcionario(self):
        super().mostrar_informacoes()
        print("Cargo:", self.cargo)
        print("Salário:", self.salario)

    def calculo_horaExtra(self, horas):
        valor_hora_extra = 15.00
        self.salario += valor_hora_extra * horas

        while opcao != 5:
            if opcao == 1:
                print("Nome:", self.nome)
            elif opcao == 2:
                print("CPF:", self.cpf)
            elif opcao == 3:
                print("Salário:", self.salario)
            elif opcao == 4:
                print(f"Cargo: {self.cargo}")
            else:
                print("Opção inválida!")

            opcao = int(input("Digite a opção desejada: "))

nome_informado = input("Digite o nome da pessoa: ")
cpf_informado = input("Digite o CPF da pessoa: ")
salario_informado = float(input("Digite o salário da pessoa: "))
cargo_informado = input("Digite o cargo do funcionário")

pessoa1 = Pessoa(nome_informado, cpf_informado, salario_informado, cargo_informado)
pessoa1.mostrar_informacoes() 
pessoa1.salario = salario_informado

horas_extra = float(input("Digite a quantidade de horas extras trabalhadas: "))
pessoa1.calculo_horaExtra(horas_extra)

print("\nApós o cálculo de hora extra:")
pessoa1.informacoes_Funcionario()
