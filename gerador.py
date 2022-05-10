from random import randint
print(f'{" GERADOR DE CPF ":*^36}')
print()
CPF = ''
for c in range(9):
    CPF += str(randint(0, 9))

c = 10
for loop in range(2):
    soma = 0
    digito = 0
    for num in CPF:
        soma += int(num) * c
        c -= 1

    digito = 11 - (soma % 11)
    if digito > 9:
        digito = 0
    CPF += str(digito)
    c = 11
print(CPF)
print(f'{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:]}')
