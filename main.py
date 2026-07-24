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
    print("8 - Sair")
    print(" ")

livros = []
while True:
    mostrar_menu()
       
    escolha = int(input("Escolha uma opçâo: "))

    if escolha == 1:
        print("1 - Cadastrando Livro")
        nome = input("qual livro deseja cadastrar ?: ")
        ano = int(input("ano: "))
        autor = input("Autor: ")
        livro = {
            "titulo": nome,
            "autor": autor,
            "ano": ano }
        livros.append(livro)
    
    elif escolha == 2:
        print("===== LIVROS CADASTRADOS =====")
        if livros:
            for livro in livros:
                print("Título:", livro["titulo"])
                print("Autor:", livro["autor"])
                print("Ano:", livro["ano"])
                print()
                
        else:
            print("sem livros cadastrados")
       
    elif escolha == 3:
        buscar = input("Digite o nome do livro: ").strip()
        encontrado = False

        for livro in livros:
            if buscar.lower() in livro["titulo"].lower():
                print("Livro encontrado!")
                print("Título:", livro["titulo"])
                print("Autor:", livro["autor"])
                print("Ano:", livro["ano"])                    
                print()

                encontrado = True
                break

        if not encontrado:
            print("Livro não encontrado.")

    elif escolha ==4:
        buscar = input("Digite o nome do livro: ").strip()
        encontrado = False

        for livro in livros:
            if buscar.lower() in livro["titulo"].lower():
                livros.remove(livro)
                print("Livro removido com sucesso!")

                encontrado = True
                break

        if not encontrado: 
            print("livro não encontrado")

    elif escolha ==5:
        buscar = input("Digite o nome do livro: ").strip()
        encontrado = False

        for livro in livros:
             if buscar.lower() in livro["titulo"].lower():
                livro["titulo"] = input("Novo Titulo: ")
                livro["autor"] = input("Novo Autor: ")
                livro["ano"] = int(input("Novo Ano: "))
                print("Livro editado com sucesso!")

                encontrado = True
                break    

        if not encontrado: 
            print("livro não encontrado")     

    elif escolha ==8:
        print("8 - Encerrando Sistema")
        break
    
    else:
        print("Código inválido")