F = 0
C = 0
E = 0
R = int(input('Convertir température ? (1 c en f et 2 f en c'))
if R!=1:

    F = int(input('a convertir'))
    F = F-32
    F = F*5
    F = F/9
    E = F
else:
    C = int(input('a convertir'))
    C = C*9 
    C = C/5
    C = C+9
    E = C
print('c’est égal à', E)