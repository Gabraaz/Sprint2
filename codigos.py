#             ~~𝓘𝓜𝓟𝓞𝓡𝓣𝓢~~

from player.inventario import adicionar_item
from util import clear_screen
from playsound import playsound


codigos_validos = {
    "AVENTURA10": {
        "mensagem": "Você ganhou 2x Poção de Vida!",
        "recompensas": [("Poção de Vida", 2, "Consumível", 0, "Cura 30 de vida.")]
    },
    "DRAGAO2025": {
        "mensagem": "Você ganhou 1x Espada Flamejante!",
        "recompensas": [("Espada Flamejante", 1, "Arma Especial", 25, "Uma espada que cospe fogo ao atacar.")]
    },
    "OURO100": {
        "mensagem": "Você ganhou 100 moedas de ouro!",
        "recompensas": [("Ouro", 100, "Moeda", 0, "Dinheiro usado para comprar itens.")]
    },
    "CANIVETE123": {
        "mensagem": "Você ganhou 1x Canivete Enferrujado!",
        "recompensas": [("Canivete Enferrujado", 1, "Arma Básica", 5, "Um canivete velho, mas um pouco afiado.")]
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

            for nome, quantidade, tipo, dano, descricao in recompensa["recompensas"]:
                adicionar_item(nome, quantidade, tipo, dano, descricao)

            codigos_resgatados.add(codigo)
            print("✅ Código resgatado com sucesso!\n")
            playsound("sons/entrartela.mp3")
        else:
            print("❌ Código inválido.\n")
            playsound("sons/mensagemerro.mp3")
