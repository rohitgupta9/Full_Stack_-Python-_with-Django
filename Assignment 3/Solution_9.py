# Write a python script to store an octal number 125 in a variable and print it in binary
# format

test_string = input("Enter octal Number")
print("The original string : " +str(test_string))
res = int(test_string, 8)
# binary=bin(res)
octa=bin(res)
print("The decimal number of hexadecimal \string : " + str(res))
print("The octal number of Octal_number \string : " + str(octa))
# print(binary)