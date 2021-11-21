#Tema II_1
def my_function(*args):
    lista = [i for i in args]
    lista_numere = []
    sum = 0
    for j in lista:
       if type(j) == int or type(j) == float:
           lista_numere.append(j)
    for i in lista_numere:
        sum = i+sum
    return sum

a = my_function(1, 5, -3, "abc", [12, 56, "cad"])
print(a)