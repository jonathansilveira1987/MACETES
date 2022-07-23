import cmath 
x = float(input('\nVetor A: '))
y = float(input('Vetor B: '))
z = complex(x,y); 
print ("\nA parte real do número complexo é: ",end="") 
print (z.real) 
print ("A parte imaginária do número complexo é: ",end="") 
print (z.imag)
print ("A fase do número complexo é: ",end="") 
print (cmath.phase(z))