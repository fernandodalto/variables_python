# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
# De la segunda palabra tome las primeras dos letras, utilice el operador :
# Formar una nueva palabra con los recortes solicitados
# Imprima en pantalla los resultados

print('    Ejercicio 5    ')

extrae_1 = palabra_1[:3]
extrae_2 = palabra_2[:2]

print('Se extrajo lo siguiente: ')
print(extrae_1)
print(extrae_2)

suma = extrae_1 + extrae_2

print('La nueva palabra formada con los recortes es:',suma)
