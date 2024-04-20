import random
e = int(input('Escolha um número de 0 a 10: '))
n = random.randint(1,10)
if e == n:
    print('Voce acertou ')
else:
    print('Voce errou...')
print(f'O número escolhido foi {n}')

