class Livro:   
   
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    
        self.titulo = titulo
        self.autor = autor
       
    def imprimir_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_publicacao}")

livro1 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
livro1.imprimir_informacoes()
print(livro1.get_titulo())
print(livro1.get_autor())
print(livro1.get_ano_publicacao())