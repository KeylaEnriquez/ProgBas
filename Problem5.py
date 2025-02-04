#Ejercicio 5. Calculadora de descuento

precio=int(input('Ingresa el precio del producto: '))
desc=int(input('Ingresa el porcentaje de descuento: '))

pfinal=precio-precio*(desc/100)

print(f'El precio con descuento del producto es de: {pfinal}')