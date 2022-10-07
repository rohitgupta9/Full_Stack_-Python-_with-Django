def check_even_odd(n):
    if n%2==0:
        print( "Number %s is even number"%str(n))
    else:
        print("Number %s is odd number"%str(n))
        
        
check_even_odd(int(input("Enter a number you want to check even or odd")))