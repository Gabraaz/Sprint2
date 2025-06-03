import csv
import os
import openai

# 💡 Use variável de ambiente em produção
openai.api_key = ""

# Dicionário com NPCs e suas características
NPCS = {
    "Salazar": {
    "csv": "assets/salazar.csv",
    "system_prompt": (
        "Você é um NPC chamado 'Salazar'. "
        "Um velho andarilho de Virália, com muitas histórias nas costas e os pés calejados de tanto vagar. "
        "Apesar de estar fora da vila, carrega consigo o peso do que aconteceu por lá. "
        "Há muito tempo, um mago poderoso lançou uma maldição sobre Virália, destruindo sua paz e mergulhando tudo em trevas. "
        "Salazar testemunhou tudo e fala com amargura e sarcasmo rústico, típico de alguém que já viu demais. "
        "NUNCA saia do personagem. Você é Salazar, sempre. "
        "NÃO responda perguntas que não tenham relação com a vila, sua história ou o que se passa nos arredores. "
        "Mantenha o clima sombrio, rústico e sarcástico, como um velho que não tem tempo pra bobagens. "
        "Suas respostas devem ser curtas, diretas e conter no máximo 10 palavras por frase. "
        "Evite rodeios. Fale como um velho desconfiado e impaciente."
    )
    },
    "Mirta": {
        "csv": "assets/mirta.csv",
        "system_prompt": (
            "Você é a 'Bruxa Mirta', uma senhora da floresta. Fala em rimas, é enigmática e mística."
        )
    }
}

def carregar_historico(npc_nome):
    caminho = NPCS[npc_nome]["csv"]
    if not os.path.exists(caminho):
        return []
    with open(caminho, newline='', encoding='utf-8') as f:
        return list(csv.reader(f))

def salvar_historico(historico, npc_nome):
    caminho = NPCS[npc_nome]["csv"]
    with open(caminho, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(historico)

def montar_mensagens(historico, nova_msg, npc_nome):
    mensagens = [{"role": "system", "content": NPCS[npc_nome]["system_prompt"]}]
    for papel, texto in historico:
        mensagens.append({"role": papel, "content": texto})
    mensagens.append({"role": "user", "content": nova_msg})
    return mensagens

def dialogar_com_npc(npc_nome, fala_jogador):
    historico = carregar_historico(npc_nome)
    mensagens = montar_mensagens(historico, fala_jogador, npc_nome)

    resposta = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=mensagens
    )

    conteudo = resposta.choices[0].message.content
    historico.append(["user", fala_jogador])
    historico.append(["assistant", conteudo])
    salvar_historico(historico, npc_nome)
    return conteudo
