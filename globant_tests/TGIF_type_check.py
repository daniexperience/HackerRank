# TEST GLOBANT FOR FIT INTERVIEW

def only_ints(a, b):
    return True if type(a) == int and type(b) == int else False

print(only_ints(1, 2)) # Output: True
print(only_ints('a', 2)) # Output: False
print(only_ints('1', 2)) # Output: False
print(only_ints(True, 2)) # Output: False