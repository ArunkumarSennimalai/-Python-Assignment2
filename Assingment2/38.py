def concatenateDict(tempdict1,tempdict2):
    tempdict1.update(tempdict2)

def updateDictSalary(tempdict1,Salary,percentageIncrease):
    tempdict1['Salary'] = int(tempdict1['Salary']*(1+(percentageIncrease/100.0)))

def updateDict(tempdict1,key,value):
    tempdict1[key] = value

def printDict(tempdict1):
    for key,values in tempdict1.items():
        print key,"=",values
    #delete 'Age'
    
def deleteElement(tempdict1,key):
    del(tempdict1[key])


if __name__ == "__main__":
    try:
        dict1 ={'Name':'Ramakrishna','Age':25}
        dict2={'EmpId':1234,'Salary':5000} 
        
        #concatenate
        concatenateDict(dict1,dict2)
        print dict1
        
        #updateSalaryBy10%percent
        updateDictSalary(dict1,'Salary',10)
        print dict1
        
        #updateage to 26
        updateDict(dict1,'Age',26)
        print dict1
        
        #insert into dict
        updateDict(dict1,'Grade','B1')
        print dict1
        
        #print elements in dict
        printDict(dict1)
       
        #delete elements in dict
        deleteElement(dict1,'Age')
        print dict1
        
                
    except Exception as e:
        print(e)
        
        
