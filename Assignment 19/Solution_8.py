def multiply_list(my_list):
    result=1
    for i in my_list:
        result=result*i
    return result

List=list(map(int,input().split(" ")))
print(multiply_list(List))
