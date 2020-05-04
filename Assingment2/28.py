def VowelsFilter(str1):
   vowels = "aeiou"
   count=0
   dict1 = {}
   for c in str1:
       if c.isupper():
           c = c.lower()
       if c in vowels:
           if(c in dict1):
               dict1[c] += 1
           else:
               dict1[c]=1
           count +=1
   print 'ovals = ', count ,
   for i in dict1:
       print ",", i," = ",dict1[i],

if __name__ == "__main__":
        try:
           str1=input("Enter the string:")
           VowelsFilter(str1)
        except Exception as e:
            print e
