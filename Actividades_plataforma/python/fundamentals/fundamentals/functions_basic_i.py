#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# Desplega el número 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# number_of_days_in_a_week_silicon_or_triangle_sides() no ha sido definido, por lo que habrá un error

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# Desplega el número 5


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# Se retornará el número 5, por lo que al imprimir se imprimirá sólo 5, omitiendo el print del interior

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# No deberia desplegar un número con print(x), sólo se imprime el 5 interior de la funcion

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# Deberia imprimir: 3,5. Posterior tira error

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# Debería imprimir en pantalla 25 como string contenado

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# Se imprime 100 y retorna el 10. Porterior se imprime el 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # retorna e imprime 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # retorna e imprime 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # retorna 21, imprime 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# Retorna 3+5, imprime 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# imprime 500. Se imprime 500 nuevamente, se imprime 300 desde la funcion y se imprime 500


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# imprime 500. Se imprime 500 nuevamente, se imprime 300 desde la funcion y se imprime 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# imprime 500. Se imprime 500 nuevamente, se imprime 300 desde la funcion y se imprime 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# imprime 1,3,2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# imprime 1,3,5,10