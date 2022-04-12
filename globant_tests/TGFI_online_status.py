# TEST GLOBANT FOR FIT INTERVIEW

def online_count(elements):
    '''
    target:
        take a dictionary of elements and return the sum of online users
    
    params:
        elements: dict
    '''
    total = len([ (x, y) for x, y in elements.items() if y == 'online' ])
    return total

print(online_count({ 
    "Alice": "online",
    "Bob": "offline",
    "Eve": "offline",
    })) # Output: 1

print(online_count({ 
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    })) # Output: 2

print(online_count({ 
    "Alice": "online",
    "Bob": "online",
    "Eve": "online",
    })) # Output: 3

print(online_count({ 
    "Alice": "offline",
    "Bob": "offline",
    "Eve": "offline",
    })) # Output: 0