# TEST COMPANY FIT INTERVIEW

def double_letters(string: str ) -> bool:
    if  len(string)<=1: return False
    else:
        y = string[0]
        for _ in range(len(string)):
        
            if _ == (len(string) - 1): return False
            elif y == string[_ + 1]: return True
            y = string[_+1]

print( double_letters("hello") ) # Output: True
print( double_letters('on and off') ) # Output: True
print( double_letters("helio") ) # Output: False
print( double_letters("abc") ) # Output: False
print( double_letters("") ) # Output: False