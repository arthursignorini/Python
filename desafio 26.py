f = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A aparece {f.count('A')} na frase')
print(f'A primeira letra A está na posição {f.find('A')+1}')
print(f'A ultima letra A apareceu na posição {f.rfind('A')+1}')



