# > LISTAS

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com listas
notas = [7.9, 9.7, 8.2]


# Criando Listas
lista = []
lista = list()
lista = [37, 'Leila', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]


# Indexação e Slices (fatiamento)

lista = [10, 'Leilaine', 3.1415, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# Slices

lista= [10, 50, 30, 40, 25, 60, 5]

print(lista[0:4]) #pega os três primeiros itens da lista
print(lista[3:6])
print(lista[3:]) # pega a partir do terceiro item até o ultimo
print(lista[2:6:2]) # pega do segundo ao sexto item da lista pulando de dois em dois numeros

# > Iterações com FOR

# 1. Utilizando os próprios elementos da lista
for elemento in lista:
    print(elemento)

# 2. Utilizando os índices

print('Comprimento da lista', len(lista))

for i in range(len(lista)):
    print(lista[i])

# MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]

# append

print(lista)

lista.append(3) #adicionar no final da lista

print('Depois do append: ', lista)

# insert

lista.insert(2, 10) # adiciona item(10) na posição dois da lista
print('Depois do insert: ', lista)

# extend

lista2 = [1, 2, 3]
lista.extend(lista2)
print('Depois do extend: ', lista)

# pop

lista.pop() # deleta ultimo elemento da lista
lista.pop(0) # retira o elemento referente posição indicada, no caso o primeiro item da lista.

print('Depois do pop: ', lista)

# remove

lista.remove(3) #diz qual o elemento que quer tirar. Sempre o primeiro encontrado.
print('Depois do remove: ', lista)

# count

print('Quantidade de 2 na lista: ', lista.count(2)) #Quantidade de determinado elemento na lista

# index

print('Índice do elemento 12: ', lista.index(12)) # Mostra o ídice (lugar) do item na lista

# sort

lista.sort(reverse = True) # Ordena lista. Comando 'reverse = True' coloca lista em ordem decrecente
print(lista)


# FUNÇÕES PARA LISTA

#len

print (len(lista)) #saber quantos elementos tem na lista

# sum

print(sum(lista)) # soma todos os elementos da lista

# max

print('Maior elemento da lista: ', max(lista))

# min

print('Menor elemento da lista: ', min(lista))

