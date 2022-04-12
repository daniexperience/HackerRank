# TEST GLOBANT FOR FIT INTERVIEW

from decorators import total_time
    
# Forma 1
@total_time
def capitalize_indexes1(string, a = 'asd'):
    '''
    crear una funcion que retorne una lista con los indices de la letras mayusculas en un string
    '''
    lista = []
    for x in range(0, len(string)):
        if string[x].isupper():
            lista.append(x)
    return lista
    
# Forma 2
@total_time
def capitalize_indexes2(string, a = 'asd'):
    '''
    crear una funcion que retorne una lista con los indices de la letras mayusculas en un string
    '''    
    lista = [x for x in range(len(string)) if string[x].isupper()]
    return lista

print(capitalize_indexes1("hEllO"))
print(capitalize_indexes2("hElLO"))