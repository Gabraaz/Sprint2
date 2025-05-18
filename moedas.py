# moedas.py

saldo = 50  # Começa com 50 moedas

def mostrar_saldo():
    return saldo

def gastar(valor):
    global saldo
    if saldo >= valor:
        saldo -= valor
        print(f"Gastou {valor} moedas. Saldo agora: {saldo}.")
        return True
    else:
        print("Moedas insuficientes!")
        return False

def ganhar(valor):
    global saldo
    saldo += valor
    print(f"Ganhou {valor} moedas. Saldo agora: {saldo}.")
