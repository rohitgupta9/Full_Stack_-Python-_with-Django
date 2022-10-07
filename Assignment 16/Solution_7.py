# Write a python program to copy elements 4 and 5 from the following tuple into a new
# tuple. tuple1=(1,2,3,4,5,6)

tuple1=(1,2,3,4,5,6)
list1=list(tuple1)
list2=[]
list2.append(list1[3])
list2.append(list1[4])
print(tuple(list2))
