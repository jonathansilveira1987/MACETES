def calcular_salario_liquido(salario_bruto):
    inss_aliquotas = [
        (1320.00, 0.075),
        (2571.29, 0.09),
        (3856.94, 0.14),
        (7507.49, 0.14),
    ]

    irpf_aliquotas = [
        (2112.00, 0),
        (2826.65, 0.075),
        (3751.05, 0.15),
        (4664.68, 0.225),
        (float('inf'), 0.275)
    ]

    inss = 0
    for limite, aliquota in inss_aliquotas:
        if salario_bruto <= limite:
            inss = salario_bruto * aliquota
            break
        else:
            inss = limite * aliquota

    irpf = 0
    for limite, aliquota in irpf_aliquotas:
        if salario_bruto <= limite:
            irpf = (salario_bruto - inss) * aliquota
            break

    salario_liquido = salario_bruto - inss - irpf

    return salario_liquido

salario_bruto = float(input('\nDigite o salário bruto: '))
salario_liquido = calcular_salario_liquido(salario_bruto)
print(f'\nO salário líquido é R$ {salario_liquido:.2f}\n')