#Ejercicio 1. Calculadora básica

a=int(input('Ingresa un número entero: '))
b=int(input('Ingresa otro número entero: '))

suma=a+b
print(f'La suma de {a} y {b} es: {suma}')

resta=a-b
print(f'La resta de {a} y {b} es: {resta}')

multiplicacion=a*b
print(f'La multiplicación de {a} y {b} es: {multiplicacion}')

division=a/b
print(f'La división de {a} y {b} es: {division}')

div_de_piso=a//b
print(f'La división entera de {a} y {b} es: {div_de_piso}')

residuo=a%b
print(f'El residuo de {a} y {b} es: {residuo}')