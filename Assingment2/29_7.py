from string import maketrans

def stringFunctions():
    str1 = "Welcome-To-Python-Programming-Course"
    str2 = "WELCOME TO THE CLASS"
    
    #len
    print len(str1)
    print len(str2),"\n"
    
    #rindex
    print str1.rindex('co'),"\n"
    
    #maketrans
    intab = "aeiou"
    outtab = "AEIOU"
    trantab = maketrans(intab, outtab)
    print str1.translate(trantab),"\n"
    
    #split
    print str2.split()
    print str1.split("-",2),"\n"
    
    #swapcase
    print str1.swapcase()

if __name__ == "__main__":
    try:
        stringFunctions()
    except Exception as e:
        print e
        
