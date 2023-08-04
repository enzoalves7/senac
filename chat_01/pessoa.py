# Classe Pessoa

class Pessoa:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def mostrar_informacoes(self):
        print("Escolha o que deseja ver:")
        print("1 - Nome")
        print("2 - CPF")
        print("3 - Salário")
        print("4 - Sair")

        opcao = int(input("Digite a opção desejada: "))

        while opcao != 4:
            if opcao == 1:
                print("Nome:", self.nome)
            elif opcao == 2:
                print("CPF:", self.cpf)
            elif opcao == 3:
                print("Salário:", self.salario)
            else:
                print("Opção inválida!")

            opcao = int(input("Digite a opção desejada: "))


# Obtendo informações do usuário
nome_informado = input("Digite o nome da pessoa: ")
cpf_informado = input("Digite o CPF da pessoa: ")
salario_informado = float(input("Digite o salário da pessoa: "))

# Criando um objeto da classe Pessoa com as informações do usuário
pessoa1 = Pessoa(nome_informado, cpf_informado, salario_informado)

# Mostrando as informações conforme a escolha da pessoa
pessoa1.mostrar_informacoes()
