import os
import funcion as fun
header = """
    ***************************************
    *     CENTRO DE SALUD CAMPUSLANDS     *
    *          CALCULADORA DE IMC         *
    ***************************************
    """
print (header)
nombre = input('Ingrese el nombre del Estudiante: ')
fun.data = 'peso (kg)'
fun.validacion()
fun.data = 'altura (m)'
fun.validacion()
os.system('cls')
print (header)
imc = fun.peso/(fun.altura**2)
if(imc >= 18.5 and imc <= 24.9):
    print(f'El Estudiante {nombre} presenta un IMC NORMAL con un {imc}')
elif(imc >= 25 and imc <= 29.9):
    print(f'El Estudiante {nombre} presenta un IMC SOBREPESO con un {imc}')
elif(imc >= 30 and imc <= 34.9):
    print(f'El Estudiante {nombre} presenta un IMC OBESIDAD I con un {imc}')
elif(imc >= 35 and imc <= 39.9):
    print(f'El Estudiante {nombre} presenta un IMC OBESIDAD II con un {imc}')
else:
    print(f'El Estudiante {nombre} presenta un IMC OBESIDAD III con un {imc}')