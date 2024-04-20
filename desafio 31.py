d = int(input('Qual é a distancia da viagem: '))
c1 = d * 0.5
c2 = d * 0.45
if d <= 200:
    print(f'voce vai ter que pagar: {c1} reais')
else:
    print(f'voce vai ter que pagar: {c2} reais')
