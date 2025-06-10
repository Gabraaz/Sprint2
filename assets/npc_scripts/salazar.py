from assets.npc_chat import dialogar_com_npc

# Variáveis de estado do diálogo
estado_dialogo = 0
dialogo_concluido = False

# Salazar tem um mini-roteiro dividido em etapas
roteiro_salazar = [
    "Salazar: Então... você realmente veio até aqui? A floresta não costuma ser gentil com forasteiros.",
    "Salazar: A vila não fica longe. Anda comigo. Vou te contar o que aconteceu por lá.",
    # Fase de diálogo dinâmico (controlado pela API)
    "API_DIALOGO",
    "Salazar: Chegamos. Olha a torre caída... é desde aquela maldição do mago Griffin.",
    "Salazar: Vamos pra taverna. Zorélio deve estar lá, bêbado como sempre."
]

def primeiraFala_salazar(fala_do_jogador):
    global estado_dialogo, dialogo_concluido
    
    # Verifica se já terminou todo o diálogo
    if dialogo_concluido and estado_dialogo >= len(roteiro_salazar):
        return "Salazar: Já falei tudo que tinha pra dizer. Agora segue teu caminho.", True
    
    # Verifica se já passou por todas as etapas
    if estado_dialogo >= len(roteiro_salazar):
        return "Salazar: *fica em silêncio, olhando para a distância*", False
    
    etapa = roteiro_salazar[estado_dialogo]
    
    if etapa == "API_DIALOGO":
        resposta, objetivos_cumpridos = dialogar_com_npc("Salazar", fala_do_jogador)
        if objetivos_cumpridos:
            estado_dialogo += 1  # avança para a próxima etapa do roteiro
            dialogo_concluido = True
        return resposta, objetivos_cumpridos
    else:
        estado_dialogo += 1
        return etapa, False