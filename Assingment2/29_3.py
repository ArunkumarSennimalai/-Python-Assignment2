def stringFunctions():
    str1 ="welcome to python programming course"
    str2 = '2033'
    str3 = "123abcd4"
    str4 = "Python"
    #isalnum
    print str1.isalnum()
    print str2.isalnum()
    print str3.isalnum(),"\n"
    
    #isalpha
    print str1.isalpha() #only aplphabets no spaces or special char or numbers
    print str2.isalpha()
    print str4.isalpha(),"\n"
    
    #isdigit
    print str1.isdigit()
    print str2.isdigit()
    print str3.isdigit(),"\n"
    
    #islower
    print str1.islower()
    print str2.islower()
    print str3.islower()
    print str4.islower(),"\n"
    
    #isnumeric --only for unicode objects
    str5 = u"1234"
    str6 = u"a123b"
    str7 = u"abcd"
    #print str2.isnumeric() #throws error because isneric is applicable only to unicode objets
    print str5.isnumeric()
    print str6.isnumeric()
    print str7.isnumeric(),"\n"

if __name__ == "__main__":
    try:
        stringFunctions()
    except Exception as e:
        print e
        
