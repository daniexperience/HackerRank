from colorama import init, Fore
init()
from itertools import product
def maximize():
    contador=0
    seleccion = []

    firt_line = input("") # valores de la primera linea
    Sfirt_line = firt_line.split(" ") # separacion por espacio

    convercion_int = [int(num) for num in Sfirt_line]
    Max_valor = max(convercion_int)
    print(Fore.GREEN,*Sfirt_line,':',Max_valor,Fore.RESET)
    print(Fore.GREEN,*seleccion,Fore.RESET)
    
    while(contador<int(Sfirt_line[0])):
        valores= input("")
        Svalores=valores.split(" ")
        listadosNumero = [int(num.strip()) for num in Svalores]

        print(Fore.RED,'list nums:'+str(listadosNumero),Fore.RESET)

        del Svalores[0]
    
        seleccion.append(listadosNumero)
        contador+=1
    
    print(Fore.RED,*seleccion,Fore.RESET)

    productos = list(product(*seleccion))
    lresults = []
    for x in productos:
        sumatoria=0
        for y in x:
            sumatoria+=y**2
        lresults.append(sumatoria % Max_valor)
    resultado = max(lresults)
    return resultado
print(maximize())