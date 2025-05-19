
inventario = {}

def adicionar_item(nome, quantidade=1, tipo=None, dano=0, cura=0, descricao=""):
    if nome in inventario:
        inventario[nome]["quantidade"] += quantidade
    else:
        inventario[nome] = {
            "quantidade": quantidade,
            "tipo": tipo,         # Ex: "arma", "consumível", "chave", etc.
            "dano": dano,         # Se for uma arma
            "cura": cura,         # Se for uma poção
            "descricao": descricao
        }
    print(f"{quantidade}x {nome} adicionado(s) ao inventário.")

def remover_item(nome, quantidade=1):
    if nome in inventario:
        inventario[nome]["quantidade"] -= quantidade
        if inventario[nome]["quantidade"] <= 0:
            del inventario[nome]
        print(f"{quantidade}x {nome} removido(s) do inventário.")
    else:
        print(f"{nome} não está no inventário.")

def mostrar_inventario():
    print("\n=== INVENTÁRIO ===")
    if not inventario:
        print("Seu inventário está vazio.")
        input("\nPressione Enter para continuar...")
    else:
        for nome, info in inventario.items():
            print(f"{nome} x{info['quantidade']}")
            if info["tipo"]: print(f"  Tipo: {info['tipo']}")
            if info["dano"]: print(f"  Dano: {info['dano']}")
            if info["cura"]: print(f"  Cura: {info['cura']}")
            if info["descricao"]: print(f"  Descrição: {info['descricao']}")
            input("\nPressione Enter para continuar...")
