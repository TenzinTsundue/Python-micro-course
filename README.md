```
# Raise / Exception
"""
Creating
************
*          *
*          *
*          *
*          *
************
"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to a string of length 1.')

    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater then 2.')
    
    print(symbol * width)
    for i in range(height -2):
        print(symbol + (' ' * (width -2)) + symbol)
              
    print(symbol * width)
boxPrint('*' ,15, 5)
```

```
# Logging

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

logging.debug('Start of program')
                    
def factorial(n):
    logging.debug('Start of factorial(%s)' %(n))
    total = 1
    for i in range(n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    
    logging.debug('Return value is %s' % (total))                
    return total

print(factorial(5))

logging.debug('End of program')
```
