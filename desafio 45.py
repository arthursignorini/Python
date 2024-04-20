import random
op1 = 'PEDRA'
op2 = 'PAPEL'
op3 = 'TESOURA'
print('\033[34m BORA JOGAR! \033[m')
n = str(input('\033[34m Qual é o seu nome? \033[m '))
print('\033[34m-=\033[m' * 15)
print('\033[34m Você pode escolher entre PEDRA, PAPEL ou TESOURA \033[m')
jogada = input('\033[34m Qual é a sua jogada? ')
print('-=' * 15)
op= [op1, op2, op3]
pc = random.choice(op)
print(f'Eu escolho {pc}')
print('-=' * 15)
if jogada == pc:
    print('EMPATOU')
elif jogada == op1 and pc == op2:
    print('EU GANHEI')
elif jogada == op1 and pc == op3:
    print(f'VOCE GANHOU {n}')
elif jogada == op2 and pc == op3:
    print('EU GANHEI')
elif jogada == op2 and pc == op1:
    print(f'VOCE GANHOU {n}')
elif jogada == op3 and pc == op1:
    print('EU GANHEI')
elif jogada == op3 and pc == op2:
    print(f'VOCE GANHOU {n}')
