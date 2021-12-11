# Dicionário em Python.

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['Situacao'] = 'Recuperação'
else:
    aluno['Situacao'] = 'Reprovado'
print("-=" * 30)
for k, v in aluno.items():
    print(f"  - {k} é igual a {v}.")