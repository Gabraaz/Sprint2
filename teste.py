from InquirerPy import inquirer
from InquirerPy.utils import Style

# 1. Definir o estilo como um dicionário simples
style_dict = {
    "questionmark": "#e5c07b",
    "answer": "#61afef",
    "input": "#98c379",
    "question": "",
    "pointer": "#61afef",
    "instruction": ""
}

# 2. Usar a abordagem alternativa que funciona na versão 0.3.4
opcao = inquirer.select(
    message="Sua mensagem aqui",
    choices=["Opção 1", "Opção 2", "Opção 3"]
    # Sem parâmetro style
).execute()