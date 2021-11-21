#TemaII_3
def suma_totala(n):
    if n == 0:
        return 0
    return n + suma_totala(n-1)

print(suma_totala(7))
#--------------------------------#
def suma_para(n):
    sum = 0
    if n == 0:
        return n
    if n%2==0:
        sum+=n
    return sum + suma_para(n-1)

print(suma_para(5))
#--------------------------------#
def suma_impara(n):
    sum = 0
    if n == 1:
        return n
    if n%2==1:
        sum+=n
    return sum + suma_impara(n-1)

print(suma_impara(5))