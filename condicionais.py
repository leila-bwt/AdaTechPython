# > ESTRUTURAS CONDICIONAIS

idade = 17

if idade >= 18:
    print('Você é maior de idade. ')
else:
    print('Você é menor de idade. ')


'''
Imagine que você queira imprimir "Aprovado", caso o estudante
tenha uma média superior ou igual a 7. e "Reprovado", caso a média
seja inferior a 7.
'''

'''nota1 = int (input ('Digite o valor da primeira nota: '))
nota2 = int (input ('Digite o valor da segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print('APROVADO')
elif media >= 5:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')'''


    #COMPARAÇÃO CONJUNTA (and - or)

media2 = 9
presenca = 70

if media2 >= 7 and presenca >= 70:
    print('APROVADO')
else:
    print('REPROVADO')

