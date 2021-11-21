import random
print('Curs3')
print('-----------------------')

# for i in range(10):
#     print(f"Set instructiuni [{i + 1}]")
#     print(f"random choice is: {random_choice}")
# while True:
#     random_choice = random.choice([i for i in range(1,11)])
#     if random_choice % 3 == 0:
#         break

# for i in range(20):
#     if i %2 !=0:
#         continue
#     print(f"Numar par:{i}")

# def get_sum(a, b):
#
#     return a + b
#
#
# my_sum =  get_sum(1, 2)
# print(my_sum)

# def my_function(param_1, param_2, param_3=3,param_4=4):
#     print('param_1', param_1)
#     print('param_2', param_2)
#     print('param_3', param_3)
#     print('param_4', param_4)
#
# my_function(1,2,param_4=4)


# my_var = input("Introduceti un nr: ")
#
# try:
#     my_int = int(my_var)
# except ValueError as e:
#     print("Va rog introduceti un nr")
# else:
#     pass
# finally:
#     pass

def my_function():
    def my_second_function():
        print(f"My second function {msg}")
    msg = "Hello World"
    my_second_function()
    print(f"My_function {msg}")
my_function()