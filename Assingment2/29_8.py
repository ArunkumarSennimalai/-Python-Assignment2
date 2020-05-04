from string import maketrans

def stringFunctions():
    str1 = "welcome-to-python-programming-course"
    
    #startswith
    print str1.startswith("wel")
    print str1.startswith("python",11,60),"\n"
    
    #title()
    print str1.title(),"\n"
    
    #translate
    intab = "aeiou"
    outtab = "12345"
    trantab = maketrans(intab, outtab)
    print str1.translate(trantab),"\n"
    
    #zfill
    print str1.zfill(50),"\n"
    
    #isdecimal -- only for unicode
    str2 = u"1234"
    str3 = u"12ab3"
    print str2.isdecimal()
    print str3.isdecimal(),"\n"
    
    #splitline
    str4 = "WELCOME\nTO\nTHE\nCLASS"
    print str4.splitlines()


if __name__ == "__main__":
    try:
        stringFunctions()
    except Exception as e:
        print e
        
