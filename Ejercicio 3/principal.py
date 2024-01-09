import os
import funcion as fun
rta = True
count = [0]*5
while rta:
    fun.peso = 0
    fun.altura = 0
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
        count[0] = count[0] + 1
    elif(imc >= 25 and imc <= 29.9):
        print(f'El Estudiante {nombre} presenta un IMC SOBREPESO con un {imc}')
        count[1] = count[1] + 1
    elif(imc >= 30 and imc <= 34.9):
        print(f'El Estudiante {nombre} presenta un IMC OBESIDAD I con un {imc}')
        count[2] = count[2] + 1
    elif(imc >= 35 and imc <= 39.9):
        print(f'El Estudiante {nombre} presenta un IMC OBESIDAD II con un {imc}')
        count[3] = count[3] + 1
    elif(imc > 40):
        print(f'El Estudiante {nombre} presenta un IMC OBESIDAD III con un {imc}')
        count[4] = count[4] + 1
    try:
        rta = input('¿Desea ingresar otro estudiante? (Si/Enter) ')
    except ValueError:
        print('Dato incorrecto')
        os.system('pause')
header = """
        ****************************************
        *        REPORTE DE ESTUDIANTES        *
        ****************************************
        """
print(header)
print(f'Estudiantes con peso NORMAL: {count[0]}')
print(f'Estudiantes con SOBREPESO: {count[1]}')
print(f'Estudiantes con OBESIDAD I: {count[2]}')
print(f'Estudiantes con OBESIDAD II: {count[3]}')
print(f'Estudiantes con OBESIDAD II: {count[4]}')