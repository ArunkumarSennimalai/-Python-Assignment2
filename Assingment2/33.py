def appendToList(list1):
    list1.append('Hyderabad')
    print(list1)
def insertAt4thIndex(list1):
    list1.insert(4,"Kolkata")
    print(list1)
def sortingList(list1):
    list1.sort()
    print(list1)
def descendingSortList(list1):
    list1.sort(reverse=True)
    print(list1)
def popElement(list1):
    print "Deleted element is",list1.pop()
    print(list1)
    

if __name__ == "__main__":
    try:
        list1 = ['Banglore', 'Delhi', 'Mumbai', 'Pune', 'Chennai']
        print(list1)
        appendToList(list1)
        insertAt4thIndex(list1)
        sortingList(list1)
        descendingSortList(list1)
        popElement(list1)
        popElement(list1)
        popElement(list1)
    except Exception as e:
        print e
        
        
