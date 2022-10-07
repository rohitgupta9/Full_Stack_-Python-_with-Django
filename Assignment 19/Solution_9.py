def test_range(n1,n2,n3):
    if n3 in range(n1,n2):
        print( "Number %s is in the range"%str(number3))
    else:
         print("The number is outside the given range.")
    
number1=int(input("Enter starting Number of range"))
number2=int(input("Enter ending Number of range"))
number3=int(input("Enter Number you want to check given range"))
test_range(number1,number2,number3)