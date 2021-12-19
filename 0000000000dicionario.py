


# Analisando e gerando Dicionários.

def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situacao da turma.
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] > 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['sitação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'       
    return r
# Programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)


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


# Aprimorando os Dicionários.
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper()[0]
        if resp in "SN":
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): ') )
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
       print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
       for i, g in enumerate(time[busca["gols"]]):
           print(f'   No jogo {i+1} fez {g} gols.')
print('-=' * 40)
print('<< VOLTE SEMPRE >>')