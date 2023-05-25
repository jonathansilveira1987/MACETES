# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade 
# de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo 
# usando este link (em minutos).
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

tamanho = float(input("Digite o tamando do arquivos que será baixado: "))
velocidade = float(input("Digite a velicodade de sua conexão de internet: "))
resultado = ((tamanho * 8) / velocidade) / 60
print ("O tempo aproximado de download é de %.2f minutos" %resultado)

# print('O tempo para que o download esteja completo será de :', resultado, 'segundos')