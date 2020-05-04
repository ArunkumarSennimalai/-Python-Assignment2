def compareTuple(tup1,tup2):
    greatertuple=tup2
    if cmp(tup1,tup2)==1:
        greatertuple=tup1
    return greatertuple

def findTupleLength(tup1):
    return len(tup1)

def maximumElement(tup1):
    return max(tup1)

def minimumElement(tup1):
    return min(tup1)

def convertToTuple(list1):
    return tuple(list1)
    
def deleteTuple(tup1):
    print "Tuple deleted is ", tup1
    del tup1
    
def countElement(tup1,element):
    return tup1.count(element) 

def findIndex(tup1,element):
    return tup1.index(element)


if __name__ == "__main__":
    try:
        tup1 = (34,23,45,12,25,67,89,33,77,12)
        tup2 = (5,53,65,45,36,67,76,99,10)
        tup3 = ("Eng","Math","Phy","Bot","Zoo","Comp")
        
        #cmp
        greatertuple = compareTuple(tup1,tup2)
        print "Greater tuple is", greatertuple
        
        #len
        length = findTupleLength(tup3)
        print "length of tuple",tup3, "is",length
        
        #max
        print "Max of int tuple is",maximumElement(tup1)
        print "Max of string tuple is",maximumElement(tup3)
        
        #min
        print "Min of int tuple is",minimumElement(tup1)
        print "Min of string tuple is",minimumElement(tup3)
        
        #Typecasting
        list1 = ['abcd','efgh','ijkl']
        tup4 =convertToTuple(list1)
        print tup4
        
        #delete tuple
        deleteTuple(tup2)
        
        
        #find count of specific element
        count = countElement(tup1,12)
        print "Count of element 12 in tuple",tup1,"is",count
            
        #finding index
        index = findIndex(tup3,"Bot")
        print "Index of element 'Bot' in tuple",tup3,"is",index
        
    except Exception as e:
        print(e)
        
        
