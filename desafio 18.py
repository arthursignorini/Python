import math
an = float(input('Digite o ângulo que voce deseja: '))
c = math.cos(math.radians(an))
s = math.sin(math.radians(an))
t = math.tan(math.radians(an))
print('O cosseno de {} é {:.2f}, o seno é {:.2f} e a tangente é {:.2f}'.format(an,c,s,t))