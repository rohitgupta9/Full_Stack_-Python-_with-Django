# Write a python script to store a hexadecimal number 2F in a variable and print it in
# octal format.


test_string = input("Enter Hexadecimal Number")
print("The original string : " +str(test_string))
res = int(test_string, 16)
# binary=bin(res)
octa=oct(res)
print("The decimal number of hexadecimal \string : " + str(res))
print("The octal number of Octal_number \string : " + str(octa))
# print(binary)