import banco

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

def cadastrar_livro():
    print("1 - Cadastrando Livro")
    nome = input("qual livro deseja cadastrar ?: ")
    while True:
        try:
            ano = int(input("Ano: "))
            break
        except ValueError:
            print("Digite um número válido.")
    autor = input("Autor: ")
    
    banco.cadastrar_livro(nome, autor, ano)

def listar_livros():
    livros = banco.listar_livros()
    
    print("===== LIVROS CADASTRADOS =====")
    
    if livros:
        for livro in livros:
            print("ID:", livro[0])
            print("Título:", livro[1])
            print("Autor:", livro[2])
            print("Ano:", livro[3])
            print()

    else:
        print("Sem livros cadastrados.")
    
def buscar_livro():
    buscar = input("Digite o nome do livro: ").strip()

    livros = banco.buscar_livro(buscar)
        
    if livros:
        print("Livro encontrado!")
        
        for livro in livros:
            
            print()
            print("ID:", livro[0])
            print("Título:", livro[1])
            print("Autor:", livro[2])
            print("Ano:", livro[3])                    
            print()
    else:
        print("Livro não encontrado.")

def remover_livro():
    while True:
        try:
            id = int(input("Digite o ID do livro: "))
            
            break
        except ValueError:
            print("Digite um número válido.")
            
    
    banco.remover_livro(id)
    print("Livro removido com sucesso")

def editar_livro():  
    while True:
        try:
            id = int(input("Digite o ID do livro: "))               
            break
        except ValueError:
            print("Digite um ID válido.")
        
    titulo = input("Novo título: ")
    autor = input("Novo autor: ")
        
    while True:
            try:
                ano = int(input("Digite o ano do livro: "))               
                break
            except ValueError:
                print("Digite um ano válido.")
          
    banco.editar_livro(id, titulo, autor ,ano)        
    print("Livro editado com sucesso!")
    

while True:
    mostrar_menu()
    while True:
        try:
            escolha = int(input("Escolha uma opçâo: "))
            break
        except ValueError:
            print("Digite um número válido.")
        
    if escolha == 1:
        cadastrar_livro()
    
    elif escolha == 2:
        listar_livros()
       
    elif escolha == 3:
        buscar_livro()

    elif escolha ==4:
        remover_livro()

    elif escolha ==5:
        editar_livro()   

    elif escolha ==6:
        print("6 - Encerrando Sistema")
        break
    
    else:
        print("Código inválido")