""" Recebe a informação de operação"""
operation = input('''
Selecione a operação matemática que gostaria de completar:
+ para soma
- para subtração
* para multiplicação
/ para divisão
''')
"""Recebe as variáveis"""
number_1 = int(input('Adicione o primeiro valor: '))
number_2 = int(input('Adicione o segundo valor '))

"""Realiza validação e calculo"""
if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('Você não selecionou nenhuma operação correta.')
