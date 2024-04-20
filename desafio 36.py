valor = float(input('valor da casa: '))
salario = float(input('salario: '))
anos = float(input('anos: '))
prestação = valor / anos / 12
if prestação > 0.3 * salario:
    print('seu emprestimo foi negado')
else:
    print('ok seu emprestimo foi aceito')

8
