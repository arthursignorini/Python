d = int(input('A quantos km por hr o carro tava: '))
multa = (d - 80) * 7
if d >80:
    print(f'VOCE FOI MULTADO EM {multa} reais')
else:
    print('VOCE NÃO FOI MULTADO, PARABENS')
