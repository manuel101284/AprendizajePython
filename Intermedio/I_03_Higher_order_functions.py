### Higher Order Functions ###
"""
Estas son funciones que manipulan otras funciones.
Es decir son funciones que pueden recibir como parametros otras funciones.
"""
def sum_two_values_and_other(num_01, num_02, f_sum):
    return f_sum(num_01 + num_02)

def sum_one(value_01):
    return (value_01 + 1)

def sum_thirteen(value_01):
    return (value_01 + 13)

print(sum_two_values_and_other(5, 5, sum_one))
print(sum_two_values_and_other(5, 5, sum_thirteen))

### Closures ###

def sum_ten(value_02):
    def add_ten(value_03):
        return value_03 + 10 + value_02
    return add_ten

add_closure_01 = sum_ten(1)
print(add_closure_01(5))
print((sum_ten(5))(1))

### Built-in Higher Order Functions ###

numbers_01 = [2, 5, 10, 21, 34]

def multiply_two(number_01):
    return (number_01 * 2)

# Map
# Recorre todos los valores de una lista para modificarlos según se indique
print(list(map(multiply_two, numbers_01)))

print(list(map(lambda number: number * 2, numbers_01)))
print(list(map(lambda number: number * 7, numbers_01)))

# Filter
# Recorre todo los valores de una lista para ejecutar sobre ellos algún criterio de filtrado
numbers_02 = [2, 5, 7, 12, 9, 14, 8, 23]

def filter_bigger_that_ten(number):
    if (number > 10):
        return True
    else:
        return False

print(list(filter(filter_bigger_that_ten, numbers_02)))
print(list(filter(lambda number: number > 10, numbers_02)))
print(list(filter(lambda number: number % 2 == 0, numbers_02)))

# Reduce
# Toma como parametros el acumulado de alguna operación o proceso anteior y va sumando el elemento actual
from functools import reduce
numbers_03 = [3, 5, 8, 12, 23, 1, 43, 6, 17]

def sum_two_nums(val01, val02):
    print(val01)
    print(val02)
    return (val01 + val02)

print(reduce(sum_two_nums, numbers_03))