import time

#Etapa 1
Beatles = []
print("Etapa 1: ", Beatles)

#Etapa 2
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Etapa 2: ", Beatles)

#Etapa 3
tamanho_lista = (len(Beatles))
for i in range(tamanho_lista // 2):
    primeiromembro = str(input("Digite Stu Sutcliffe para adicionar ele a lista: "))
    Beatles.append(primeiromembro)
    segundomembro = str(input("Digite Pete Best para adicionar ele a lista: "))
    Beatles.append(segundomembro)
print("etapa 3: ", Beatles)

#Etapa 4
del Beatles[-1]
del Beatles[-1]
print("Etapa 4: ", Beatles)

#Etapa 5
Beatles.insert(0, "Ringo Starr")
print("Etapa 5: ", Beatles)

time.sleep(5)