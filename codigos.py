#             ~~𝓘𝓜𝓟𝓞𝓡𝓣𝓢~~

from personagem.inventario import adicionar_item
from util import clear_screen
from playsound import playsound


codigos_validos = {
    "AVENTURA10": {
        "mensagem": "Você ganhou 2x Poção de Vida!",
        "recompensas": [("Poção de Vida", 2)]
    },
    "DRAGAO2025": {
        "mensagem": "Você ganhou 1x Espada Flamejante!",
        "recompensas": [("Espada Flamejante", 1)]
    },
    "OURO100": {
        "mensagem": "Você ganhou 100 moedas de ouro!",
        "recompensas": [("Ouro", 100)]
    }
}

codigos_resgatados = set()

def tela_resgate_codigo(jogador):
    clear_screen()
    print("\n===== 🧾 RESGATAR CÓDIGO PROMOCIONAL =====")
    print("Digite um código ou deixe vazio para sair.")

    while True:
        codigo = input("Código: ").strip().upper()

        if codigo == "":
            print("Saindo da tela de códigos.\n")
            playsound("sons/voltartela.mp3")

            break

        if codigo in codigos_resgatados:
            print("⚠️  Esse código já foi usado.\n")
        elif codigo in codigos_validos:
            recompensa = codigos_validos[codigo]
            print(f"🎁 {recompensa['mensagem']}")
            codigos_resgatados.add(codigo)
            print("✅ Código resgatado com sucesso!\n")
            playsound("sons/entrartela.mp3")
        else:
            print("❌ Código inválido.\n")
            playsound("sons/mensagemerro.mp3")

            
