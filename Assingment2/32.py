def printCityWithLenAndFindBiggestAndSmallestCity(WholeList):
    biggestcity=WholeList[0][0]
    smallestcity=WholeList[0][0]
    for list in WholeList:
        minlen=len(list[0])
        maxlen=len(list[0])
        listbcity=list[0]
        listscity=list[0]
        for city in list:
            citylen = len(city)
            print city,citylen
            if minlen>citylen:
                minlen = citylen
                listscity = city
                if(len(smallestcity)>minlen):
                    smallestcity = city
            elif maxlen<citylen:
                maxlen = citylen
                listbcity = city
                if(len(biggestcity)<maxlen):
                    biggestcity = city
        print 'Maximum length element of ', list,'is',listbcity,'with length',maxlen
        print 'Minimum legth of ',list,'is',minlen,'is',listscity,'with length',minlen
    print smallestcity,"is the smallest city with length of ",len(smallestcity)
    print biggestcity,"is the biggest city with length of",len(biggestcity)
    
def deleteFirstAndLastElement(WholeList):
    for list in WholeList:
        del(list[0])
        del(list[-1])
        print list


if __name__ == "__main__":
    try:
        list1 = ['Banglore', 'Delhi', 'Mumbai', 'Pune', 'Chennai']
        list2 = ['Paris', 'Berlin', 'Moscow', 'Lyon', 'Mersaille']
        list3 = ['Washington', 'Miami', 'New Orleans', 'New york', 'Sacremento']
        Wholelist=[list1,list2,list3]
        printCityWithLenAndFindBiggestAndSmallestCity(Wholelist)
        deleteFirstAndLastElement(Wholelist)
    except Exception as e:
        print e
        
