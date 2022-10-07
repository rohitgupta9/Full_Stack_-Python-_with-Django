# Here We  already know the formula of simple interest
# Simple Interest=(P*R*T)/100


# P--->Principal Ammount
# R---> rate of Interest
# T--->Time

principal_ammount=int(input("Enter the principal ammount"))
rate_of_interest=float(input("Enter the rate of interest"))
time=int(input("Enter the time of year like 1 year 2 year 3 year"))

Simple_Interest=(principal_ammount*rate_of_interest*time)/100
print("Simple Interest is :%f"%(Simple_Interest))