# Um print especial.

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


escreva('Jonathan Silveira')
escreva('Software Developer')
escreva('Instagram: @jonathandev')