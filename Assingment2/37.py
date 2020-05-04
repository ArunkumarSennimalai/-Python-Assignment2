import json

def biggestDict(dict1,dict2,dict3):
    biggestDict = dict2
    if cmp(dict1,dict2):
        biggestDict = dict1
    if cmp(dict3,biggestDict):
        biggestDict = dict3
    return biggestDict

def addToDict(tempdict,key,val):
    tempdict[key] = val #dict2['l'] = 12
    
def addDictToAnotherDict(tempdict1,tempdict2):
    tempdict1.update(tempdict2) #dict1.update({'j':10,'k':11})

def findLength(tempdict):
    return len(tempdict)
    
def convertToStringAndConcatenate(dict1,dict2,dict3):
    return str(dict1) + str(dict2) + json.dumps(dict3) #str(dict3)


if __name__ == "__main__":
    try:
        dict1 = {'a':1,'b':2,'c':3}
        dict2 = {'d':4,'e':5,'f':6}
        dict3 = {'g':7,'h':8,'i':9}
        
        #finding biggest dict
        biggest = biggestDict(dict1,dict2,dict3)
        print "biggest dict is ", biggest
        
        #adding new elements to dict
        addDictToAnotherDict(dict1,{'j':10,'k':11})
        print dict1
        addToDict(dict2,'l',12)
        print dict2
        
        #printing length
        dict1_len = findLength(dict1)
        print "length of",dict1,"is",dict1_len
        dict2_len = findLength(dict2)
        print "length of",dict2,"is",dict2_len
        dict3_len = findLength(dict3)
        print "length of",dict3,"is",dict3_len
        
        #convert to string and concatenate
        str = convertToStringAndConcatenate(dict1,dict2,dict3)
        print "Final string is",str
        
    except Exception as e:
        print(e)
        
        
