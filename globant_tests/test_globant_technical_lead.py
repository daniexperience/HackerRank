
# func input - list str, out str
# '1:hola|2:mundo|3:xyz'

# 1
def converter(lista: list):
    '''
    crear una funcion que reciba una lista de elementos y lo retorne en un formato distinto
    '''
    return '|'.join(str(num+1)+':'+element for num, element in enumerate(lista))

print(converter(['hola', 'mundo', 'xyz','hola']))
# 1:hola|2:mundo|3:xyz|4:hola

#--------------------------------------
# 2
# define f such that f(n)(m)==n+m
# example: print(f(3)(4)) would show 7

def f(n):
    def f2(m):
        return n+m
    return f2

print(f(3)(4))