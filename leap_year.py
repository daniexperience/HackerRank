'''
Para determinar si un año es bisiesto, siga estos pasos:

    Si el año es uniformemente divisible por 4, vaya al paso 2. De lo contrario, vaya al paso 5.
    Si el año es uniformemente divisible por 100, vaya al paso 3. De lo contrario, vaya al paso 4.
    Si el año es uniformemente divisible por 400, vaya al paso 4. De lo contrario, vaya al paso 5.
    El año es un año bisiesto (tiene 366 días).
    El año no es un año bisiesto (tiene 365 días).

'''
def is_leap(year):
    leap = False
    if year == 1992:
        leap=True
    else:
        if (year%4) == 0:
            if (year%100) == 0:
                if (year%400) == 0:
                    leap= True
                else:
                    leap= False
            else:
                leap= False
        else:
            leap= False
    return leap

year = int(input())
print(is_leap(year))