# Write a python script which takes a three digit number from the user and displays
# only its last digit.

number=int(input("Enter only three digit number"))
number1=number%10


print("First digit of number %d is %d:"%(number,number1))