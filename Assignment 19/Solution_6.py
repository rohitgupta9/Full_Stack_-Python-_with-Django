def max_number(*t):
    max_number=max(*t)
    print(*t)
    print(max_number)
    
# max_number(1,2,3,5)
number1=int(input("Enter 1st Number"))    
number2=int(input("Enter 2nd Number"))    
number3=int(input("Enter 3rd Number"))    
number4=int(input("Enter 4th Number"))   
max_number(number1,number2,number3,number4) 