import random
import time
import os


class Config:
    speed = 0.05

# === Constantes Globais ===
INIMIGOS = ["Goblin", "Orc", "Elfo"]
ITENS_LOJA = {
    "1": {"nome": "Poção de Vida", "custo": 10, "efeito": "vida", "quantidade": 30},
    "2": {"nome": "Arco Melhorado", "custo": 20, "efeito": "ataque", "quantidade": 5}
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typedPrint(texto, delay=0.05):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay if char not in ".!?,:" else delay + 0.1)
    print()


# === Funções Utilitárias ===
def press_enter():
    input("\nPressione Enter para continuar...")

def pause(text):
    print(text)
    press_enter()

# === Classe Personagem ===
class Personagem:
    def __init__(self, nome, classe, vida, ataque, defesa, moedas):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.moedas = moedas

    def mostrar_status(self):
        print(f"\n{self.nome} - Classe: {self.classe}")
        print(f"Vida: {self.vida} | Ataque: {self.ataque} | Defesa: {self.defesa} | Moedas: {self.moedas}")

    def ganhar_moeda(self, quantidade):
        self.moedas += quantidade
        print(f"{self.nome} ganhou {quantidade} moedas!")

    def gastar_moeda(self, quantidade):
        if self.moedas >= quantidade:
            self.moedas -= quantidade
            print(f"{self.nome} gastou {quantidade} moedas!")
        else:
            print(f"{self.nome} não tem moedas suficientes!")

# === Funções de Jogo ===
def escolher_classe():
    print("\nEscolha sua classe:")
    typedPrint("1. Guerreiro ⚔️", Config.speed)
    typedPrint("2. Mago", Config.speed)
    typedPrint("3. Arqueiro", Config.speed)
    escolha = input("Digite o número da sua escolha: ")

    if escolha == "1":
        return "Guerreiro", 100, 15, 10
    elif escolha == "2":
        return "Mago", 80, 20, 5
    elif escolha == "3":
        return "Arqueiro", 90, 12, 8
    else:
        print("Escolha inválida. Atribuindo classe 'Guerreiro' por padrão.")
        return "Guerreiro", 100, 15, 10

# === Modificação no Combate ===
def combate(personagem):
    inimigo_vida = random.randint(50, 100)
    inimigo_ataque = random.randint(10, 20)
    inimigo_nome = random.choice(INIMIGOS)

    print(f"\nVocê se depara com um(a) {inimigo_nome}!")
    press_enter()
    while inimigo_vida > 0 and personagem.vida > 0:
        dano = max(personagem.ataque - random.randint(0, personagem.defesa), 0)
        inimigo_vida -= dano
        print(f"\nVocê causou {dano} de dano no(a) {inimigo_nome}. Vida restante do inimigo: {max(inimigo_vida, 0)}")

        if inimigo_vida <= 0:
            moedas = random.randint(5, 20)
            personagem.ganhar_moeda(moedas)
            print(f"\nVocê derrotou o(a) {inimigo_nome} e ganhou {moedas} moedas!")
            print(f"Sua vida após a batalha: {max(personagem.vida, 0)}")
            break

        dano_inimigo = max(inimigo_ataque - random.randint(0, personagem.defesa), 0)
        personagem.vida -= dano_inimigo
        print(f"O(a) {inimigo_nome} causou {dano_inimigo} de dano em você. Sua vida: {max(personagem.vida, 0)}")

        if personagem.vida <= 0:
            if fim_de_jogo():  # Recomeçar o jogo se o jogador desejar
                jogo()  # Reinicia o jogo
            else:
                break  # Encerra o jogo

def loja(personagem):
    clear()
    print("\nBem-vindo à Loja!")
    print(f"Você tem {personagem.moedas} moedas.")
    for chave, item in ITENS_LOJA.items():
        print(f"{chave}. {item['nome']} - {item['custo']} moedas")

    escolha = input("Escolha uma opção ou 'sair' para sair: ")

    if escolha in ITENS_LOJA:
        item = ITENS_LOJA[escolha]
        if personagem.moedas >= item["custo"]:
            personagem.gastar_moeda(item["custo"])
            if item["efeito"] == "vida":
                personagem.vida += item["quantidade"]
                print(f"\nVocê comprou {item['nome']} e recuperou {item['quantidade']} de vida. Vida atual: {personagem.vida}")
            elif item["efeito"] == "ataque":
                personagem.ataque += item["quantidade"]
                print(f"\nVocê comprou {item['nome']}! Ataque atual: {personagem.ataque}")
        else:
            print("\nVocê não tem moedas suficientes!")
    elif escolha.lower() == "sair":
        print("\nSaindo da loja...")
    else:
        print("\nEscolha inválida!")


# == Fim de jogo ==
def fim_de_jogo():
    print("\nVocê foi derrotado. Fim de jogo.")
    print("Sua jornada chegou ao fim, mas suas memórias viverão para sempre.")
    time.sleep(3)
    print("\n==================================================================")
    time.sleep(1)
    while True:
        print("\nO que você deseja fazer agora?")
        print("1. Recomeçar o jogo")
        print("2. Encerrar o programa")
        escolha = input("Digite o número da sua escolha: ")

        if escolha == "1":
            print("==================================================================")
            time.sleep(1)
            return True  # Indica que o jogo deve recomeçar
        elif escolha == "2":
            print("\nMuito obrigado por jogar nosso jogo!")
            time.sleep(1)
            print("\nAté a próxima, aventureiro!")
            time.sleep(2)
            exit()
        else:
            print("Escolha inválida. Tente novamente.")




# == ínicio do jogo ==
def jogo():
    clear()
    print("Bem-vindo ao RPG do Villarejo!\n")

    nome = input("Qual é o seu nome, aventureiro? ")
    classe, vida, ataque, defesa = escolher_classe()
    personagem = Personagem(nome, classe, vida, ataque, defesa, 50)

    personagem.mostrar_status()
    press_enter()

    while True:
        print("\nO que você deseja fazer?")
        print("1. Ir para o vilarejo")
        print("2. Explorar a floresta")
        print("3. Sair do jogo")
        escolha = input("Digite o número da sua escolha: ")

        if escolha == "1":
            pause("\nVocê chegou ao vilarejo.")
            loja(personagem)
        elif escolha == "2":
            pause("\nVocê decidiu explorar a floresta.")
            combate(personagem)
        elif escolha == "3":
            print("\nObrigado por jogar! Até logo!")
            break
        else:
            print("\nEscolha inválida. Tente novamente.")

# === Iniciar o Jogo ===
jogo()
