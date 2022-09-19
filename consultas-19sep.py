# 1) Para modificar una variable global dentro de una funcion, se debe usar la palabra reservada 'global'?
# Pero me confunde que aunque no le ponga el 'global' igual puedo acceder a ella dentro de la funcion...

# Ejemplo 1
# animal = 'Perro'


# def set_animal(nuevo_animal):
#     animal = nuevo_animal  # variable local (no se modifica la global)


# print(animal)
# set_animal('Gato')
# print(animal)

# ============================================
# Ejemplo 2
# Modificar variable global desde una funcion
# animal = 'Perro'


# def set_animal(nuevo_animal):
#     global animal
#     animal = nuevo_animal  # variable global (se modifica la global)


# print(animal)
# set_animal('Gato')
# print(animal)

# ============================================
animal = 'Perro'


def print_animal():
    print(animal)


print_animal()
