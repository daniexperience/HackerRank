from itertools import permutations, combinations, combinations_with_replacement  
from colorama import init, Fore
init()
def comprehension(a, b, c, n):
    contenedor = []
    for x in range(a+1):
        #print(Fore.RED,x,Fore.RESET)
        for y in range(b+1):
            #print(Fore.YELLOW,y,Fore.RESET)
            for z  in range(c+1):
                #print(Fore.GREEN,z,Fore.RESET)
                if x+y+z != n:
                    #print([x,y,z])
                    contenedor.append([x,y,z])
    print(contenedor)
    

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    comprehension(x, y, z, n)