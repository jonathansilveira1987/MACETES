# 16. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.
# Desenvolvido por Guilherme Louro
# Fonte: https://github.com/guilouro/Python-para-Zumbis/blob/master/Lista3/exercicio03_guilhermelouro_04.py

fibo = [1, 500]
i = 0
num = int(input("Entre com um número: "))

while num > len(fibo):
	fibo.append(fibo[i] + fibo[i+1])
	i+=1

print ('Fibonacci(%d): %d' %(num,fibo[num-1]))