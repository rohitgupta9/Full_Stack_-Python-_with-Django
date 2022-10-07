# Write a python script which takes a three digit number from the user and displays
# only its middle digit.

number=int(input("Enter only three digit number"))
number1=number//10
number2=number1%10

print("First digit of number %d is %d:"%(number,number2))