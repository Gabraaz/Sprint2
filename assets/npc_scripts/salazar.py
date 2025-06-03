from assets.npc_chat import dialogar_com_npc

# Salazar tem um mini-roteiro dividido em etapas
roteiro_salazar = [
    "Salazar: Então... você realmente veio até aqui? A floresta não costuma ser gentil com forasteiros.",
    "Salazar: A vila não fica longe. Anda comigo. Vou te contar o que aconteceu por lá.",
    # Aqui entra um trecho dinâmico (via API):
    "API",
    "API",
    "API",
    "API",
    "API",
    "API",
    "API",
    "Salazar: Chegamos. Olha a torre caída... é desde aquela maldição do mago Griffin.",
    "Salazar: Vamos pra taverna. Zorélio deve estar lá, bêbado como sempre."
]

estado_dialogo = 0  # progresso do NPC (você pode salvar isso no seu save também)

def primeiraFala_salazar(fala_do_jogador):
    global estado_dialogo

    if estado_dialogo >= len(roteiro_salazar):
        return "Salazar: Já falei tudo que tinha pra dizer. Agora segue teu caminho."

    etapa = roteiro_salazar[estado_dialogo]
    estado_dialogo += 1

    if etapa == "API":
        return dialogar_com_npc("Salazar", fala_do_jogador)
    else:
        return etapa
