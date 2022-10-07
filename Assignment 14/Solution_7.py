list=[1,2,3,'Hello',4.5,'my',5.5,4.8]
list1=[]
for i in list:
    if(type(i)==int):
        list1.append(i)
        
print(list1)