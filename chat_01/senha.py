import re

class SenhaInvalidaException(Exception):
    def __init__(self, mensagem="Senha inválida."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
        self.email = str
    
    def validar_senha(self):
        if len(self.senha) < 8:
            raise SenhaInvalidaException("A senha deve conter pelo menos 8 caracteres.")
        
        if not re.search(r"[A-Z]", self.senha):
            raise SenhaInvalidaException("A senha deve conter pelo menos uma letra maiúscula.")
        
        if not re.search(r"\d", self.senha):
            raise SenhaInvalidaException("A senha deve conter pelo menos um número.")

# Criar usuário
login = input("Digite o login: ")
senha = input("Digite a senha: ")

while True:
    try:
        usuario = Usuario(login, senha)
        usuario.validar_senha()
        print("Usuário criado com sucesso!")
        break
    except SenhaInvalidaException as e:
        print(e.mensagem)
        senha = input("Digite uma senha válida: ")

# Login do usuário
login_digitado = input("Digite seu login: ")
senha_digitada = input("Digite sua senha: ")

if login_digitado == usuario.login and senha_digitada == usuario.senha:
    print("Login realizado com sucesso!")
else:
    print("Login ou senha incorretos.")
