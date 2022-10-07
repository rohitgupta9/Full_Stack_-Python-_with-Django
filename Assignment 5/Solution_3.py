#  Write a python script to swap data of two variables

# There are various method to swap data here we discuss two method 

number1=int(input("Enter 1st number"))
number2=int(input("Enter 2nd number"))
# here use 3rd variable to swap the number
print("Before swapping number is",number1,number2)
number3=number1
number1=number2
number2=number3
print("After Swapping number is:",number1,number2)

# Second method are used to swapp to number

number4=int(input("Enter 1st number"))
number5=int(input("Enter 2nd number"))
print("Before swapping number is",number4,number5)
number4,number5=number5,number4
print("After Swapping number is:",number4,number5)
