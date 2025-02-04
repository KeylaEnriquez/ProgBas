#Ejercicio 3. Determinar par o impar

num=int(input('Ingresa un número:'))

res=num%2

if res==0:
    print(f'{num} es un número par')
else:
    print(f'{num} es un número impar')