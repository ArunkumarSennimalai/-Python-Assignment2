import math
def trignometricOperations(a,b):
    print "cos(",a,")", math.cos(a)
    print "sin(",a,")", math.sin(a)
    print "tan(",a,")", math.tan(a)
    print "acos(",a,")", math.acos(a)
    print "asin(",a,")", math.asin(a)
    print "atan(",a,")", math.atan(a)
    print "atan2(",a,b,")", math.atan2(a,b)
    print "hypot(",a,b,")", math.hypot(a,b)

if __name__ == "__main__":
    try:
        a=int(input("Enter value1:"))
        b=int(input("Enter value2:"))
        trignometricOperations(a,b)
    except Exception as e:
        print e

