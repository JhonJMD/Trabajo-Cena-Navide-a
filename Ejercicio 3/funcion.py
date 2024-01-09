import os
data = ''
peso = 0 
altura = 0
def validacion():
    global peso
    global altura
    try: 
        n = float(input(f'Ingrese el {data} del Estudiante: '))
    except ValueError:
        print('Dato incorrecto')
        os.system('pause')
    else: 
        if (data == 'peso (kg)'):
            peso = peso + n
        else:
            altura = altura + n