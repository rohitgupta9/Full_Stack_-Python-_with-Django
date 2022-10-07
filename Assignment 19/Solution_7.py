def sum_of_list(*args):
    Total=sum(*args)
    print(Total)



List=list(map(int,input().split(" ")))
sum_of_list(List)