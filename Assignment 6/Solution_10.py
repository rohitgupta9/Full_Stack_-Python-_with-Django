a,b,c=map(int,input().split(' '))
# 10 20 40
# 10>20 10>40

# 20>10 20>40

# 40

if a>=b and a>c:
    print(f'{a} is Greater in given number')
    
elif b>c and b>a:
    print(f'{b} is greater all three among')
    
else:
    print(f'{c} is greater all three among')
    
