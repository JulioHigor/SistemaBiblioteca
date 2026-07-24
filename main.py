def mostrar_menu():
    print("=========================")
    print("   Sistema Biblioteca")
    print("=========================")
    print(" ")
    print("1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Buscar Livro")
    print("4 - remover Livro")
    print("5 - editar Livro")
    print("6 - Sair")
    print(" ")

def encontrar_livro(livro, buscar):
    for livro in livros:
        if buscar.lower() in livro["titulo"].lower():
            return livro

    return None

def cadastrar_livro(livros):
    print("1 - Cadastrando Livro")
    nome = input("qual livro deseja cadastrar ?: ")
    ano = int(input("ano: "))
    autor = input("Autor: ")
    livro = {
        "titulo": nome,
        "autor": autor,
        "ano": ano }
    livros.append(livro)

def listar_livros(livros):
        print("===== LIVROS CADASTRADOS =====")
        if livros:
            for livro in livros:
                print("Título:", livro["titulo"])
                print("Autor:", livro["autor"])
                print("Ano:", livro["ano"])
                print()
                
        else:
            print("sem livros cadastrados")

def buscar_livro(livros):
    buscar = input("Digite o nome do livro: ").strip()

    livro = encontrar_livro(livros, buscar)
        
    if livro:
        print("Livro encontrado!")
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])                    
        print()

    else:
        print("Livro não encontrado.")

def remover_livro(livros):
    buscar = input("Digite o nome do livro: ").strip()

    livro = encontrar_livro(livros, buscar)

    if livro:
        livros.remove(livro)
        print("Livro removido com sucesso!")
    else:
        print("Livro não encontrado.")

def editar_livro(livros):
    buscar = input("Digite o nome do livro: ").strip()

    livro = encontrar_livro(livros, buscar)

    if livro:
        livro["titulo"] = input("Novo título: ")
        livro["autor"] = input("Novo autor: ")
        livro["ano"] = int(input("Novo ano: "))
        print("Livro editado com sucesso!")
    else:
        print("Livro não encontrado.")

livros = []
while True:
    mostrar_menu()

    escolha = int(input("Escolha uma opçâo: "))

    if escolha == 1:
        cadastrar_livro(livros)
    
    elif escolha == 2:
        listar_livros(livros)
       
    elif escolha == 3:
        buscar_livro(livros)

    elif escolha ==4:
        remover_livro(livros)

    elif escolha ==5:
        editar_livro(livros)   

    elif escolha ==6:
        print("6 - Encerrando Sistema")
        break
    
    else:
        print("Código inválido")
        
