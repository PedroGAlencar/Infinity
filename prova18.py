from tkinter import *

class Livro:
    def __init__(self, titulo, autor, ID):
        self.titulo = titulo
        self.autor = autor
        self.ID = ID
        self.emprestado = False  # Inicialmente, o livro está disponível

class Membro:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.historico = []  # Lista para armazenar os livros emprestados pelo membro

class Biblioteca:
    def __init__(self):
        self.catalogo = {}  # Dicionário para armazenar os livros por ID
        self.membros = {}   # Dicionário para armazenar os membros por número

    def adicionar_livro(self, livro):
        self.catalogo[livro.ID] = livro

    def adicionar_membro(self, membro):
        self.membros[membro.numero] = membro

    def emprestar_livro(self, livro_id, membro_numero):
        livro = self.catalogo.get(livro_id)
        membro = self.membros.get(membro_numero)
        if livro and membro and not livro.emprestado:
            livro.emprestado = True
            membro.historico.append(livro)
            print(f"O livro '{livro.titulo}' foi emprestado para {membro.nome}.")
        else:
            print("Não foi possível realizar o empréstimo.")

    def registrar_devolucao(self, livro_id, membro_numero):
        livro = self.catalogo.get(livro_id)
        membro = self.membros.get(membro_numero)
        if livro and membro and livro in membro.historico:
            livro.emprestado = False
            membro.historico.remove(livro)
            print(f"O livro '{livro.titulo}' foi devolvido por {membro.nome}.")
        else:
            print("Não foi possível registrar a devolução.")

    def pesquisar_livro(self, termo):
        resultados = []
        for livro in self.catalogo.values():
            if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower() or termo.lower() == livro.ID.lower():
                resultados.append(livro)
        return resultados

def add_livro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    livro_id = entry_id.get()
    novo_livro = Livro(titulo, autor, livro_id)
    biblioteca.adicionar_livro(novo_livro)
    print("Livro adicionado com sucesso!")

def add_membro():
    nome = entry_nome.get()
    numero = entry_numero.get()
    novo_membro = Membro(nome, numero)
    biblioteca.adicionar_membro(novo_membro)
    print("Membro adicionado com sucesso!")

def emprestar_livro():
    livro_id = entry_livro_id.get()
    membro_numero = entry_membro_numero.get()
    biblioteca.emprestar_livro(livro_id, membro_numero)

def devolver_livro():
    livro_id = entry_livro_id.get()
    membro_numero = entry_membro_numero.get()
    biblioteca.registrar_devolucao(livro_id, membro_numero)

def pesquisar_livro():
    termo = entry_termo.get()
    resultados = biblioteca.pesquisar_livro(termo)
    if resultados:
        print("\nResultados da pesquisa:")
        for livro in resultados:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, ID: {livro.ID}")
    else:
        print("Nenhum resultado encontrado.")

biblioteca = Biblioteca()

root = Tk()
root.title("Gerenciamento de Biblioteca")

frame_adicionar_livro = Frame(root)
frame_adicionar_livro.pack(pady=10)

label_titulo = Label(frame_adicionar_livro, text="Título:")
label_titulo.grid(row=0, column=0, padx=5, pady=5)
entry_titulo = Entry(frame_adicionar_livro)
entry_titulo.grid(row=0, column=1, padx=5, pady=5)

label_autor = Label(frame_adicionar_livro, text="Autor:")
label_autor.grid(row=1, column=0, padx=5, pady=5)
entry_autor = Entry(frame_adicionar_livro)
entry_autor.grid(row=1, column=1, padx=5, pady=5)

label_id = Label(frame_adicionar_livro, text="ID:")
label_id.grid(row=2, column=0, padx=5, pady=5)
entry_id = Entry(frame_adicionar_livro)
entry_id.grid(row=2, column=1, padx=5, pady=5)

button_adicionar_livro = Button(frame_adicionar_livro, text="Adicionar Livro", command=add_livro)
button_adicionar_livro.grid(row=3, columnspan=2, pady=10)

frame_adicionar_membro = Frame(root)
frame_adicionar_membro.pack(pady=10)

label_nome = Label(frame_adicionar_membro, text="Nome:")
label_nome.grid(row=0, column=0, padx=5, pady=5)
entry_nome = Entry(frame_adicionar_membro)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_numero = Label(frame_adicionar_membro, text="Número:")
label_numero.grid(row=1, column=0, padx=5, pady=5)
entry_numero = Entry(frame_adicionar_membro)
entry_numero.grid(row=1, column=1, padx=5, pady=5)

button_adicionar_membro = Button(frame_adicionar_membro, text="Adicionar Membro", command=add_membro)
button_adicionar_membro.grid(row=2, columnspan=2, pady=10)

frame_emprestar_devolver = Frame(root)
frame_emprestar_devolver.pack(pady=10)

label_livro_id = Label(frame_emprestar_devolver, text="ID do Livro:")
label_livro_id.grid(row=0, column=0, padx=5, pady=5)
entry_livro_id = Entry(frame_emprestar_devolver)
entry_livro_id.grid(row=0, column=1, padx=5, pady=5)

label_membro_numero = Label(frame_emprestar_devolver, text="Número do Membro:")
label_membro_numero.grid(row=1, column=0, padx=5, pady=5)
entry_membro_numero = Entry(frame_emprestar_devolver)
entry_membro_numero.grid(row=1, column=1, padx=5, pady=5)

button_emprestar_livro = Button(frame_emprestar_devolver, text="Emprestar Livro", command=emprestar_livro)
button_emprestar_livro.grid(row=2, column=0, padx=5, pady=5)

button_devolver_livro = Button(frame_emprestar_devolver, text="Devolver Livro", command=devolver_livro)
button_devolver_livro.grid(row=2, column=1, padx=5, pady=5)

frame_pesquisar = Frame(root)
frame_pesquisar.pack(pady=10)

label_termo = Label(frame_pesquisar, text="Termo de Pesquisa:")
label_termo.grid(row=0, column=0, padx=5, pady=5)
entry_termo = Entry(frame_pesquisar)
entry_termo.grid(row=0, column=1, padx=5, pady=5)

button_pesquisar_livro = Button(frame_pesquisar, text="Pesquisar Livro", command=pesquisar_livro)
button_pesquisar_livro.grid(row=1, columnspan=2, pady=10)

root.mainloop()

