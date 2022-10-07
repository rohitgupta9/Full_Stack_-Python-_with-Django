def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)
 
 
myFun('Hello', 'Welcome', 'to', 'iNeuron')



# def f1(*t):
#     print(t)
    
# f1(10)
# f1(10,20)
# f1(10,20,30)
# f1(10,40,50,60)
# f1(10,70,80,90,100)




