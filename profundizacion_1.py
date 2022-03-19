# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

### probando Calculadora ###

#1ro Genero constantes:

SUMA = 1
RESTA = 2
MULTIPLICACION = 3
DIVISION = 4


print(f''' Calculadora Inove
{SUMA}) Suma
{RESTA}) Resta
{MULTIPLICACION}) Multiplicación
{DIVISION}) División''')

opc = int(input('Seleccione la operación deseada: '))

if SUMA <= opc <= DIVISION:
  nro_1 = float(input('Ingrese 1er nro:'))
  nro_2 = float(input('Ingrese 2do nro:'))
  if opc == SUMA:
    print('La suma entre',nro_1,'y',nro_2,'es:',nro_1 + nro_2)
  elif opc == RESTA:
    print('La resta entre',nro_1,'y',nro_2,'es:',nro_1 - nro_2)
  elif opc == MULTIPLICACION:
    print('La multiplicación entre', nro_1,'y',nro_2,'es:',nro_1 * nro_2 )
  elif opc == DIVISION:
    if nro_2 != 0:
      print('La división entre',nro_1,'y',nro_2,'es:',nro_1 / nro_2)
    else:
      print('NO dividirás por cero, Hereje!')  
else:
  print('Opción no válida')  

print('Hasta luego...')















