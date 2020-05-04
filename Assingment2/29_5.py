def stringFunctions():
    str1 = "    ***%%**Welcome To Python Programming Course**%%%***    "
    str2 = "Welcome-To-Python-Programming-Course"
    str3 = "843921"
    
    #strip
    print str1.strip(),"\n"
    
    #lstring
    print str1.lstrip(" *%"),"\n"
    
    #rstrip
    print str1.rstrip(" *%"),"\n"
    
    #max
    print max(str2)
    print max(str3),"\n"
    
    #min
    print min(str2)
    print min(str3),"\n"

if __name__ == "__main__":
    try:
        stringFunctions()
    except Exception as e:
        print e
        
