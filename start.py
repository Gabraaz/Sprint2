def menu_inicial():
    clear()
    print("=" * 50)
    print("🎮  BEM-VINDO AO RPG DO VILLAREJO")
    print("=" * 50)
    print("1. Iniciar o jogo")
    print("2. Ler as regras")
    print("3. Inserir código secreto")
    print("4. Sair")

    while True:
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            return  # segue pro jogo()
        elif escolha == "2":
            mostrar_regras()
            clear()
            menu_inicial()  # volta ao menu depois
            return
        elif escolha == "3":
            aplicar_codigo_secreto()
            clear()
            menu_inicial()
            return
        elif escolha == "4":
            print("Até a próxima, aventureiro!")
            exit()
        else:
            print("Opção inválida. Tente novamente.")
