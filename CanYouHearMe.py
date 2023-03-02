import random
import time

servicesAreUp = True

def getData50():
    if servicesAreUp and random.random() < 0.5:
        return 'You got the data! That only happens 50% of the time!'

def getData25():
    if servicesAreUp and random.random() < 0.25:
        return 'You got the data! That only happens 25% of the time!'    

def getData10():
    if servicesAreUp and random.random() < 0.1:
        return 'You got the data! That only happens 10% of the time!'
    

# Your code here!
def getWithRetry(dataFunc):
    listFunction = [getData50(), getData25(), getData10()]
    for function in listFunction:
        if function == getData50():
            for _ in range(0, 10):
                if function != None:
                    break
        elif function == getData25():
            for _ in range(0, 10):
                if function != None:
                    break
        elif function == getData10():
            for _ in range(0, 10):
                if function != None:
                    break 
    return function


getWithRetry(getData50)
print('is this running?')
getWithRetry(getData25)
getWithRetry(getData10)