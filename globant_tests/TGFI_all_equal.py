# TEST GLOBANT FOR FIT INTERVIEW

from decorators import total_time

@total_time
def all_equal(lista):
    '''
    crear una funcion que valide que todos los elementos de una lista sean iguales
    '''
    y = lista[0]
    for x in range(0, len(lista)):

        if lista[x] != y:
            return False
        if x == len(lista)-1:
            return True
        
print(all_equal([1, 1, 2])) # False
print(all_equal([1, 2, 1])) # False
print(all_equal([2, 1, 1])) # False
print(all_equal([1, 1, 1])) # True

