from faker import Faker

gerador = Faker

for i in range(10):
    print(gerador.name())
    print(gerador.adress())
    print('#' * 5)