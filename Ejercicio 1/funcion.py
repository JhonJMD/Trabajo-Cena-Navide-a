num=[]
i = 0
def validacion():
    try:
        n = int(input(f"Ingrese un numero positivo: "))
        return n
    except ValueError:
        print("Debe ingresar valores numericos y enteros")
def addlist():
    global i
    n = validacion()
    while n < 0:
        print("Los numeros deben ser positivos")
        n = validacion()
    num.append(n)
    i+=1