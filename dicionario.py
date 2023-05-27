# > DICIONÁRIOS

# Criando dicionários

dicionario = {}
dicionario = dict=()

dicionario = {'nome': 'Leila', 'idade': 37, 'altura': 1.62}

print(dicionario)
print(dicionario['idade'])



# Adicionando elementos em um dicionário

dicionario['programador'] = True
print(dicionario)

dicionario['altura'] = 1.7

print(dicionario)

# Iterando sobre um dicionário // Percorrer elementos do dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave    

print('peso' in dicionario)
print('altura' in dicionario)


