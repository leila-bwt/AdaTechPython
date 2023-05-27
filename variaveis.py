 # > VARIÁVEIS

'''Os comentários podem ser feitos com uso da #
ou então, em comentários maiores,
usamos as três aspas'''

idade = 37 # para criar uma variavél é necessario o nome e valor somente.

print(idade)

nome = 'Leilaine Borges' # Textos são escritos com aspas simples ou duplas

print(nome)

'''
Tipos de Variáveis:
int: números inteiros;
float: números reais;
str: (string) cadeia de caracteres;
bool: valores lógicos (booleano);
'''

idade = 38
altura = 1.62
nome = 'Leila Borges'
estudando = True

#usa-se o 'type' para imprimir/consultar o tipo da variável
print(type(nome))
print(type(idade))
print(type(altura))
print(type(estudando))

linguagem = input('Qual é a linguagem de programação que você está estudando?')

print('A linguagem que você está estudando é: ', linguagem)

print(nome, idade, altura, linguagem)