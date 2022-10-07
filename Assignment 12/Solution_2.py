import math
n=int(input("Enter a number"))
for i in range(2,n):
    if n%i==0:
        print(f"Not Prime Number is {n}")
        break
else:
    print(f" Prime Number is {n}")