def stringFunctions():
    str1 ="Welcome to python\tprogramming course"
    
    #endswith
    print str1.endswith('course')
    print str1.endswith("Welcome",0,7)
    
    #expandtabs
    print str1
    print str1.expandtabs() #default size=8
    print str1.expandtabs(16)
    
    #find
    print str1.find("co")
    print str1.find("co",10,len(str1))
    print str1.find("hello")
    
    #index 
    print str1.index("co")
    print str1.index("co",10)
    #print str1.index("hello") #if not found, find method return -1 whereas index throws value error
    
    #join
    list1 = ['1','2','3']
    str2 = "-".join(list1)
    print str2


if __name__ == "__main__":
    try:
        stringFunctions()
    except Exception as e:
        print e
