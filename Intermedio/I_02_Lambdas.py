### Lambdas ###

# Es similar a una función, recibe parámtros y opera con ellas, pero es anónima.
# Su resultado se puede guardar en una variable

sum_two_values = lambda number_01, number_02: number_01 + number_02

# Para llamar a dicha lambda, llamamos la variable y le enviamos los parámetros 
print(sum_two_values(2, 5))
print(f"La suma es: {sum_two_values(2, 5)}")

# Otro ejemplo de lambda
multiply_values = lambda number_03, number_04: number_03*number_04 - 3
print(multiply_values(1, 9))

# Es posible dentro de una función llamar un lambda
def sum_three_values(num_05):
    return lambda num_01, num_02: num_01 + num_02 + num_05

print(sum_three_values(5)(2,  4))