print(f'{" VALIDADOR DE CPF ":*^38}')
print()
while True:
    while True:
        CPF = input('Digite o CPF: ').replace('.', '').replace('-', '')
        if not CPF.isdigit():
            print('Por favor digite apenas números para o CPF.')
            continue
        elif len(CPF) < 11 or len(CPF) > 11:
            print('O CPF deve conter no total 11 digitos.')
            continue
        else:
            break

    novo_cpf = CPF[:9]

    c = 10
    for loop in range(2):
        s = 0
        digito = 0
        for n in novo_cpf:
            s = s + (int(n) * c)
            c -= 1

        digito = 11 - (s % 11)
        if digito > 9:
            digito = 0
        novo_cpf = novo_cpf + str(digito)
        c = 11

    sequencia = novo_cpf == novo_cpf[0] * len(CPF)

    print(f'{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:]}')
    if CPF == novo_cpf and not sequencia:
        print('Válido.')
    else:
        print('Inválido.')
    print()