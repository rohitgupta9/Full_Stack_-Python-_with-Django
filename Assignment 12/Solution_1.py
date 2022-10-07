n=int(input("Enter a number you want to reverse"))
reverse_number=0
while(n!=0):
    digit=n%10
    reverse_number=reverse_number*10+digit
    n=n//10
    

print(reverse_number)
    