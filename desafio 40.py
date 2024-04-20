n1 = float(input('nota: '))
n2 = float(input('nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('\033[31m REPROVADO \033[m')
elif media <= 6.9 and media >= 5.0:
    print('\033[31m RECUPERAÇÃO \033[m')
else:
    print('\033[32m APROVADO \033[m')
