# TEST COMPANY FIT INTERVIEW

def double_letters(string: str ) -> bool:
    y = string[0]
    for _ in range(len(string)):
        if _ == (len(string) - 1): return False
        elif y == string[_ + 1]: return True
        y = string[_+1]
        
print( double_letters("hello") ) # must print True
print( double_letters('on and off') ) # must print True
print( double_letters("helio") ) # must print False