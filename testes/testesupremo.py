from InquirerPy import inquirer

def menu_interativo():
    escolha = inquirer.select(
        message="Escolha uma opção:",
        choices=[
            "Jogar",
            "Ler Regras",
            "Resgatar Código",
            "Sair"
        ],
        default="Jogar",
        pointer="👉",
        instruction="Use as setas ↑ ↓ e Enter para selecionar"
    ).execute()

    print(f"Você escolheu: {escolha}")

menu_interativo()
