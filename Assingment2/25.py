def printDifferentDataTypes(a,b,c,d,e):
    #int
    print "%d"%a
    #float
    print "%f"%b
    #float with 2 precision
    print "%.2f"%b
    #string
    print "%s"%c
    #hex representation
    print "%x" %a
    #char
    print "%c"%e
    #exponential notation
    print "%e"%a
    #octal
    print "%o"%a
    #unsigned int
    print "%u"%a

if __name__ == '__main__':
    try:
        a=5289
        b=5.678954
        c="ABCD"
        d = True
        e='a'
        printDifferentDataTypes(a,b,c,d,e)
    except Exception as e:
        print e


