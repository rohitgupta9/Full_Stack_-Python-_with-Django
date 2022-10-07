# Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
# display the result in binary format.

test_string1 = input("Enter octal Number")
print("The original string : " +str(test_string1))
res = int(test_string1, 8)


test_string2=input("Enter a hexadecimal number ")
print("The original string : " +str(test_string1))
res1=int(test_string2,16)


res_bin=bin(res+res1)

print("Binary number \string : " + str(res_bin))
