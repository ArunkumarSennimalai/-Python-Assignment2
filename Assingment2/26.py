def decode(str1,encoding,errors):
    return str1.decode(encoding,errors)

if __name__ == '__main__':
    try:
        str1 = input("Enter the encode string") 
        print "Enter the algorithm used for encoding"
        encoding = input() #base64
        errors = input() #strict
        decodedstr = decode(str1,encoding='base64',errors='strict')
        print "Encodedstring: ", str1
        print "Decodedstring: ",decodedstr
    except Exception as e:
        print e
    

