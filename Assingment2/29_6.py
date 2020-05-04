def stringFunctions():
    str1 = "Welcome-To-Python-Programming-Course"
    str2 = "WELCOME TO THE CLASS"
    
    #upper
    print str1.upper(),"\n"
    
    #lower
    print str2.lower(),"\n"
    
    #replace
    print str1.replace('o','$') 
    print str1.replace('o','$',3) #last argument is max replace
    
    #find
    print str1.find('o')
    print str1.find('o',8,16)
    
    #rfind
    print str1.rfind('o')
    print str1.rfind('o',8,16)


if __name__ == "__main__":
    try:
        stringFunctions()
    except Exception as e:
        print e
        
