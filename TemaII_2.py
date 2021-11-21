#TemaII_2
def my_function():
    while True:
        try:
            numarintrodus = int(input("Introduceti un numar: "))
        except ValueError:
            print("0")
            continue
        else:
            print(numarintrodus)
            break

my_function()