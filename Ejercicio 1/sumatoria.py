import os
import funcion as fun
while fun.i < 3:
    fun.addlist()
if (len(fun.num) == 3):
    os.system("cls")
    print(fun.num)
    print(f"La sumatoria de los numeros ingresados es: {sum(fun.num)}")
    os.system("pause")
    isActive = False    