def revers_name():
    name = input('nombre: ')
    last = input('apellido: ')
    nombre_apellido = name + ' ' + last
    apellido_nombre = ""
    con = len(nombre_apellido) - 1
    while con >= 0:
        apellido_nombre += nombre_apellido[con] + ' '
        con -= 1
    return apellido_nombre
revers_name()