wartosci= input()
lista= wartosci.split(',')
print(lista, type(lista))


for i in range(len(lista)):
    lista[i] = int(lista[i])

lista= [int(i) for i in lista]

print(lista, type (lista))

lista = list(map(int,lista))
print(lista)
