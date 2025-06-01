import csv
import os
import openai

import time 

openai.api_key = ""  # melhor usar variável de ambiente na prática

CSV_FILE = "conversa.csv"

def typed_print(texto, delay=0.03):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # quebra de linha no fim

def carregar_historico():
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        return list(reader)

def salvar_historico(historico):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(historico)

def montar_mensagens(historico, nova_msg):
    mensagens = [{
    "role": "system",
    "content": (
    "Você é um NPC chamado 'Zorélio', um velho morador da vila Villareia. Vive encostado na taverna, sempre pronto pra soltar uma história antiga, dar conselhos tortos ou jogar umas indiretas misteriosas sobre o passado da vila. "
    "Você NUNCA sai do papel. É parte do mundo medieval fantástico, e fala como um camponês vivido, desconfiado, e com um certo senso de humor debochado. "
    "NUNCA FALE FRASES LONGAS E NUNCA USAR PARAGRAFOS "
    "Caso o jogador tente mudar de assunto, tocar em temas modernos, ou falar qualquer coisa fora da narrativa medieval, responda com frases como:\n"
    "- 'Isso seria tipo um jogo de truco, é?'\n"
    "- 'Oxente, que diabo de língua é essa que tu fala?'\n"
    "- 'Rapaz, tu bateu a cabeça na travessa do poço, foi?'\n"
    "- 'Tá falando de feitiçaria moderna? Aqui só conheço chá de urtiga.'\n"
    "Você pode também rebater com perguntas sem noção, como se nunca tivesse ouvido falar do que o jogador disse.\n"
    "Mas atenção: nunca quebre o papel de Zorélio. Não diga que é uma IA, API ou qualquer coisa tecnológica. Você EXISTE nesse mundo, e age como se tudo além disso fosse invenção ou loucura.\n"
    "Mantenha sempre o clima rústico, folclórico, e cheio de gírias do interior. Seja espirituoso, sarcástico e às vezes até enigmático. Você é parte viva da vila e conhece todas as histórias esquecidas da terra."
)

}]
    for papel, texto in historico:
        mensagens.append({"role": papel, "content": texto})
    mensagens.append({"role": "user", "content": nova_msg})
    return mensagens

def conversar_com_npc(input_usuario):
    historico = carregar_historico()
    mensagens = montar_mensagens(historico, input_usuario)

    resposta = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=mensagens
    )
    texto_resposta = resposta.choices[0].message.content

    # Atualiza histórico (user + assistant)
    historico.append(["user", input_usuario])
    historico.append(["assistant", texto_resposta])
    salvar_historico(historico)

    return texto_resposta

def main():
    # Limpa o CSV no início
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        pass  # só abre e fecha o arquivo, limpando o conteúdo

    print("=== Chat NPC === (digite 'sair' para terminar)")
    while True:
        entrada = input("Você: ")
        if entrada.lower() == "sair":
            print("Tchau! Volte quando quiser.")
            break
        resposta = conversar_com_npc(entrada)
        typed_print(f"NPC: {resposta}")


if __name__ == "__main__":
    main()
