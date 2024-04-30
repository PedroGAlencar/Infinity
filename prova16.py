class Material:
    def __init__(self,titulo,autor_ou_editora):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora

    def exibir_informacoes(self):
        return f'''
Título: {self.titulo}
Autor/Editora: {self.autor_ou_editora}
'''
    
class Livro(Material):
    def __init__(self,titulo,autor_ou_editora,genero):
        super().__init__(titulo,autor_ou_editora)
        self.genero = genero

    def exibir_informacoes(self):
        return f'''
{super().exibir_informacoes()}
Gênero: {self.genero}
'''
    
class Revista(Material):
    def __init__(self,titulo,autor_ou_editora,edicao):
        super().__init__(titulo,autor_ou_editora)
        self.edicao = edicao

    def exibir_informacoes(self):
        return f'''
{super().exibir_informacoes()}
Edição: {self.edicao}
'''
    

livro = Livro('O monstro atrás de você','Rei Stephen','Terror')
revista = Revista('Beleza para todos?','Editora Belo','200')

print(livro.exibir_informacoes())

print(revista.exibir_informacoes())