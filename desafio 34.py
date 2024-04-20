s = float(input('Qual é o seu salário? '))
s1 = s * 1.10
s2 = s * 1.15
if s > 1250:
    print(f'Seu salário será de {s1} reais')
else:
    print(f'Seu salário será de {s2} reais')
