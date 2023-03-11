# Simulador de Caixa Eletrônico.

print("=" * 30)
print("{:^30}".format("BANCO DO DESENVOLVEDOR"))
print("=" * 30)

valor = int(input("Que valor você eseja sacar? R$ "))

total = valor
cedula = 50
totcedula = 0

while True:
    if total >= cedula:
        total = total - cedula
        totcedula = totcedula + 1

    else:
        if totcedula > 0:
            print(f"Total de {totcedula} cédulas de R$ {cedula}.")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 2
        totcedula = 0
        if total == 0:
            break
        
print("=" * 30)
print("VOLTE SEMPRE AO BANCO DO DESENVOLVEDOR.")
print("Tenha um bom dia!")