import math
a=int(input("Enter the value of a: and a!=0"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
dis=b**2-4*a*c

if dis>0:
    root1=(-b+math.sqrt(dis))//(2*a)
    root2=(-b-math.sqrt(dis))//(2*a)
    print("Two distinct complex root are %.2f and %.2f" %(root1,root2))
    
    
elif dis==0:
    root1=root2=-b/(2*a)
    print("Two eqaul and real root are %.2f and %.2f" %(root1,root2))
    
    
elif dis<0:
    root1=root2=-b/(2*a)
    imaginary=math.sqrt(-dis)/(2*a)
    print("Two distinct root are %.2f+ %.2f and %.2f-%.2f"%(root1,imaginary,root2,imaginary))
    
    
    
    