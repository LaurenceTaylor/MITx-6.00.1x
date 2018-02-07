# Exercise: is in
# Recursive bisection search

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''

    g = len(aStr) // 2
    
    if len(aStr) <= 1 and aStr != char:
        return False
    
    elif aStr[g] == char:
        return True
    
    elif aStr[g] > char:
        return isIn(char, aStr[0: g])
    
    else:
        return isIn(char, aStr[g: len(aStr)])
