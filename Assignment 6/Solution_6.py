number=int(input("Enter a number"))
count=0
while(number!=0):
    number=number//10
    count+=1
    
if(count==3):
    print("Number has 3 digit number")
else:
    print("Number has not 3 digit number")
    