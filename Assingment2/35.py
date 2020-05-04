def printTupleElements(tuple1):
    for element in tuple1:
        print element,
    print "\v"
    
def concatenateTuples(tuple1,tuple2):
    tuple1 += tuple2
    return tuple1
    
def findingGreaterTuple(tup1,tup2,tup3):
    greatertuple=tup2
    if cmp(tup1,tup2)==1:
        greatertuple=tup1
    if cmp(tup3,greatertuple)==1:
        greatertuple=tup3
    print "Greater tuple is", greatertuple
    
def delTuple(tup1,tup2):
    try:
        #deleting entire tuple is possible
        del(tup2)
        #trying to delete tuple element will throw error
        del(tup1[0])
    except TypeError:
        print "Tuple doesn't support deletion"

def convertToList(tup1):
    return list(tup1)
    print list1
    list1.append(123)
    print list

def appendValueToList(list1,value):
    list1.append(value)
    
if __name__ == "__main__":
    try:
        #printing elements in tuple
        tuple1 = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
        printTupleElements(tuple1)
        
        tuple2 = ("January","February","March","April","May","June","July","August","September","October","November","December")
        printTupleElements(tuple2)
        
        #concatenating tuples
        tuple1 = concatenateTuples(tuple1,tuple2)
        printTupleElements(tuple1)
        
        #finding greater tuple
        tup1 = (34,23,45,12,25,67,89,33,77)
        tup2 = (5,53,65,45,36,67,76,99,10)
        tup3 = (66,55,1,23,9,98,76,45,34,33)    
        findingGreaterTuple(tup1,tup2,tup3)
        
        #tying to delete tuple element and entire tuple
        delTuple(tup1,tup2)
        
        #typecating to list 
        list1 = convertToList(tup1)
        
        #inserting value into list
        appendValueToList(list1,123)
        print list1
        
    except Exception as e:
        print(e)
        
        
