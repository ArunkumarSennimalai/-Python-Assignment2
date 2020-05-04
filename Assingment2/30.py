def selectionsort(list1):
    for i in range(len(list1)):
        min=i
        for j in range(i+1,len(list1)):
            if(list1[min]>list1[j]):
                min=j
        list1[i],list1[min] = list1[min],list1[i]
    return list1

if __name__ == "__main__":
    try:
        list1 = [2,3,12,34,1,234,23,455,6778,233,22,12,11]
        sortedlist = selectionsort(list1)
        print sortedlist
    except Exception as e:
        print e
        
