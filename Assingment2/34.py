from statistics import mean


def createMaxList(WholeList):
    global maxlist
    maxlist = []
    for list in WholeList:
        list.sort()
        maxlist.extend(list[-2:])
    print("maxlist =",maxlist)

def createMinList(WholeList):
    global minlist
    minlist = []
    for list in WholeList:
        list.sort()
        minlist.extend(list[:2])
    print("minlist =",minlist)
        
def avgOfMaxList(maxlist):
    maxlistAvg = mean(maxlist)
    print("Average of maxlist is", maxlistAvg)
    
def avgOfMinList(minlist):
    minlistAvg = mean(minlist)
    print("Average of minlist is", minlistAvg)
    
if __name__ == "__main__":
    try:
        list1 = [34,23,45,12,25,67,89,33,77]
        list2 = [55,53,65,45,36,67,76,99,10]
        list3 = [66,55,1,23,9,98,76,45,34,33]
        WholeList = [list1,list2,list3]
        createMaxList(WholeList)
        createMinList(WholeList)
        avgOfMaxList(maxlist)
        avgOfMinList(minlist)
    except Exception as e:
        print(e)
        
        
