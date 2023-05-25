# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

letra = (input('\nDigite a letra que deseja descobrir: '))
if letra in "a,e,i,o,u,A,E,I,O,U":
    print(f'\n{letra} é uma vogal\n')
else:
    print(f'\n{letra} é uma consoante\n')

letra = (input('Digite a letra que deseja descobrir: '))
if letra in "a,e,i,o,u,A,E,I,O,U":
    print(f'\n{letra} é uma vogal\n')
else:
    if letra in "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z":
        print(f'\n{letra} é uma consoante\n')
    else:
        print(f'\n{letra} não é consoante nem vogal.\n')