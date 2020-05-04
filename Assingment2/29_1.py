def stringFunctions():
        str1 = "welcome to the python programming course welcome"
        print "str.capitalize():",str1.capitalize()
        print "str.center(65,'*'):",str1.center(65,'*')
        print "str.count('welcome'):",str1.count('welcome')
        print "str.count('o',9,22):",str1.count('o',9,22)

        str1 = str1.encode('base64','strict')
        print "Encoded string is:",str1

        str1 = str1.decode('base64','strict')
        print "Decoded string is:",str1

if __name__ == "__main__":
        try:
           stringFunctions()
        except Exception as e:
                print e
        
