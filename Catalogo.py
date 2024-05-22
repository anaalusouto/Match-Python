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
        print("Livro cadastrado com sucesso!")

    def validar_disponibilidade(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.exemplares > 0:
                    print("O livro está disponível.")
                else:
                    print("O livro está indisponível.")
                return
        print("Livro não encontrado.")

    def pesquisar_livro(self, chave):
        resultados = []
        for livro in self.livros:
            if chave.lower() in livro.titulo.lower() or chave.lower() in livro.autor.lower():
                resultados.append(livro)
        if resultados:
            for livro in resultados:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}, Exemplares disponíveis: {livro.exemplares}")
        else:
            print("Nenhum livro encontrado com esse título ou autor.")

catalogo = Catalogo()

def exibir_menu():
    print("MENU:")
    print("1. Cadastrar livro")
    print("2. Validar disponibilidade")
    print("3. Pesquisar livro")
    print("4. Sair")

def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    exemplares = int(input("Digite o número de exemplares disponíveis: "))
    livro = Livro(titulo, autor, exemplares)
    catalogo.cadastrar_livro(livro)

def validar_disponibilidade():
    titulo = input("Digite o título do livro: ")
    catalogo.validar_disponibilidade(titulo)

def pesquisar_livro():
    chave = input("Digite o título ou autor do livro: ")
    catalogo.pesquisar_livro(chave)

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_livro()
    elif opcao == "2":
        validar_disponibilidade()
    elif opcao == "3":
        pesquisar_livro()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

