r1 = int(input('Digite o tamanho da reta: '))
r2 = int(input('Digite o tamanho da reta: '))
r3 = int(input('Digite o tamanho da reta: '))
c1 = r1 + r2 > r3
c2 = r2 + r3 > r1
c3 = r1 + r3 > r2
if c1 or c2 or c3:
    print('É possivel formar um triangulo ')
else:
    print('Não é possivel formar um triangulo ')
