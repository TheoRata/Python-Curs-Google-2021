# Tema 1

lista_numere = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(lista_numere)

lista_crescator = lista_numere[::]
lista_crescator.sort()
print(lista_crescator)

lista_descrescator = lista_numere[::]
lista_descrescator.sort(reverse=True)
print(lista_descrescator)

lista_par = lista_numere[::]
lista_par = lista_par[::2]
print(lista_par)

lista_impar = lista_numere[::]
lista_impar = lista_impar[1::2]
print(lista_impar)

lista_multiplii = lista_crescator[2:3] + lista_crescator[5:6] + lista_crescator[8:9]
print(lista_multiplii)

lista_goala = []
for i in lista_crescator:
    if i % 3 == 0:
        lista_goala.append(i)
print(lista_goala)

