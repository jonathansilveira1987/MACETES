from reportlab.pdfgen import canvas # pip install reportlab

try:
    nome_pdf = input('\nInforme o nome do PDF: ')
    elemento = int(input('\nInforme o número de elementos para a lista: '))
    print()
    listaFinal = [input("Dado: ") for i in range(elemento)]
    # pdf = canvas.Canvas("Site_Prefeitura.pdf")
    pdf = canvas.Canvas(f'{nome_pdf}.pdf')
    for cont, l in enumerate(listaFinal):
        # Lembre de mudar a posição para não sobrepor uma string com outra da lista
        pdf.drawString(100, 300-15*cont,l)
    pdf.save()
    print(f'\n{nome_pdf}.pdf gerado com sucesso!\n')
except:
    print(f'\nNão foi possível gerar o {nome_pdf}.pdf!\n')

# Caso o arquivo precise ter mais de uma página você pode usar a função pdf.showPage(). Veja esse exemplo abaixo:
from reportlab.pdfgen import canvas

pdf = canvas.Canvas('paginas.pdf')

pdf.drawString(100, 750, "Primeira página") # 100 é alinhado a esquerda.
pdf.showPage()
pdf.drawString(100, 750, "Segunda página") # 200 é alinhado centralizado.
pdf.showPage()
pdf.drawString(100, 750, "Terceira página") # 300 é alinhado a direita.
pdf.showPage()
pdf.save()