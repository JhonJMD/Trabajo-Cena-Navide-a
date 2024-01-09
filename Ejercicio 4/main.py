import os
isActive = True
result = [0]*8

while isActive:
    try:
        n = int(input("""
            Ingrese numeros enteros positivos 
            (Para finalizar ingrese un numero negativo): """))
    except ValueError:
        print('Dato incorrecto')
        os.system('pause')
    else:
        if (n < 0):
            isActive = False
        elif (n % 2 == 0):
            result[1] = result[1] + 1
            result[2] = result[2] + n
        else:
            result[3] = result[3] + 1
            result[4] = result[4] + n
        if (n <= 10):
            result[5] = result[5] + 1
        elif (n >= 10 and n <= 50):
            result[6] = result[6] + 1
        elif (n >= 100):
            result[7] = result[7] + 1
        if (n >= 0):
            result[0] = result[0] + 1
header = """
***************************
*        RESULTADO        *
***************************
"""
print(header)
print(f'Total números ingresados: {result[0]}')
print(f'Total números pares ingresados: {result[1]}')
print(f'Promedio de los números pares: {result[2]/result[1]}')
print(f'Promedio de los números impares: {result[4]/result[3]}')
print(f'Números menores de 10: {result[5]}')
print(f'Números entre 20 y 50: {result[6]}')
print(f'Números mayores a 100: {result[7]}')

