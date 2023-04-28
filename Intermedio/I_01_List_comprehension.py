### List Comprehension ###

my_original_list = [1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

# Es posible crear listas por comprensión
"""
Estoy creando listas que se están modificando al momento de crearlas.
Cada elemento o valor para cada indice de la lista se va modificando según yo le indique,
y todo esto en el momento de crear la lista.
"""
my_range_01 = range(8)
print(list(my_range_01))

my_list_01 = [i+1 for i in range(8)]
print(my_list_01)

my_list_02 = [i*2 for i in range(8)]
print(my_list_02)

def sum_five(number):
    return number +5

my_list_04 = [sum_five(i) for i in range(8)]
print(my_list_04)