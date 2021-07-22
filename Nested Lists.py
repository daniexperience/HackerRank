if __name__ == '__main__':
    estudiantes_temp = []
    estudiantes = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        estudiantes_temp.append([name, score])
    for item in estudiantes_temp:
        for elem in estudiantes_temp:
            if item[0] < elem[0]:
                estudiantes_temp.insert(0,item)

    print(estudiantes_temp)
    
    nombres = []
    puntajes = []

    for item in estudiantes:
        nombres.append(item[0])
        puntajes.append(item[1])
    #print(nombres)
    #print(puntajes)
    dicty = {}
    for item in estudiantes:
        dicty[item[0]] = item[1]
    #print(dicty)

    lista_total = sorted(nombres, key=dicty.__getitem__)
    
    print(lista_total[0])
    print(lista_total[1])
    
    finalistas = []
    