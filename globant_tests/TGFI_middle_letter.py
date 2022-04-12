# TEST GLOBANT FOR FIT INTERVIEW

import math as m
def middle_letter(string: str) -> str:
    if len(string) % 2 != 0:
        return string[( m.ceil(len(string)/2)-1 )]
    else:
        return ''

print(middle_letter("abcdefg")) # Output: 'd'
print(middle_letter("abcdef")) # Output: ''