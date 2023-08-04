class Pessoa:

    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def mostrarInformacoes(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}\nSalário: {self.salario}")

class Funcionario(Pessoa):

    def __init__(self, nome, cpf, cargo):
        super().__init__(nome, cpf)
        self.cargo = cargo

    def informacoesFuncionario(self):
        super().mostrarInformacoes()
        print(f"Cargo: {self.cargo}")

    def calcularHoraExtra(self, hora):
        self.salario += hora * 15
        return self.salario
    
class Gerente(Pessoa):

    def __init__(self, nome, cpf, setor):
        super().__init__(nome, cpf)
        self.qtde_equi = int
        self.setor = setor

    def informacaoGerente(self):
        super().mostrarInformacoes()
        print(f"Setor: {self.setor}\nQuantidade Equipe: {self.qtde_equi}")

    def calculoBonificacao(self):
        if self.qtde_equi > 10:
            return self.salario + (self.salario * 0.1)
        else:
            return self.salario + (self.salario * 0.05)
        
f = Funcionario("Aparecida", "704312844-74", "Instrutor")
f.salario = 200
print(f"Horas: {f.calcularHoraExtra(10)}")
# f.mostrarInformacoes()
f.informacoesFuncionario()

g = Gerente("Maria", "11111111-11", "TI")
g.salario = 500
g.qtde_equi = 11
print(f"Bonificação: {g.calculoBonificacao()}")
g.mostrarInformacoes()
