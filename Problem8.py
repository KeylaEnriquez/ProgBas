#Ejercicio 8. Calculadora de año bisiesto

año=int(input('Ingresa el año a determinar: '))

if (año%4==0 and año%100!=0) or año%400==0:
    print(f'{año} sí es año bisiesto')
else:
    print(f'{año} no es año bisiesto')



