import tkinter as tk
from tkinter import messagebox

class Livro:
    def __init__(self, titulo, autor, exemplares):
        self.titulo = titulo
        self.autor = autor
        self.exemplares = exemplares

class Catalogo:
    def __init__(self):
        self.livros = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")

    def validar_disponibilidade(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.exemplares > 0:
                    messagebox.showinfo("Disponibilidade", "O livro está disponível.")
                else:
                    messagebox.showinfo("Disponibilidade", "O livro está indisponível.")
                return
        messagebox.showinfo("Erro", "Livro não encontrado.")

    def pesquisar_livro(self, chave):
        resultados = []
        for livro in self.livros:
            if chave.lower() in livro.titulo.lower() or chave.lower() in livro.autor.lower():
                resultados.append(livro)
        if resultados:
            mensagem = ""
            for livro in resultados:
                mensagem += f"Título: {livro.titulo}, Autor: {livro.autor}, Exemplares disponíveis: {livro.exemplares}\n"
            messagebox.showinfo("Resultados", mensagem)
        else:
            messagebox.showinfo("Resultados", "Nenhum livro encontrado com esse título ou autor.")

catalogo = Catalogo()

def cadastrar_livro():
    titulo = titulo_entry.get()
    autor = autor_entry.get()
    exemplares = exemplares_entry.get()
    livro = Livro(titulo, autor, exemplares)
    catalogo.cadastrar_livro(livro)

def validar_disponibilidade():
    titulo = titulo_entry.get()
    catalogo.validar_disponibilidade(titulo)

def pesquisar_livro():
    chave = chave_entry.get()
    catalogo.pesquisar_livro(chave)

def abrir_programa():

    pass


root = tk.Tk()
root.title("Sistema de Biblioteca")


titulo_label = tk.Label(root, text="Título:")
titulo_label.grid(row=0, column=0, sticky="w")
titulo_entry = tk.Entry(root)
titulo_entry.grid(row=0, column=1)

autor_label = tk.Label(root, text="Autor:")
autor_label.grid(row=1, column=0, sticky="w")
autor_entry = tk.Entry(root)
autor_entry.grid(row=1, column=1)

exemplares_label = tk.Label(root, text="Exemplares:")
exemplares_label.grid(row=2, column=0, sticky="w")
exemplares_entry = tk.Entry(root)
exemplares_entry.grid(row=2, column=1)

chave_label = tk.Label(root, text="Chave de busca:")
chave_label.grid(row=3, column=0, sticky="w")
chave_entry = tk.Entry(root)
chave_entry.grid(row=3, column=1)

cadastrar_button = tk.Button(root, text="Cadastrar livro", command=cadastrar_livro)
cadastrar_button.grid(row=4, column=0, columnspan=2, pady=5)

validar_button = tk.Button(root, text="Validar disponibilidade", command=validar_disponibilidade)
validar_button.grid(row=5, column=0, columnspan=2, pady=5)

pesquisar_button = tk.Button(root, text="Pesquisar livro", command=pesquisar_livro)
pesquisar_button.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()
