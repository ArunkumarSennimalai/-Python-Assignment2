def binarysearch(list1,x):
    start = 0
    end = len(list1)-1
    while(start<=end):
        mid = start + (end-start)/2
        if list1[mid] == x:
            return mid
        elif x > list1[mid]:
            start = mid+1
        else:
            end = mid-1
    return -1
            
if __name__ == "__main__":
    try:
        sortedlist = [2,3,12,34,45,67,73,76,79,81,85,90,98,103,111]
        x = int(input("Enter the value to be found: "))
        position = binarysearch(sortedlist,x)
        if(position==-1):
            print "Element not found"
        else:
            print "Element found at position", position
    except ValueError:
            print "Enter only int value"
    except Exception as e:
        print e
        
