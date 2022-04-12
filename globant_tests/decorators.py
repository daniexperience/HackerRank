from datetime import datetime as dt
from colorama import init, Fore

init()

def total_time(func):
    def wrapper(*args):
        
        start = dt.now()
        print(func(*args))
        end = dt.now()
        return (Fore.GREEN + 'Total Time Execution: ' + str(end - start) + Fore.RESET)
    return wrapper
    