import math
import random
def operationOnNumbers():
    try:
        n=0.543
        print(round(n))
        val1 = input("Enter the number to find squareroot")
        sqrtval = math.sqrt(val1)
        print sqrtval
        print random.random()
        print random.uniform(1,100)
        print math.ceil(12.534)
        print math.floor(12.534)
        print math.trunc(12.984)
        print pow(2,3)
        print random.randint(1,10)
        print random.randrange(20,50)
    except Exception as e:
        print e

if __name__ == '__main__':
    operationOnNumbers()
