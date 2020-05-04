def stringFunctions():
    str1 = "        "
    str2 = "     A   "
    str3 = "Welcome To Python Programming Course"
    str4 = "Welcome to python programming course"
    str5 = "WELCOME TO PYTHON PROGRAMMING COURSE"
    
    #isspace
    print str1.isspace()
    print str2.isspace()
    print str3.isspace(),"\n"
    
    #istitle
    print str3.istitle()
    print str4.istitle()
    print str5.istitle(),"\n"
    
    #isupper
    print str3.isupper()
    print str4.isupper()
    print str5.isupper(),"\n"
    
    #ljust
    print str5.ljust(50,"#") #only char allowed not string
    print str5.ljust(20,'#'),"\n" #value less than length
    
    #rjust
    print str5.rjust(50,"#") #only char allowed not string

if __name__ == "__main__":
    try:
        stringFunctions()
    except Exception as e:
        print e
        
